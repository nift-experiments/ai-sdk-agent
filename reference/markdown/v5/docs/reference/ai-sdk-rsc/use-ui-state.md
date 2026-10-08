---
title: useUIState
description: Reference for the useUIState function from the AI SDK RSC
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-rsc/use-ui-state"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

AI SDK RSC is currently experimental. We recommend using [AI SDK
UI](/v5/docs/ai-sdk-ui/overview) for production. For guidance on migrating from
RSC to UI, see our [migration guide](/v5/docs/ai-sdk-rsc/migrating-to-ui).

It is a hook that enables you to read and update the UI State. The state is client-side and can contain functions, React nodes, and other data. UIState is the visual representation of the AI state.

## Import

```
import { useUIState } from "@ai-sdk/rsc"
```

## API Signature

### Returns

Similar to useState, it is an array, where the first element is the current UI state and the second element is the function that updates the state.

## Examples

- [Learn to manage AI and UI states in Next.js](/examples/next-app/state-management/ai-ui-states)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)