---
title: createAgentUIStreamResponse
description: API Reference for the createAgentUIStreamResponse utility.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/create-agent-ui-stream-response"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The `createAgentUIStreamResponse` function executes an [Agent](/v6/docs/reference/ai-sdk-core/agent), runs its streaming output as a UI message stream, and returns an HTTP [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object whose body is the live, streaming UI message output. This is designed for API routes that deliver real-time agent results, such as chat endpoints or streaming tool-use operations.

## Import

```
import { createAgentUIStreamResponse } from "ai"
```

## Usage

```ts
import { ToolLoopAgent, createAgentUIStreamResponse } from 'ai';

const agent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: 'You are a helpful assistant.',
  tools: { weather: weatherTool, calculator: calculatorTool },
});

export async function POST(request: Request) {
  const { messages } = await request.json();

  // Optional: support cancellation (aborts on disconnect, etc.)
  const abortController = new AbortController();

  return createAgentUIStreamResponse({
    agent,
    uiMessages: messages,
    abortSignal: abortController.signal, // optional
    // ...other UIMessageStreamOptions like sendSources, experimental_transform, etc.
  });
}
```

## Parameters

- `agent` (`Agent`): The agent instance to stream responses from. Must implement \`.stream(\{ prompt, ... })\` and define the \`tools\` property.
- `uiMessages` (`unknown[]`): Array of input UI messages provided to the agent (e.g., user and assistant messages).
- `abortSignal` (`AbortSignal`): Optional abort signal to cancel streaming, e.g., on client disconnect. This should be an \[\`AbortSignal\`]\(https\://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) instance.
- `timeout` (`number | { totalMs?: number }`): Timeout in milliseconds. Can be specified as a number or as an object with a totalMs property. The call will be aborted if it takes longer than the specified timeout. Can be used alongside abortSignal.
- `options` (`CALL_OPTIONS`): Optional agent call options, for agents with generic parameter \`CALL\_OPTIONS\`.
- `experimental_transform` (`StreamTextTransform | StreamTextTransform[]`): Optional stream transforms to post-process text output—the same as in lower-level streaming APIs.
- `onStepFinish` (`ToolLoopAgentOnStepFinishCallback`): Callback invoked after each agent step (LLM/tool call) completes. Useful for tracking token usage or logging intermediate steps.
- `...UIMessageStreamOptions` (`UIMessageStreamOptions`): Other UI message output options—such as \`sendSources\` and more.
- `headers` (`HeadersInit`): Optional HTTP headers to include in the Response object.
- `status` (`number`): Optional HTTP status code.
- `statusText` (`string`): Optional HTTP status text.
- `consumeSseStream` (`(options: { stream: ReadableStream<string> }) => PromiseLike<void> | void`): Optional function to consume the SSE stream. When provided, this function will be called with the SSE stream to handle consumption.

## Returns

A `Promise<Response>` whose `body` is a streaming UI message output from the agent. Use this as the return value of API/server handlers in serverless, Next.js, Express, Hono, or edge runtime contexts.

## Example: Next.js API Route Handler

```ts
import { createAgentUIStreamResponse } from 'ai';
import { MyCustomAgent } from '@/agent/my-custom-agent';

export async function POST(request: Request) {
  const { messages } = await request.json();

  return createAgentUIStreamResponse({
    agent: MyCustomAgent,
    uiMessages: messages,
    sendSources: true, // (optional)
    // headers, status, abortSignal, and other UIMessageStreamOptions also supported
  });
}
```

## How It Works

- 1. **UI Message Validation:** Validates the incoming `uiMessages` array according to the agent's specified tools and requirements.
- 2. **Model Message Conversion:** Converts validated UI messages into the internal model message format for the agent.
- 3. **Streaming Agent Output:** Invokes the agent’s `.stream({ prompt, ... })` to get a stream of chunks (steps/UI messages).
- 4. **HTTP Response Creation:** Wraps the output stream as a readable HTTP `Response` object that streams UI message chunks to the client.

## Notes

- Your agent **must** implement `.stream({ prompt, ... })` and define a `tools` property (even if it's just `{}`) to work with this function.
- **Server Only:** This API should only be called in backend/server-side contexts (API routes, edge/serverless/server route handlers, etc.). Not for browser use.
- Additional options (`headers`, `status`, UI stream options, transforms, etc.) are available for advanced scenarios.
- This leverages [ReadableStream](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) so your platform/client must support HTTP streaming consumption.

## See Also

- [`Agent`](/v6/docs/reference/ai-sdk-core/agent)
- [`ToolLoopAgent`](/v6/docs/reference/ai-sdk-core/tool-loop-agent)
- [`UIMessage`](/v6/docs/reference/ai-sdk-core/ui-message)
- [`createAgentUIStream`](/v6/docs/reference/ai-sdk-core/create-agent-ui-stream)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)