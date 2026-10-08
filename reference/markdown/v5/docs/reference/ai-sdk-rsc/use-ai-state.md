---
title: useAIState
description: Reference for the useAIState function from the AI SDK RSC
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-rsc/use-ai-state"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

AI SDK RSC is currently experimental. We recommend using [AI SDK
UI](/v5/docs/ai-sdk-ui/overview) for production. For guidance on migrating from
RSC to UI, see our [migration guide](/v5/docs/ai-sdk-rsc/migrating-to-ui).

It is a hook that enables you to read and update the AI state. The AI state is shared globally between all `useAIState` hooks under the same `<AI/>` provider.

The AI state is intended to contain context and information shared with the AI model, such as system messages, function responses, and other relevant data.

## Import

```
import { useAIState } from "@ai-sdk/rsc"
```

## API Signature

### Returns

A single element array where the first element is the current AI state.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)