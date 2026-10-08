---
title: ToolLoopAgent
description: API Reference for the ToolLoopAgent class.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/tool-loop-agent"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Creates a reusable AI agent capable of generating text, streaming responses, and using tools over multiple steps (a reasoning-and-acting loop). `ToolLoopAgent` is ideal for building autonomous, multi-step agents that can take actions, call tools, and reason over the results until a stop condition is reached.

Unlike single-step calls like `generateText()`, an agent can iteratively invoke tools, collect tool results, and decide next actions until completion or user approval is required.

```ts
import { ToolLoopAgent } from 'ai';

const agent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: 'You are a helpful assistant.',
  tools: {
    weather: weatherTool,
    calculator: calculatorTool,
  },
});

const result = await agent.generate({
  prompt: 'What is the weather in NYC?',
});

console.log(result.text);
```

To see `ToolLoopAgent` in action, check out [these examples](#examples).

## Import

```
import { ToolLoopAgent } from "ai"
```

## Constructor

### Parameters

- `model` (`LanguageModel`): The language model instance to use (e.g., from a provider).
- `instructions?` (`string | SystemModelMessage | SystemModelMessage[]`): Instructions for the agent, usually used for system prompt/context.
- `allowSystemInMessages?` (`boolean`): Whether \`role: "system"\` messages are allowed in the \`prompt\` or \`messages\` fields. When unset, system messages are rejected because they can create a prompt injection attack risk. Ideally, use the \`instructions\` option instead. Set to \`true\` to allow system messages, or \`false\` to explicitly reject them.
- `tools?` (`Record<string, Tool>`): A set of tools the agent can call. Keys are tool names. Tools require the underlying model to support tool calling.
- `toolChoice?` (`ToolChoice`): Tool call selection strategy. Options: 'auto' | 'none' | 'required' | \{ type: 'tool', toolName: string }. Default: 'auto'.
- `stopWhen?` (`StopCondition | StopCondition[]`): Condition(s) for ending the agent loop. Default: stepCountIs(20).
- `activeTools?` (`Array<string>`): Limits the subset of tools that are available in a specific call.
- `output?` (`Output`): Optional structured output specification, for parsing responses into typesafe data.
- `prepareStep?` (`PrepareStepFunction`): Optional function to mutate step settings or inject state for each agent step, including per-step model call settings such as temperature, maxOutputTokens, sampling controls, penalties, stop sequences, and seed. Model call setting overrides apply only to the current step.
- `experimental_repairToolCall?` (`ToolCallRepairFunction`): Optional callback to attempt automatic recovery when a tool call cannot be parsed.
- `onStepFinish?` (`ToolLoopAgentOnStepFinishCallback`): Callback invoked after each agent step (LLM/tool call) completes. If also specified in \`generate()\` or \`stream()\`, both callbacks are called (constructor first).
- `onFinish?` (`ToolLoopAgentOnFinishCallback`): Callback that is called when all agent steps are finished and the response is complete. Receives step results, total usage, experimental\_context, functionId, and metadata. If also specified in \`generate()\` or \`stream()\`, both callbacks are called (constructor first).
- `experimental_context?` (`unknown`): Experimental: Custom context object passed to each tool call.
- `experimental_telemetry?` (`TelemetrySettings`): Experimental: Optional telemetry configuration.
- `experimental_download?` (`DownloadFunction | undefined`): Experimental: Custom download function for fetching files/URLs for tool or model use. By default, files are downloaded if the model does not support the URL for a given media type.
- `maxOutputTokens?` (`number`): Maximum number of tokens the model is allowed to generate.
- `temperature?` (`number`): Sampling temperature, controls randomness. Passed through to the model.
- `topP?` (`number`): Top-p (nucleus) sampling parameter. Passed through to the model.
- `topK?` (`number`): Top-k sampling parameter. Passed through to the model.
- `presencePenalty?` (`number`): Presence penalty parameter. Passed through to the model.
- `frequencyPenalty?` (`number`): Frequency penalty parameter. Passed through to the model.
- `stopSequences?` (`string[]`): Custom token sequences which stop the model output. Passed through to the model.
- `seed?` (`number`): Seed for deterministic generation (if supported).
- `maxRetries?` (`number`): How many times to retry on failure. Default: 2.
- `providerOptions?` (`ProviderOptions`): Additional provider-specific configuration.
- `headers?` (`Record<string, string | undefined>`): Additional HTTP headers to be sent with the request. Only applicable for HTTP-based providers.
- `callOptionsSchema?` (`FlexibleSchema<CALL_OPTIONS>`): Optional schema for custom call options that can be passed when calling generate() or stream().
- `prepareCall?` (`PrepareCallFunction`): Optional function to prepare call-specific settings based on the call options.
- `id?` (`string`): Custom agent identifier.

## Methods

### `generate()`

Generates a response and triggers tool calls as needed, running the agent loop and returning the final result. Returns a promise resolving to a `GenerateTextResult`.

```ts
const result = await agent.generate({
  prompt: 'What is the weather like?',
});
```

- `prompt` (`string | Array<ModelMessage>`): A text prompt or message array.
- `messages` (`Array<ModelMessage>`): A full conversation history as a list of model messages.
- `abortSignal?` (`AbortSignal`): An optional abort signal that can be used to cancel the call.
- `timeout?` (`number | { totalMs?: number; stepMs?: number; chunkMs?: number }`): Timeout in milliseconds. Can be specified as a number or as an object with totalMs, stepMs, and/or chunkMs properties. The call will be aborted if it takes longer than the specified timeout. Can be used alongside abortSignal.
- `options?` (`CALL_OPTIONS`): Custom call options when the agent is configured with a callOptionsSchema.
- `onStepFinish?` (`ToolLoopAgentOnStepFinishCallback`): Callback invoked after each agent step (LLM/tool call) completes. If also specified in the constructor, both callbacks are called (constructor first, then this one).

#### Returns

The `generate()` method returns a `GenerateTextResult` object (see [`generateText`](/v6/docs/reference/ai-sdk-core/generate-text#returns) for details).

### `stream()`

Streams a response from the agent, including agent reasoning and tool calls, as they occur. Returns a `StreamTextResult`.

```ts
const stream = agent.stream({
  prompt: 'Tell me a story about a robot.',
});

for await (const chunk of stream.textStream) {
  console.log(chunk);
}
```

- `prompt` (`string | Array<ModelMessage>`): A text prompt or message array.
- `messages` (`Array<ModelMessage>`): A full conversation history as a list of model messages.
- `abortSignal?` (`AbortSignal`): An optional abort signal that can be used to cancel the call.
- `timeout?` (`number | { totalMs?: number; stepMs?: number; chunkMs?: number }`): Timeout in milliseconds. Can be specified as a number or as an object with totalMs, stepMs, and/or chunkMs properties. The call will be aborted if it takes longer than the specified timeout. Can be used alongside abortSignal.
- `options?` (`CALL_OPTIONS`): Custom call options when the agent is configured with a callOptionsSchema.
- `experimental_transform?` (`StreamTextTransform | Array<StreamTextTransform>`): Optional stream transformation(s). They are applied in the order provided and must maintain the stream structure. See \`streamText\` docs for details.
- `onStepFinish?` (`ToolLoopAgentOnStepFinishCallback`): Callback invoked after each agent step (LLM/tool call) completes. If also specified in the constructor, both callbacks are called (constructor first, then this one).

#### Returns

The `stream()` method returns a `StreamTextResult` object (see [`streamText`](/v6/docs/reference/ai-sdk-core/stream-text#returns) for details).

## Types

### `InferAgentUIMessage`

Infers the UI message type for the given agent instance. Useful for type-safe UI and message exchanges.

#### Basic Example

```ts
import { ToolLoopAgent, InferAgentUIMessage } from 'ai';

const weatherAgent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  tools: { weather: weatherTool },
});

type WeatherAgentUIMessage = InferAgentUIMessage<typeof weatherAgent>;
```

#### Example with Message Metadata

You can provide a second type argument to customize the metadata for each message. This is useful for tracking rich metadata returned by the agent (such as createdAt, tokens, finish reason, etc.).

```ts
import { ToolLoopAgent, InferAgentUIMessage } from 'ai';
import { z } from 'zod';

// Example schema for message metadata
const exampleMetadataSchema = z.object({
  createdAt: z.number().optional(),
  model: z.string().optional(),
  totalTokens: z.number().optional(),
  finishReason: z.string().optional(),
});
type ExampleMetadata = z.infer<typeof exampleMetadataSchema>;

// Define agent as usual
const metadataAgent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  // ...other options
});

// Type-safe UI message type with custom metadata
type MetadataAgentUIMessage = InferAgentUIMessage<
  typeof metadataAgent,
  ExampleMetadata
>;
```

## Examples

### Basic Agent with Tools

```ts
import { ToolLoopAgent, stepCountIs } from 'ai';
import { weatherTool, calculatorTool } from './tools';

const assistant = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: 'You are a helpful assistant.',
  tools: {
    weather: weatherTool,
    calculator: calculatorTool,
  },
  stopWhen: stepCountIs(3),
});

const result = await assistant.generate({
  prompt: 'What is the weather in NYC and what is 100 * 25?',
});

console.log(result.text);
console.log(result.steps); // Array of all steps taken by the agent
```

### Streaming Agent Response

```ts
const agent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: 'You are a creative storyteller.',
});

const stream = agent.stream({
  prompt: 'Tell me a short story about a time traveler.',
});

for await (const chunk of stream.textStream) {
  process.stdout.write(chunk);
}
```

### Agent with Output Parsing

```ts
import { z } from 'zod';

const analysisAgent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  output: {
    schema: z.object({
      sentiment: z.enum(['positive', 'negative', 'neutral']),
      score: z.number(),
      summary: z.string(),
    }),
  },
});

const result = await analysisAgent.generate({
  prompt: 'Analyze this review: "The product exceeded my expectations!"',
});

console.log(result.output);
// Typed as { sentiment: 'positive' | 'negative' | 'neutral', score: number, summary: string }
```

### Example: Approved Tool Execution

```ts
import { openai } from '@ai-sdk/openai';
import { ToolLoopAgent } from 'ai';

const agent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: 'You are an agent with access to a weather API.',
  tools: {
    weather: openai.tools.weather({
      /* ... */
    }),
  },
  // Optionally require approval, etc.
});

const result = await agent.generate({
  prompt: 'Is it raining in Paris today?',
});
console.log(result.text);
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)