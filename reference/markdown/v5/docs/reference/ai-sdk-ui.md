---
title: AI SDK UI
description: Reference documentation for the AI SDK UI
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-ui"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

[AI SDK UI](/v5/docs/ai-sdk-ui) is designed to help you build interactive chat, completion, and assistant applications with ease.
It is framework-agnostic toolkit, streamlining the integration of advanced AI functionalities into your applications.

AI SDK UI contains the following hooks:

#### [useChat](/v5/docs/reference/ai-sdk-ui/use-chat)

Use a hook to interact with language models in a chat interface.

#### [useCompletion](/v5/docs/reference/ai-sdk-ui/use-completion)

Use a hook to interact with language models in a completion interface.

#### [useObject](/v5/docs/reference/ai-sdk-ui/use-object)

Use a hook for consuming a streamed JSON objects.

#### [convertToModelMessages](/v5/docs/reference/ai-sdk-ui/convert-to-model-messages)

Convert useChat messages to ModelMessages for AI functions.

#### [pruneMessages](/v5/docs/reference/ai-sdk-ui/prune-messages)

Prunes model messages from a list of model messages.

#### [createUIMessageStream](/v5/docs/reference/ai-sdk-ui/create-ui-message-stream)

Create a UI message stream to stream additional data to the client.

#### [createUIMessageStreamResponse](/v5/docs/reference/ai-sdk-ui/create-ui-message-stream-response)

Create a response object to stream UI messages to the client.

#### [pipeUIMessageStreamToResponse](/v5/docs/reference/ai-sdk-ui/pipe-ui-message-stream-to-response)

Pipe a UI message stream to a Node.js ServerResponse object.

#### [readUIMessageStream](/v5/docs/reference/ai-sdk-ui/read-ui-message-stream)

Transform a stream of UIMessageChunk objects into an AsyncIterableStream of UIMessage objects.

## UI Framework Support

AI SDK UI supports the following frameworks: [React](https://react.dev/), [Svelte](https://svelte.dev/), and [Vue.js](https://vuejs.org/).
Here is a comparison of the supported functions across these frameworks:

| Function                                                  | React | Svelte             | Vue.js |
| --------------------------------------------------------- | ----- | ------------------ | ------ |
| [useChat](/v5/docs/reference/ai-sdk-ui/use-chat)             | ✓     | ✓ Chat             | ✓      |
| [useCompletion](/v5/docs/reference/ai-sdk-ui/use-completion) | ✓     | ✓ Completion       | ✓      |
| [useObject](/v5/docs/reference/ai-sdk-ui/use-object)         | ✓     | ✓ StructuredObject | ✗      |

[Contributions](https://github.com/vercel/ai/blob/main/CONTRIBUTING.md) are
welcome to implement missing features for non-React frameworks.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)