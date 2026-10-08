---
title: LangChain
description: Learn how to use LangChain with the AI SDK.
url: "https://ai-sdk.dev/v5/providers/adapters/langchain"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

[LangChain](https://js.langchain.com/docs/) is a framework for developing applications powered by language models.
It provides tools and abstractions for working with AI models, agents, vector stores, and other data sources for retrieval augmented generation (RAG).
However, LangChain does not provide a way to easily build UIs or a standard way to stream data to the client.

## Example: Completion

Here is a basic example that uses both the AI SDK and LangChain together with the [Next.js](https://nextjs.org/docs) App Router.

The [`@ai-sdk/langchain` package](/v5/docs/reference/stream-helpers/langchain-adapter) uses the result from [LangChain ExpressionLanguage streaming](https://js.langchain.com/docs/how_to/streaming) to pipe text to the client.
`toDataStreamResponse()` is compatible with the LangChain Expression Language `.stream()` function response.

```tsx title="app/api/completion/route.ts" {16}
import { toUIMessageStream } from '@ai-sdk/langchain';
import { ChatOpenAI } from '@langchain/openai';
import { createUIMessageStreamResponse } from 'ai';

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

export async function POST(req: Request) {
  const { prompt } = await req.json();

  const model = new ChatOpenAI({
    model: 'gpt-3.5-turbo-0125',
    temperature: 0,
  });

  const stream = await model.stream(prompt);

  return createUIMessageStreamResponse({
    stream: toUIMessageStream(stream),
  });
}
```

Then, we use the AI SDK's [`useCompletion`](/v5/docs/ai-sdk-ui/completion) method in the page component to handle the completion:

```tsx title="app/page.tsx"
'use client';

import { useCompletion } from '@ai-sdk/react';

export default function Chat() {
  const { completion, input, handleInputChange, handleSubmit } =
    useCompletion();

  return (
    <div>
      {completion}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
      </form>
    </div>
  );
}
```

## More Examples

You can find additional examples in the AI SDK [examples/next-langchain](https://github.com/vercel/ai/tree/main/examples/next-langchain) folder.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)