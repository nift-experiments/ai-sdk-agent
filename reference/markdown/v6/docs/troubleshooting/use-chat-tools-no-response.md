---
title: useChat No Response
description: Troubleshooting errors related to the Use Chat Failed to Parse Stream error.
url: "https://ai-sdk.dev/v6/docs/troubleshooting/use-chat-tools-no-response"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

I am using [`useChat`](/v6/docs/reference/ai-sdk-ui/use-chat).
When I log the incoming messages on the server, I can see the tool call and the tool result, but the model does not respond with anything.

## Solution

To resolve this issue, convert the incoming messages to the `ModelMessage` format using the [`convertToModelMessages`](/v6/docs/reference/ai-sdk-ui/convert-to-model-messages) function.

```tsx {9}
import { openai } from '@ai-sdk/openai';
import { convertToModelMessages, streamText } from 'ai';

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: "anthropic/claude-sonnet-5.5",
    messages: await convertToModelMessages(messages),
  });

  return result.toUIMessageStreamResponse();
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)