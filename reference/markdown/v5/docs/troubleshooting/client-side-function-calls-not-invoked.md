---
title: Client-Side Function Calls Not Invoked
description: Troubleshooting client-side function calls not being invoked.
url: "https://ai-sdk.dev/v5/docs/troubleshooting/client-side-function-calls-not-invoked"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

I upgraded the AI SDK to v3.0.20 or newer. I am using [`OpenAIStream`](/v5/docs/reference/stream-helpers/openai-stream). Client-side function calls are no longer invoked.

## Solution

You will need to add a stub for `experimental_onFunctionCall` to [`OpenAIStream`](/v5/docs/reference/stream-helpers/openai-stream) to enable the correct forwarding of the function calls to the client.

```tsx
const stream = OpenAIStream(response, {
  async experimental_onFunctionCall() {
    return;
  },
});
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)