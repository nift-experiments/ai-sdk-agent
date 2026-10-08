---
title: AnthropicStream
description: Learn to use AnthropicStream helper function in your application.
url: "https://ai-sdk.dev/v5/docs/reference/stream-helpers/anthropic-stream"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

AnthropicStream has been removed in AI SDK 4.0.

AnthropicStream is part of the legacy Anthropic integration. It is not
compatible with the AI SDK 3.1 functions. It is recommended to use the [AI SDK
Anthropic Provider](/v5/providers/ai-sdk-providers/anthropic) instead.

It is a utility function that transforms the output from Anthropic's SDK into a ReadableStream. It uses AIStream under the hood, applying a specific parser for the Anthropic's response data structure.

## Import

### React

```
import { AnthropicStream } from "ai"
```

## API Signature

### Parameters

- `response` (`Response`): The response object returned by a call made by the Provider SDK.
- `callbacks?` (`AIStreamCallbacksAndOptions`): An object containing callback functions to handle the start, each token, and completion of the AI response. In the absence of this parameter, default behavior is implemented.
  - `AIStreamCallbacksAndOptions`
    - `onStart` (`() => Promise<void>`): An optional function that is called at the start of the stream processing.
    - `onCompletion` (`(completion: string) => Promise<void>`): An optional function that is called for every completion. It's passed the completion as a string.
    - `onFinal` (`(completion: string) => Promise<void>`): An optional function that is called once when the stream is closed with the final completion message.
    - `onToken` (`(token: string) => Promise<void>`): An optional function that is called for each token in the stream. It's passed the token as a string.

### Returns

A `ReadableStream`.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)