---
title: Azure OpenAI Slow to Stream
description: Learn to troubleshoot Azure OpenAI slow to stream issues.
url: "https://ai-sdk.dev/v6/docs/troubleshooting/azure-stream-slow"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

When using OpenAI hosted on Azure, streaming is slow and in big chunks.

## Cause

This is a Microsoft Azure issue. Some users have reported the following solutions:

- **Update Content Filtering Settings**:
  Inside [Azure AI Studio](https://ai.azure.com/), within "Shared resources" > "Content filters", create a new
  content filter and set the "Streaming mode (Preview)" under "Output filter" from "Default"
  to "Asynchronous Filter".

## Solution

You can use the [`smoothStream` transformation](/v6/docs/ai-sdk-core/generating-text#smoothing-streams) to stream each word individually.

```tsx {6}
import { smoothStream, streamText } from 'ai';

const result = streamText({
  model,
  prompt,
  experimental_transform: smoothStream(),
});
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)