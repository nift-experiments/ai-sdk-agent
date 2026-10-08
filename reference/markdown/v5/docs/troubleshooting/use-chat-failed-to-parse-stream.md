---
title: useChat Failed to Parse Stream
description: Troubleshooting errors related to the Use Chat Failed to Parse Stream error.
url: "https://ai-sdk.dev/v5/docs/troubleshooting/use-chat-failed-to-parse-stream"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

I am using [`useChat`](/v5/docs/reference/ai-sdk-ui/use-chat) or [`useCompletion`](/v5/docs/reference/ai-sdk-ui/use-completion), and I am getting a `"Failed to parse stream string. Invalid code"` error. I am using version `3.0.20` or newer of the AI SDK.

## Background

The AI SDK has switched to the stream data protocol in version `3.0.20`.
[`useChat`](/v5/docs/reference/ai-sdk-ui/use-chat) and [`useCompletion`](/v5/docs/reference/ai-sdk-ui/use-completion) expect stream parts that support data, tool calls, etc.
What you see is a failure to parse the stream.
This can be caused by using an older version of the AI SDK in the backend, by providing a text stream using a custom provider, or by using a raw LangChain stream result.

## Solution

You can switch [`useChat`](/v5/docs/reference/ai-sdk-ui/use-chat) and [`useCompletion`](/v5/docs/reference/ai-sdk-ui/use-completion) to raw text stream processing with the [`streamProtocol`](/v5/docs/reference/ai-sdk-ui/use-completion#stream-protocol) parameter.
Set it to `text` as follows:

```tsx
const { messages, append } = useChat({ streamProtocol: 'text' });
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)