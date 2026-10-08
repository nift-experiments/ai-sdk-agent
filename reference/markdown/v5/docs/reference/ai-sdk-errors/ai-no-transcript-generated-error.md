---
title: AI_NoTranscriptGeneratedError
description: Learn how to fix AI_NoTranscriptGeneratedError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-no-transcript-generated-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when no transcript could be generated from the input.

## Properties

- `responses`: Array of responses
- `message`: The error message

## Checking for this Error

AI SDK 5 does not export the `NoTranscriptGeneratedError` class. Use the base
`AISDKError` guard and check the error name:

```typescript
import { AISDKError } from 'ai';

if (
  AISDKError.isInstance(error) &&
  error.name === 'AI_NoTranscriptGeneratedError'
) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)