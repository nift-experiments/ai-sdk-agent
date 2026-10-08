---
title: createAgentUIStream
description: API Reference for the createAgentUIStream utility.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/create-agent-ui-stream"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The `createAgentUIStream` function executes an [Agent](/v6/docs/reference/ai-sdk-core/agent), consumes an array of UI messages, and streams the agent's output as UI message chunks via an async iterable. This enables real-time, incremental rendering of AI assistant output with full access to tool use, intermediate reasoning, and interactive UI features in your own runtime—perfect for building chat APIs, dashboards, or bots powered by agents.

## Import

```
import { createAgentUIStream } from "ai"
```

## Usage

```ts
import { ToolLoopAgent, createAgentUIStream } from 'ai';

const agent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: 'You are a helpful assistant.',
  tools: { weather: weatherTool, calculator: calculatorTool },
});

export async function* streamAgent(
  uiMessages: unknown[],
  abortSignal?: AbortSignal,
) {
  const stream = await createAgentUIStream({
    agent,
    uiMessages,
    abortSignal,
    // ...other options (see below)
  });

  for await (const chunk of stream) {
    yield chunk; // Each chunk is a UI message output from the agent.
  }
}
```

## Parameters

- `agent` (`Agent`): The agent to run. Must define its \`tools\` and implement \`.stream(\{ prompt, ... })\`.
- `uiMessages` (`unknown[]`): Array of input UI message objects (e.g., user/assistant/chat history). These will be validated and converted for the agent.
- `abortSignal` (`AbortSignal`): Optional abort signal to cancel the stream early (for example, if the client disconnects).
- `timeout` (`number | { totalMs?: number }`): Timeout in milliseconds. Can be specified as a number or as an object with a totalMs property. The call will be aborted if it takes longer than the specified timeout. Can be used alongside abortSignal.
- `options` (`CALL_OPTIONS`): Optional agent call options, only needed if your agent expects extra configuration (see agent generic parameters).
- `experimental_transform` (`StreamTextTransform | StreamTextTransform[]`): Optional transformations to apply to the agent output stream (experimental).
- `onStepFinish` (`ToolLoopAgentOnStepFinishCallback`): Callback invoked after each agent step (LLM/tool call) completes. Useful for tracking token usage or logging intermediate steps.
- `...UIMessageStreamOptions` (`UIMessageStreamOptions`): Additional options to control the output stream, such as including sources or usage data.

## Returns

A `Promise<AsyncIterableStream<UIMessageChunk>>`, where each yielded chunk is a UI message output from the agent (see [`UIMessage`](/v6/docs/reference/ai-sdk-core/ui-message)). This can be consumed with any async iterator loop, or piped to a streaming HTTP response, socket, or any other sink.

## Example

```ts
import { createAgentUIStream } from 'ai';

const controller = new AbortController();

const stream = await createAgentUIStream({
  agent,
  uiMessages: [{ role: 'user', content: 'What is the weather in SF today?' }],
  abortSignal: controller.signal,
  sendStart: true,
  // ...other UIMessageStreamOptions
});

for await (const chunk of stream) {
  // Each chunk is a UI message update — stream it to your client, dashboard, logs, etc.
  console.log(chunk);
}

// Call controller.abort() to cancel the agent operation early.
```

## How It Works

1. **UI Message Validation:** The input `uiMessages` array is validated and normalized using the agent's `tools` definition. Any invalid messages cause an error.
2. **Conversion to Model Messages:** The validated UI messages are converted into model-specific message format, as required by the agent.
3. **Agent Streaming:** The agent's `.stream({ prompt, ... })` method is invoked with the converted model messages, optional call options, abort signal, and any experimental transforms.
4. **UI Message Stream Building:** The result stream is converted and exposed as a streaming async iterable of UI message chunks for you to consume.

## Notes

- The agent **must** implement the `.stream({ prompt, ... })` method and define its supported `tools` property.
- This utility returns an async iterable for maximal streaming flexibility. For HTTP responses, see [`createAgentUIStreamResponse`](/v6/docs/reference/ai-sdk-core/create-agent-ui-stream-response) (Web) or [`pipeAgentUIStreamToResponse`](/v6/docs/reference/ai-sdk-core/pipe-agent-ui-stream-to-response) (Node.js).
- The `uiMessages` parameter is named `uiMessages`, **not** just `messages`.
- You can provide advanced options via `UIMessageStreamOptions` (for example, to include sources or usage).
- To cancel the stream, pass an [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) via the `abortSignal` parameter.

## See Also

- [`Agent`](/v6/docs/reference/ai-sdk-core/agent)
- [`ToolLoopAgent`](/v6/docs/reference/ai-sdk-core/tool-loop-agent)
- [`UIMessage`](/v6/docs/reference/ai-sdk-core/ui-message)
- [`createAgentUIStreamResponse`](/v6/docs/reference/ai-sdk-core/create-agent-ui-stream-response)
- [`pipeAgentUIStreamToResponse`](/v6/docs/reference/ai-sdk-core/pipe-agent-ui-stream-to-response)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)