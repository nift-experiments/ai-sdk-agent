---
title: AI_InvalidDataContentError
description: How to fix AI_InvalidDataContentError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-invalid-data-content-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when the data content provided in a multi-modal message part is invalid. Check out the [ prompt examples for multi-modal messages ](/v5/docs/foundations/prompts#message-prompts).

## Properties

- `content`: The invalid content value
- `message`: The error message describing the expected and received content types

## Checking for this Error

You can check if an error is an instance of `AI_InvalidDataContentError` using:

```typescript
import { InvalidDataContentError } from 'ai';

if (InvalidDataContentError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)