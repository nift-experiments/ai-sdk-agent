---
title: Embed Text
description: Learn how to embed text using the AI SDK and Node
url: "https://ai-sdk.dev/v6/cookbook/node/embed-text"
docs_index: /llms.txt
tags:
  - node
  - embedding
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Text embeddings are numerical representations of text that capture semantic meaning, allowing machines to understand and process language in a mathematical way. These vector representations are crucial for many AI applications, as they enable tasks like semantic search, document similarity comparison, and content recommendation.

This example demonstrates how to convert text into embeddings using a text embedding model. The resulting embedding is a high-dimensional vector that represents the semantic meaning of the input text. For a more practical application of embeddings, check out our [RAG example](/v6/cookbook/node/retrieval-augmented-generation) which shows how embeddings can be used for document retrieval.

```ts
import { embed } from 'ai';
import 'dotenv/config';

async function main() {
  const { embedding, usage } = await embed({
    model: 'openai/text-embedding-3-small',
    value: 'sunny day at the beach',
  });

  console.log(embedding);
  console.log(usage);
}

main().catch(console.error);
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)