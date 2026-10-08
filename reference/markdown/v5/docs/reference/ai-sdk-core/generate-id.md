---
title: generateId
description: Generate a unique identifier (API Reference)
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-core/generate-id"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Generates a unique identifier. You can optionally provide the length of the ID.

This is the same id generator used by the AI SDK.

```ts
import { generateId } from 'ai';

const id = generateId();
```

## Import

```
import { generateId } from "ai"
```

## API Signature

### Parameters

- `size` (`number`): The length of the generated ID. It defaults to 16. This parameter is deprecated and will be removed in the next major version.

### Returns

A string representing the generated ID.

## See also

- [`createIdGenerator()`](/v5/docs/reference/ai-sdk-core/create-id-generator)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)