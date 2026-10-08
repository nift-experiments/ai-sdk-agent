---
title: AI_InvalidPromptError
description: Learn how to fix AI_InvalidPromptError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-invalid-prompt-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when the prompt provided is invalid.

## Properties

- `prompt`: The invalid prompt value
- `message`: The error message
- `cause`: The cause of the error

## Checking for this Error

You can check if an error is an instance of `AI_InvalidPromptError` using:

```typescript
import { InvalidPromptError } from 'ai';

if (InvalidPromptError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)