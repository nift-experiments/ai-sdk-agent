---
title: AI_NoSuchProviderReferenceError
description: Learn how to fix AI_NoSuchProviderReferenceError
url: "https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-such-provider-reference-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when a provider reference cannot be resolved because the
specified provider is not found in the provider reference mapping.

## Properties

- `provider`: The provider that was not found
- `reference`: The full provider reference mapping that was searched
- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_NoSuchProviderReferenceError` using:

```typescript
import { NoSuchProviderReferenceError } from 'ai';

if (NoSuchProviderReferenceError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)