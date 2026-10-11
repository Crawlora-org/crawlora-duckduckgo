import { DuckDuckGoClient } from "../src/index.js";

const client = new DuckDuckGoClient({ apiKey: "test-key" });
void client.image({"q": "sample"});
void client.request("duckduckgo-image", {"q": "sample"});
const streamResponse: Promise<Response> = client.request("duckduckgo-image", {"q": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("duckduckgo-image", {"q": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.image({"q": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("duckduckgo-image", {"q": "sample", "page": 1, "region": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("duckduckgo-image", {"q": "sample"}, { responseType: "text" });
void rawText;



// @ts-expect-error The selected operation requires its documented params.
void client.image();
