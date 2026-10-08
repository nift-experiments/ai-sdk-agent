---
title: "TypeScript error \"Cannot find namespace 'JSX'\""
description: Troubleshooting errors related to TypeScript and JSX.
url: "https://ai-sdk.dev/v6/docs/troubleshooting/typescript-cannot-find-namespace-jsx"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

I am using the AI SDK in a project without React, e.g. an Hono server, and I get the following error:
`error TS2503: Cannot find namespace 'JSX'.`

## Background

The AI SDK has a dependency on `@types/react` which defines the `JSX` namespace.
It will be removed in the next major version of the AI SDK.

## Solution

You can install the `@types/react` package as a dependency to fix the error.

```bash
npm install @types/react
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)