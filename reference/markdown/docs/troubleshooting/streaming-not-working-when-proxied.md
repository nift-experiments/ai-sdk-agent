---
title: Streaming Not Working When Proxied
description: Troubleshooting streaming issues in proxied apps.
url: "https://ai-sdk.dev/docs/troubleshooting/streaming-not-working-when-proxied"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

Streaming with the AI SDK doesn't work in local development environment, or deployed in some proxy environments.
Instead of streaming, only the full response is returned after a while.

## Cause

The causes of this issue are caused by the proxy middleware.

If the middleware is configured to compress the response, it will cause the streaming to fail.

## Solution

You can try the following, the solution only affects the streaming API:

- add `'Content-Encoding': 'none'` headers

  ```tsx
  return createUIMessageStreamResponse({
    stream: toUIMessageStream({ stream: result.stream }),
    headers: {
      'Content-Encoding': 'none',
    },
  });
  ```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)