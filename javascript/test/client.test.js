import test from "node:test";
import assert from "node:assert/strict";
import {
  DuckDuckGoClient, CrawloraClientError, CrawloraNetworkError,
  CrawloraServerError, groups, operations, operationCount
} from "../src/index.js";

const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json", ...headers }
});

test("exports only this platform and exposes direct and grouped methods", async () => {
  const client = new DuckDuckGoClient({ apiKey: "test-key", fetch: async () => json({ ok: true }) });
  assert.equal(operationCount, Object.keys(operations).length);
  assert.deepEqual(Object.keys(groups), ["duckduckgo"]);
  assert.equal(typeof client["image"], "function");
  assert.equal(typeof client["duckduckgo"]["image"], "function");
});

test("serializes required query/path values, adds API key and platform User-Agent", async () => {
  let seen;
  const client = new DuckDuckGoClient({ apiKey: "secret", fetch: async (url, init) => {
    seen = { url: String(url), headers: init.headers };
    return json({ ok: true });
  } });
  await client.request("duckduckgo-image", {"q": "sample"});
  assert.match(seen.url, /\/duckduckgo\/image/);
  assert.equal(seen.headers["x-api-key"], "secret");
  assert.equal(seen.headers["user-agent"], "crawlora-duckduckgo-js/0.1.1");
});

test("allows caller User-Agent override and response text mode", async () => {
  let seen;
  const client = new DuckDuckGoClient({ apiKey: "key", userAgent: "custom-agent", fetch: async (_url, init) => {
    seen = init.headers;
    return new Response("caption text", { headers: { "content-type": "text/plain" } });
  } });
  const result = await client.request("duckduckgo-image", {"q": "sample"}, { responseType: "text" });
  assert.equal(seen["user-agent"], "custom-agent");
  assert.equal(result, "caption text");

  const rawFeed = "1~home|2~away\n";
  const autoClient = new DuckDuckGoClient({ fetch: async () => new Response(rawFeed, {
    headers: { "content-type": "text/plain" }
  }) });
  assert.equal(await autoClient.request("duckduckgo-image", {"q": "sample"}), rawFeed);
});

test("maps API errors and retries server failures", async () => {
  let calls = 0;
  const client = new DuckDuckGoClient({ apiKey: "key", retries: 1, retryDelay: 0, fetch: async () => {
    calls++;
    return calls === 1 ? json({ msg: "try again" }, 503) : json({ ok: true });
  } });
  assert.deepEqual(await client.request("duckduckgo-image", {"q": "sample"}), { ok: true });
  assert.equal(calls, 2);

  const bad = new DuckDuckGoClient({ fetch: async () => json({ msg: "bad input" }, 400) });
  await assert.rejects(bad.request("duckduckgo-image", {"q": "sample"}), CrawloraClientError);
  const down = new DuckDuckGoClient({ fetch: async () => json({ msg: "down" }, 503) });
  await assert.rejects(down.request("duckduckgo-image", {"q": "sample"}), CrawloraServerError);
});

test("reports timeout and caller cancellation as network errors", async () => {
  const hanging = (_url, { signal }) => new Promise((_resolve, reject) => {
    signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true });
  });
  const timed = new DuckDuckGoClient({ timeout: 5, fetch: hanging });
  await assert.rejects(timed.request("duckduckgo-image", {"q": "sample"}), CrawloraNetworkError);

  const controller = new AbortController();
  const aborted = new DuckDuckGoClient({ fetch: hanging });
  const pending = aborted.request("duckduckgo-image", {"q": "sample"}, { signal: controller.signal });
  controller.abort();
  await assert.rejects(pending, CrawloraNetworkError);
});
