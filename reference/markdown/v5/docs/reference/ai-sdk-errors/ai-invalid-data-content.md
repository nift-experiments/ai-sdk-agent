---
title: AI_InvalidDataContent
description: Learn how to fix AI_InvalidDataContent
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-invalid-data-content"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when invalid data content is provided.

## Properties

- `content`: The invalid content value
- `message`: The error message
- `cause`: The cause of the error

## Checking for this Error

You can check if an error is an instance of `AI_InvalidDataContent` using:

```typescript
import { InvalidDataContent } from 'ai';

if (InvalidDataContent.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)