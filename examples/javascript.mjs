import { DuckDuckGoClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new DuckDuckGoClient({ apiKey });

  const search = await client.search({ q: "open source web crawler" });
  console.log("search", search);
  const news = await client.news({ q: "technology" });
  console.log("news", news);
