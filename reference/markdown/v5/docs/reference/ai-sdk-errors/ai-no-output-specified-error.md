---
title: AI_NoOutputSpecifiedError
description: Learn how to fix AI_NoOutputSpecifiedError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-no-output-specified-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when no output format was specified for the AI response, and output-related methods are called.

## Properties

- `message`: The error message (defaults to 'No output specified.')

## Checking for this Error

You can check if an error is an instance of `AI_NoOutputSpecifiedError` using:

```typescript
import { NoOutputSpecifiedError } from 'ai';

if (NoOutputSpecifiedError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)