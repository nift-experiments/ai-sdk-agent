---
title: AI_InvalidToolApprovalError
description: Learn how to fix AI_InvalidToolApprovalError
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-error"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

This error occurs when a tool approval response references an unknown `approvalId`. No matching `tool-approval-request` was found in the message history.

## Properties

- `approvalId`: The approval ID that was not found

## Checking for this Error

You can check if an error is an instance of `AI_InvalidToolApprovalError` using:

```typescript
import { InvalidToolApprovalError } from 'ai';

if (InvalidToolApprovalError.isInstance(error)) {
  // Handle the error
}
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)