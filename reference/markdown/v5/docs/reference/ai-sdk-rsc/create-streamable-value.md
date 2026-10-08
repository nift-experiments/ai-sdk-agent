---
title: createStreamableValue
description: Reference for the createStreamableValue function from the AI SDK RSC
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-rsc/create-streamable-value"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

AI SDK RSC is currently experimental. We recommend using [AI SDK
UI](/v5/docs/ai-sdk-ui/overview) for production. For guidance on migrating from
RSC to UI, see our [migration guide](/v5/docs/ai-sdk-rsc/migrating-to-ui).

Create a stream that sends values from the server to the client. The value can be any serializable data.

## Import

```
import { createStreamableValue } from "@ai-sdk/rsc"
```

## API Signature

### Parameters

- `value` (`any`): Any data that RSC supports. Example, JSON.

### Returns

- `value` (`streamable`): This creates a special value that can be returned from Actions to the client. It holds the data inside and can be updated via the update method.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)