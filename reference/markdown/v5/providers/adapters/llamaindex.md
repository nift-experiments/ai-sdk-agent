---
title: LlamaIndex
description: Learn how to use LlamaIndex with the AI SDK.
url: "https://ai-sdk.dev/v5/providers/adapters/llamaindex"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

[LlamaIndex](https://ts.llamaindex.ai/) is a framework for building LLM-powered applications. LlamaIndex helps you ingest, structure, and access private or domain-specific data. LlamaIndex.TS offers the core features of LlamaIndex for Python for popular runtimes like Node.js (official support), Vercel Edge Functions (experimental), and Deno (experimental).

## Example: Completion

Here is a basic example that uses both AI SDK and LlamaIndex together with the [Next.js](https://nextjs.org/docs) App Router.

The AI SDK [`@ai-sdk/llamaindex` package](/v5/docs/reference/stream-helpers/llamaindex-adapter) uses the stream result from calling the `chat` method on a [LlamaIndex ChatEngine](https://ts.llamaindex.ai/modules/chat_engine) or the `query` method on a [LlamaIndex QueryEngine](https://ts.llamaindex.ai/modules/query_engines) to pipe text to the client.

```tsx title="app/api/completion/route.ts" {17}
import { OpenAI, SimpleChatEngine } from 'llamaindex';
import { toDataStreamResponse } from '@ai-sdk/llamaindex';

export const maxDuration = 60;

export async function POST(req: Request) {
  const { prompt } = await req.json();

  const llm = new OpenAI({ model: 'gpt-4o' });
  const chatEngine = new SimpleChatEngine({ llm });

  const stream = await chatEngine.chat({
    message: prompt,
    stream: true,
  });

  return toDataStreamResponse(stream);
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

[create-llama](https://github.com/run-llama/create-llama) is the easiest way to get started with LlamaIndex. It uses the AI SDK to connect to LlamaIndex in all its generated code.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)