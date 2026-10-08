---
title: stepCountIs
description: API Reference for stepCountIs.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/step-count-is"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Creates a stop condition that stops when the number of steps reaches a specified count.

This function is used with `stopWhen` in `generateText` and `streamText` to control when a tool-calling loop should stop based on the number of steps executed.

```ts
import { generateText, stepCountIs } from 'ai';

const result = await generateText({
  model: "anthropic/claude-sonnet-5.5",
  tools: {
    // your tools
  },
  // Stop after 5 steps
  stopWhen: stepCountIs(5),
});
```

## Import

```
import { stepCountIs } from "ai"
```

## API Signature

### Parameters

- `count` (`number`): The maximum number of steps to execute before stopping the tool-calling loop.

### Returns

A `StopCondition` function that returns `true` when the step count reaches the specified number. The function can be used with the `stopWhen` parameter in `generateText` and `streamText`.

## Examples

### Basic Usage

Stop after 3 steps:

```ts
import { generateText, stepCountIs } from 'ai';

const result = await generateText({
  model: yourModel,
  tools: yourTools,
  stopWhen: stepCountIs(3),
});
```

### Combining with Other Conditions

You can combine multiple stop conditions in an array:

```ts
import { generateText, stepCountIs, hasToolCall } from 'ai';

const result = await generateText({
  model: yourModel,
  tools: yourTools,
  // Stop after 10 steps OR when finalAnswer tool is called
  stopWhen: [stepCountIs(10), hasToolCall('finalAnswer')],
});
```

## See also

- [`hasToolCall()`](/v6/docs/reference/ai-sdk-core/has-tool-call)
- [`generateText()`](/v6/docs/reference/ai-sdk-core/generate-text)
- [`streamText()`](/v6/docs/reference/ai-sdk-core/stream-text)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)