---
title: Event Callbacks
description: Subscribe to lifecycle events in generateText and streamText calls
url: "https://ai-sdk.dev/v6/docs/ai-sdk-core/event-listeners"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The AI SDK provides per-call event callbacks that you can pass to `generateText` and `streamText` to observe lifecycle events. This is useful for building observability tools, logging systems, analytics, and debugging utilities.

## Basic Usage

Pass callbacks directly to `generateText` or `streamText`:

```ts
import { generateText } from 'ai';

const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'What is the weather in San Francisco?',
  experimental_onStart: event => {
    console.log('Generation started:', event.model.modelId);
  },
  onFinish: event => {
    console.log('Generation finished:', event.totalUsage);
  },
});
```

## Available Callbacks

- `experimental_onStart` (`(event: OnStartEvent) => void | Promise<void>`): Called when generation begins, before any LLM calls.
- `experimental_onStepStart` (`(event: OnStepStartEvent) => void | Promise<void>`): Called when a step (LLM call) begins, before the provider is called.
- `experimental_onToolCallStart` (`(event: OnToolCallStartEvent) => void | Promise<void>`): Called when a tool's execute function is about to run.
- `experimental_onToolCallFinish` (`(event: OnToolCallFinishEvent) => void | Promise<void>`): Called when a tool's execute function completes or errors.
- `onStepFinish` (`(event: OnStepFinishEvent) => void | Promise<void>`): Called when a step (LLM call) completes.
- `onFinish` (`(event: OnFinishEvent) => void | Promise<void>`): Called when the entire generation completes (all steps finished).

## Event Reference

### `experimental_onStart`

Called when the generation operation begins, before any LLM calls are made.

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Hello!',
  experimental_onStart: event => {
    console.log('Model:', event.model.modelId);
    console.log('Temperature:', event.temperature);
  },
});
```

- `model` (`{ provider: string; modelId: string }`): The model being used for generation.
- `system` (`string | SystemModelMessage | Array<SystemModelMessage> | undefined`): The system message(s) provided to the model.
- `prompt` (`string | Array<ModelMessage> | undefined`): The prompt string or array of messages if using the prompt option.
- `messages` (`Array<ModelMessage> | undefined`): The messages array if using the messages option.
- `tools` (`ToolSet | undefined`): The tools available for this generation.
- `toolChoice` (`ToolChoice | undefined`): The tool choice strategy for this generation.
- `activeTools` (`Array<keyof TOOLS> | undefined`): Limits which tools are available for the model to call.
- `maxOutputTokens` (`number | undefined`): Maximum number of tokens to generate.
- `temperature` (`number | undefined`): Sampling temperature for generation.
- `topP` (`number | undefined`): Top-p (nucleus) sampling parameter.
- `topK` (`number | undefined`): Top-k sampling parameter.
- `presencePenalty` (`number | undefined`): Presence penalty for generation.
- `frequencyPenalty` (`number | undefined`): Frequency penalty for generation.
- `stopSequences` (`string[] | undefined`): Sequences that will stop generation.
- `seed` (`number | undefined`): Random seed for reproducible generation.
- `maxRetries` (`number`): Maximum number of retries for failed requests.
- `timeout` (`TimeoutConfiguration | undefined`): Timeout configuration for the generation.
- `headers` (`Record<string, string | undefined> | undefined`): Additional HTTP headers sent with the request.
- `providerOptions` (`ProviderOptions | undefined`): Additional provider-specific options.
- `stopWhen` (`StopCondition | Array<StopCondition> | undefined`): Condition(s) for stopping the generation.
- `output` (`Output | undefined`): The output specification for structured outputs.
- `abortSignal` (`AbortSignal | undefined`): Abort signal for cancelling the operation.
- `include` (`{ requestBody?: boolean; responseBody?: boolean } | undefined`): Settings for controlling what data is included in step results.
- `functionId` (`string | undefined`): Identifier from telemetry settings for grouping related operations.
- `metadata` (`Record<string, unknown> | undefined`): Additional metadata passed to the generation.
- `experimental_context` (`unknown`): User-defined context object that flows through the entire generation lifecycle.

### `experimental_onStepStart`

Called before each step (LLM call) begins. Useful for tracking multi-step generations.

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Hello!',
  experimental_onStepStart: event => {
    console.log('Step:', event.stepNumber);
    console.log('Messages:', event.messages.length);
  },
});
```

- `stepNumber` (`number`): Zero-based index of the current step.
- `model` (`{ provider: string; modelId: string }`): The model being used for this step.
- `system` (`string | SystemModelMessage | Array<SystemModelMessage> | undefined`): The system message for this step.
- `messages` (`Array<ModelMessage>`): The messages that will be sent to the model for this step.
- `tools` (`ToolSet | undefined`): The tools available for this generation.
- `toolChoice` (`LanguageModelV3ToolChoice | undefined`): The tool choice configuration for this step.
- `activeTools` (`Array<keyof TOOLS> | undefined`): Limits which tools are available for this step.
- `steps` (`ReadonlyArray<StepResult>`): Array of results from previous steps (empty for first step).
- `providerOptions` (`ProviderOptions | undefined`): Additional provider-specific options for this step.
- `timeout` (`TimeoutConfiguration | undefined`): Timeout configuration for the generation.
- `headers` (`Record<string, string | undefined> | undefined`): Additional HTTP headers sent with the request.
- `stopWhen` (`StopCondition | Array<StopCondition> | undefined`): Condition(s) for stopping the generation.
- `output` (`Output | undefined`): The output specification for structured outputs.
- `abortSignal` (`AbortSignal | undefined`): Abort signal for cancelling the operation.
- `include` (`{ requestBody?: boolean; responseBody?: boolean } | undefined`): Settings for controlling what data is included in step results.
- `functionId` (`string | undefined`): Identifier from telemetry settings for grouping related operations.
- `metadata` (`Record<string, unknown> | undefined`): Additional metadata from telemetry settings.
- `experimental_context` (`unknown`): User-defined context object. May be updated from prepareStep between steps.

### `experimental_onToolCallStart`

Called before a tool's `execute` function runs.

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'What is the weather?',
  tools: { getWeather },
  experimental_onToolCallStart: event => {
    console.log('Tool:', event.toolCall.toolName);
    console.log('Input:', event.toolCall.input);
  },
});
```

- `stepNumber` (`number | undefined`): Zero-based index of the current step where this tool call occurs.
- `model` (`{ provider: string; modelId: string } | undefined`): The model being used for this step.
- `toolCall` (`TypedToolCall`): The full tool call object.
  - `TypedToolCall`
    - `type` (`'tool-call'`): The type of the call.
    - `toolCallId` (`string`): Unique identifier for this tool call.
    - `toolName` (`string`): Name of the tool being called.
    - `input` (`unknown`): Input arguments passed to the tool.
- `messages` (`Array<ModelMessage>`): The conversation messages available at tool execution time.
- `abortSignal` (`AbortSignal | undefined`): Signal for cancelling the operation.
- `functionId` (`string | undefined`): Identifier from telemetry settings for grouping related operations.
- `metadata` (`Record<string, unknown> | undefined`): Additional metadata from telemetry settings.
- `experimental_context` (`unknown`): User-defined context object flowing through the generation.

### `experimental_onToolCallFinish`

Called after a tool's `execute` function completes or errors. Uses a discriminated union on the `success` field.

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'What is the weather?',
  tools: { getWeather },
  experimental_onToolCallFinish: event => {
    console.log('Tool:', event.toolCall.toolName);
    console.log('Duration:', event.durationMs, 'ms');

    if (event.success) {
      console.log('Output:', event.output);
    } else {
      console.error('Error:', event.error);
    }
  },
});
```

- `stepNumber` (`number | undefined`): Zero-based index of the current step where this tool call occurred.
- `model` (`{ provider: string; modelId: string } | undefined`): The model being used for this step.
- `toolCall` (`TypedToolCall`): The full tool call object.
  - `TypedToolCall`
    - `type` (`'tool-call'`): The type of the call.
    - `toolCallId` (`string`): Unique identifier for this tool call.
    - `toolName` (`string`): Name of the tool that was called.
    - `input` (`unknown`): Input arguments passed to the tool.
- `messages` (`Array<ModelMessage>`): The conversation messages available at tool execution time.
- `abortSignal` (`AbortSignal | undefined`): Signal for cancelling the operation.
- `durationMs` (`number`): Execution time of the tool call in milliseconds.
- `functionId` (`string | undefined`): Identifier from telemetry settings for grouping related operations.
- `metadata` (`Record<string, unknown> | undefined`): Additional metadata from telemetry settings.
- `experimental_context` (`unknown`): User-defined context object flowing through the generation.
- `success` (`boolean`): Discriminator indicating whether the tool call succeeded. When true, output is available. When false, error is available.
- `output` (`unknown`): The tool's return value (only present when success is true).
- `error` (`unknown`): The error that occurred during tool execution (only present when success is false).

### `onStepFinish`

Called after each step (LLM call) completes. Provides the full `StepResult`.

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Hello!',
  onStepFinish: event => {
    console.log('Step:', event.stepNumber);
    console.log('Finish reason:', event.finishReason);
    console.log('Tokens:', event.usage.totalTokens);
  },
});
```

- `stepNumber` (`number`): Zero-based index of this step.
- `model` (`{ provider: string; modelId: string }`): Information about the model that produced this step.
- `finishReason` (`'stop' | 'length' | 'content-filter' | 'tool-calls' | 'error' | 'other'`): The unified reason why the generation finished.
- `usage` (`LanguageModelUsage`): The token usage of the generated text.
  - `LanguageModelUsage`
    - `inputTokens` (`number | undefined`): The total number of input (prompt) tokens used.
    - `outputTokens` (`number | undefined`): The number of output (completion) tokens used.
    - `totalTokens` (`number | undefined`): The total number of tokens used.
- `text` (`string`): The generated text.
- `toolCalls` (`Array<TypedToolCall>`): The tool calls that were made during the generation.
- `toolResults` (`Array<TypedToolResult>`): The results of the tool calls.
- `content` (`Array<ContentPart>`): The content that was generated in this step.
- `reasoning` (`Array<ReasoningPart>`): The reasoning that was generated during the generation.
- `reasoningText` (`string | undefined`): The reasoning text that was generated.
- `files` (`Array<GeneratedFile>`): The files that were generated during the generation.
- `sources` (`Array<Source>`): The sources that were used to generate the text.
- `warnings` (`CallWarning[] | undefined`): Warnings from the model provider.
- `request` (`LanguageModelRequestMetadata`): Additional request information.
- `response` (`LanguageModelResponseMetadata`): Additional response information including id, modelId, timestamp, headers, and messages.
- `functionId` (`string | undefined`): Identifier from telemetry settings for grouping related operations.
- `metadata` (`Record<string, unknown> | undefined`): Additional metadata from telemetry settings.
- `experimental_context` (`unknown`): User-defined context object flowing through the generation.
- `providerMetadata` (`ProviderMetadata | undefined`): Additional provider-specific metadata.

### `onFinish`

Called when the entire generation completes (all steps finished). Includes aggregated data.

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Hello!',
  onFinish: event => {
    console.log('Total steps:', event.steps.length);
    console.log('Total tokens:', event.totalUsage.totalTokens);
    console.log('Final text:', event.text);
  },
});
```

- `steps` (`Array<StepResult>`): Array containing results from all steps in the generation.
- `totalUsage` (`LanguageModelUsage`): Aggregated token usage across all steps.
  - `LanguageModelUsage`
    - `inputTokens` (`number | undefined`): The total number of input tokens used across all steps.
    - `outputTokens` (`number | undefined`): The total number of output tokens used across all steps.
    - `totalTokens` (`number | undefined`): The total number of tokens used across all steps.
- `stepNumber` (`number`): Zero-based index of the final step.
- `model` (`{ provider: string; modelId: string }`): Information about the model that produced the final step.
- `finishReason` (`'stop' | 'length' | 'content-filter' | 'tool-calls' | 'error' | 'other'`): The unified reason why the generation finished.
- `usage` (`LanguageModelUsage`): The token usage from the final step only (not aggregated).
- `text` (`string`): The full text that has been generated.
- `toolCalls` (`Array<TypedToolCall>`): The tool calls that were made in the final step.
- `toolResults` (`Array<TypedToolResult>`): The results of the tool calls from the final step.
- `content` (`Array<ContentPart>`): The content that was generated in the final step.
- `reasoning` (`Array<ReasoningPart>`): The reasoning that was generated.
- `reasoningText` (`string | undefined`): The reasoning text that was generated.
- `files` (`Array<GeneratedFile>`): Files that were generated in the final step.
- `sources` (`Array<Source>`): Sources that have been used as input to generate the response.
- `warnings` (`CallWarning[] | undefined`): Warnings from the model provider.
- `request` (`LanguageModelRequestMetadata`): Additional request information from the final step.
- `response` (`LanguageModelResponseMetadata`): Additional response information from the final step.
- `functionId` (`string | undefined`): Identifier from telemetry settings for grouping related operations.
- `metadata` (`Record<string, unknown> | undefined`): Additional metadata from telemetry settings.
- `experimental_context` (`unknown`): The final state of the user-defined context object.
- `providerMetadata` (`ProviderMetadata | undefined`): Additional provider-specific metadata from the final step.

## Use Cases

### Logging and Debugging

```ts
import { generateText } from 'ai';

const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Hello!',
  experimental_onStart: event => {
    console.log(`[${new Date().toISOString()}] Generation started`, {
      model: event.model.modelId,
      provider: event.model.provider,
    });
  },
  onStepFinish: event => {
    console.log(
      `[${new Date().toISOString()}] Step ${event.stepNumber} finished`,
      {
        finishReason: event.finishReason,
        tokens: event.usage.totalTokens,
      },
    );
  },
  onFinish: event => {
    console.log(`[${new Date().toISOString()}] Generation complete`, {
      totalSteps: event.steps.length,
      totalTokens: event.totalUsage.totalTokens,
    });
  },
});
```

### Tool Execution Monitoring

```ts
import { generateText } from 'ai';

const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'What is the weather?',
  tools: { getWeather },
  experimental_onToolCallStart: event => {
    console.log(`Tool "${event.toolCall.toolName}" starting...`);
  },
  experimental_onToolCallFinish: event => {
    if (event.success) {
      console.log(
        `Tool "${event.toolCall.toolName}" completed in ${event.durationMs}ms`,
      );
    } else {
      console.error(`Tool "${event.toolCall.toolName}" failed:`, event.error);
    }
  },
});
```

## Error Handling

Errors thrown inside callbacks are caught and do not break the generation flow. This ensures that monitoring code cannot disrupt your application:

```ts
const result = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Hello!',
  experimental_onStart: () => {
    throw new Error('This error is caught internally');
    // Generation continues normally
  },
});
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)