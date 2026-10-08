---
title: AI_JSONParseError
description: Learn how to fix AI_JSONParseError
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors/ai-json-parse-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when JSON fails to parse.

## Properties

- `text`: The text value that could not be parsed
- `message`: The error message including parse error details

## Checking for this Error

You can check if an error is an instance of `AI_JSONParseError` using:

```typescript
import { JSONParseError } from 'ai';

if (JSONParseError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)