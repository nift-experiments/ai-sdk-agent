---
title: Intercepting Fetch Requests
description: Learn how to intercept fetch requests using the AI SDK and Node
url: "https://ai-sdk.dev/v6/cookbook/node/intercept-fetch-requests"
docs_index: /llms.txt
tags:
  - node
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Many providers support setting a custom `fetch` function using the `fetch` argument in their factory function.

A custom `fetch` function can be used to intercept and modify requests before they are sent to the provider's API,
and to intercept and modify responses before they are returned to the caller.

Use cases for intercepting requests include:

- Logging requests and responses
- Adding authentication headers
- Modifying request bodies
- Caching responses
- Using a custom HTTP client

## Example

```ts title='index.ts' {5-13}
import { generateText, createGateway } from 'ai';

const gateway = createGateway({
  // example fetch wrapper that logs the input to the API call:
  fetch: async (url, options) => {
    console.log('URL', url);
    console.log('Headers', JSON.stringify(options!.headers, null, 2));
    console.log(
      `Body ${JSON.stringify(JSON.parse(options!.body! as string), null, 2)}`,
    );
    return await fetch(url, options);
  },
});

const { text } = await generateText({
  model: gateway('openai/gpt-4o'),
  prompt: 'Why is the sky blue?',
});
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)