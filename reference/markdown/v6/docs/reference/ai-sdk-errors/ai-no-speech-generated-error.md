---
title: AI_NoSpeechGeneratedError
description: Learn how to fix AI_NoSpeechGeneratedError
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-errors/ai-no-speech-generated-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when no audio could be generated from the input.

## Properties

- `responses`: Array of speech model response metadata (required in constructor)

## Checking for this Error

You can check if an error is an instance of `AI_NoSpeechGeneratedError` using:

```typescript
import { NoSpeechGeneratedError } from 'ai';

if (NoSpeechGeneratedError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)