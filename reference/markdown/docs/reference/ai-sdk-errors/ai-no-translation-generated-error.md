---
title: AI_NoTranslationGeneratedError
description: Learn how to fix AI_NoTranslationGeneratedError
url: "https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-translation-generated-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when no translation could be generated from the input audio:
no `audio` part was emitted and the final output text is empty, or the stream
ended without a finish event.

## Properties

- `response`: Speech translation model response metadata (required in constructor)

## Checking for this Error

You can check if an error is an instance of `AI_NoTranslationGeneratedError` using:

```typescript
import { NoTranslationGeneratedError } from 'ai';

if (NoTranslationGeneratedError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)