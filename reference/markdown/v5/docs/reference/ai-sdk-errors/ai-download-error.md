---
title: AI_DownloadError
description: Learn how to fix AI_DownloadError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-download-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when a download fails.

## Properties

- `url`: The URL that failed to download
- `statusCode`: The HTTP status code returned by the server
- `statusText`: The HTTP status text returned by the server
- `message`: The error message containing details about the download failure

## Checking for this Error

You can check if an error is an instance of `AI_DownloadError` using:

```typescript
import { DownloadError } from 'ai';

if (DownloadError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)