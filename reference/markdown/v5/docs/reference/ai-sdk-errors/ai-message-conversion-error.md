---
title: AI_MessageConversionError
description: Learn how to fix AI_MessageConversionError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-message-conversion-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when message conversion fails.

## Properties

- `originalMessage`: The original message that failed conversion
- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_MessageConversionError` using:

```typescript
import { MessageConversionError } from 'ai';

if (MessageConversionError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)