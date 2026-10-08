---
title: createStreamableUI
description: Reference for the createStreamableUI function from the AI SDK RSC
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-rsc/create-streamable-ui"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

AI SDK RSC is currently experimental. We recommend using [AI SDK
UI](/v6/docs/ai-sdk-ui/overview) for production. For guidance on migrating from
RSC to UI, see our [migration guide](/v6/docs/ai-sdk-rsc/migrating-to-ui).

Create a stream that sends UI from the server to the client. On the client side, it can be rendered as a normal React node.

## Import

```
import { createStreamableUI } from "@ai-sdk/rsc"
```

## API Signature

### Parameters

- `initialValue?` (`ReactNode`): The initial value of the streamable UI.

### Returns

- `value` (`ReactNode`): The value of the streamable UI. This can be returned from a Server Action and received by the client.

### Methods

- `update` (`(ReactNode) => void`): Updates the current UI node. It takes a new UI node and replaces the old one.
- `append` (`(ReactNode) => void`): Appends a new UI node to the end of the old one. Once appended a new UI node, the previous UI node cannot be updated anymore.
- `done` (`(ReactNode | null) => void`): Marks the UI node as finalized and closes the stream. Once called, the UI node cannot be updated or appended anymore. This method is always required to be called, otherwise the response will be stuck in a loading state.
- `error` (`(Error) => void`): Signals that there is an error in the UI stream. It will be thrown on the client side and caught by the nearest error boundary component.

## Examples

- [Render a React component during a tool call](/examples/next-app/tools/render-interface-during-tool-call)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)