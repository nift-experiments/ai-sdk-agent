---
title: AI_NoSuchToolError
description: Learn how to fix AI_NoSuchToolError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-no-such-tool-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when a model tries to call an unavailable tool.

## Properties

- `toolName`: The name of the tool that was not found
- `availableTools`: Array of available tool names
- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_NoSuchToolError` using:

```typescript
import { NoSuchToolError } from 'ai';

if (NoSuchToolError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)