---
title: Stream Object
description: Learn how to stream structured data using the AI SDK and Node
url: "https://ai-sdk.dev/v5/cookbook/node/stream-object"
docs_index: /llms.txt
tags:
  - node
  - streaming
  - structured data
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Object generation can sometimes take a long time to complete,
especially when you're generating a large schema.

In Generative UI use cases, it is useful to stream the object to the client in real-time
to render UIs as the object is being generated.
You can use the [`streamObject`](/v5/docs/reference/ai-sdk-core/stream-object) function to generate partial object streams.

```ts title='index.ts'
import { streamObject } from 'ai';
import { z } from 'zod';

const { partialObjectStream } = streamObject({
  model: 'openai/gpt-4.1',
  schema: z.object({
    recipe: z.object({
      name: z.string(),
      ingredients: z.array(z.string()),
      steps: z.array(z.string()),
    }),
  }),
  prompt: 'Generate a lasagna recipe.',
});

for await (const partialObject of partialObjectStream) {
  console.clear();
  console.log(partialObject);
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)