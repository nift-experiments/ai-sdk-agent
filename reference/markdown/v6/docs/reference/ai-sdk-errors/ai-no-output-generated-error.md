---
title: AI_NoOutputGeneratedError
description: Learn how to fix AI_NoOutputGeneratedError
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-errors/ai-no-output-generated-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error is thrown when no LLM output was generated, e.g. because of errors.

For `generateText`, accessing `result.output` throws this error when the result
does not contain an output. This can happen when the final step does not finish
with a `stop` reason, for example when it finishes with `tool-calls`. The
`output` property is a getter, so destructuring it also triggers this access.

## Properties

- `message`: The error message (optional, defaults to `'No output generated.'`)
- `cause`: The underlying error that caused no output to be generated (optional)

## Checking for this Error

You can check if an error is an instance of `AI_NoOutputGeneratedError` using:

```typescript
import { NoOutputGeneratedError } from 'ai';

if (NoOutputGeneratedError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)