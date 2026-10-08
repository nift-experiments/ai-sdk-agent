---
title: AI_InvalidMessageRoleError
description: Learn how to fix AI_InvalidMessageRoleError
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-errors/ai-invalid-message-role-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when an invalid message role is provided.

## Properties

- `role`: The invalid role value
- `message`: The error message (optional, auto-generated from `role`)

## Checking for this Error

You can check if an error is an instance of `AI_InvalidMessageRoleError` using:

```typescript
import { InvalidMessageRoleError } from 'ai';

if (InvalidMessageRoleError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)