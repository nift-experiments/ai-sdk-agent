---
title: Tool calling with generateObject and streamObject
description: Troubleshooting tool calling when combined with generateObject and streamObject
url: "https://ai-sdk.dev/v5/docs/troubleshooting/tool-calling-with-structured-outputs"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

You may want to combine tool calling with structured output generation. While `generateObject` and `streamObject` are designed specifically for structured outputs, they don't support tool calling.

## Background

To use tool calling with structured outputs, use `generateText` or `streamText` with the `experimental_output` option.

**Important**: When using `experimental_output` with tool calling, the structured output generation counts as an additional step in the execution flow.

## Solution

When using `experimental_output` with tool calling, adjust your `stopWhen` condition to account for the additional step required for structured output generation:

```tsx
const result = await generateText({
  model: "anthropic/claude-sonnet-5.5",
  experimental_output: Output.object({
    schema: z.object({
      summary: z.string(),
      sentiment: z.enum(['positive', 'neutral', 'negative']),
    }),
  }),
  tools: {
    analyze: tool({
      description: 'Analyze data',
      inputSchema: z.object({
        data: z.string(),
      }),
      execute: async ({ data }) => {
        return { result: 'analyzed' };
      }),
    },
  },
  // Add at least 1 to your intended step count to account for structured output
  stopWhen: stepCountIs(3), // Now accounts for: tool call + tool result + structured output
  prompt: 'Analyze the data and provide a summary',
});
```

For more information about using structured outputs with `generateText` and `streamText` see [Generating Structured Data](/v5/docs/ai-sdk-core/generating-structured-data#generating-structured-outputs).

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)