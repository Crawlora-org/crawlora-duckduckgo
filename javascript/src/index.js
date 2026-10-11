import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class DuckDuckGoClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-duckduckgo-js/0.1.0" });
    this["image"] = (...args) => this.request("duckduckgo-image", ...args);
    this["news"] = (...args) => this.request("duckduckgo-news", ...args);
    this["search"] = (...args) => this.request("duckduckgo-search", ...args);
    this["shopping"] = (...args) => this.request("duckduckgo-shopping", ...args);
    this["suggest"] = (...args) => this.request("duckduckgo-suggest", ...args);
    this["video"] = (...args) => this.request("duckduckgo-video", ...args);
  }
}

export { DuckDuckGoClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default DuckDuckGoClient;
