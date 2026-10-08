---
title: AI_APICallError
description: Learn how to fix AI_APICallError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-api-call-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when an API call fails.

## Properties

- `url`: The URL of the API request that failed
- `requestBodyValues`: The request body values sent to the API
- `statusCode`: The HTTP status code returned by the API
- `responseHeaders`: The response headers returned by the API
- `responseBody`: The response body returned by the API
- `isRetryable`: Whether the request can be retried based on the status code
- `data`: Any additional data associated with the error

## Checking for this Error

You can check if an error is an instance of `AI_APICallError` using:

```typescript
import { APICallError } from 'ai';

if (APICallError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)