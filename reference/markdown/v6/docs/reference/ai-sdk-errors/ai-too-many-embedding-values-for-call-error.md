---
title: AI_TooManyEmbeddingValuesForCallError
description: Learn how to fix AI_TooManyEmbeddingValuesForCallError
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when too many values are provided in a single embedding call.

## Properties

- `provider`: The AI provider name
- `modelId`: The ID of the embedding model
- `maxEmbeddingsPerCall`: The maximum number of embeddings allowed per call
- `values`: The array of values that was provided

## Checking for this Error

You can check if an error is an instance of `AI_TooManyEmbeddingValuesForCallError` using:

```typescript
import { TooManyEmbeddingValuesForCallError } from 'ai';

if (TooManyEmbeddingValuesForCallError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)