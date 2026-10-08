---
title: Open Responses
description: Learn how to use the Open Responses provider for the AI SDK.
url: "https://ai-sdk.dev/v6/providers/ai-sdk-providers/open-responses"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The [Open Responses](https://www.openresponses.org/) provider contains language model support for Open Responses compatible APIs.

## Setup

The Open Responses provider is available in the `@ai-sdk/open-responses` module. You can install it with

#### pnpm

```
pnpm add @ai-sdk/open-responses
```

#### npm

```
npm install @ai-sdk/open-responses
```

#### yarn

```
yarn add @ai-sdk/open-responses
```

#### bun

```
bun add @ai-sdk/open-responses
```

## Provider Instance

Create an Open Responses provider instance using `createOpenResponses`:

```ts
import { createOpenResponses } from '@ai-sdk/open-responses';

const openResponses = createOpenResponses({
  name: 'aProvider',
  url: 'http://localhost:1234/v1/responses',
});
```

The `name` and `url` options are required:

- **name** *string*

  Provider name. Used as the key for provider options and metadata.

- **url** *string*

  URL for the Open Responses API POST endpoint.

You can use the following optional settings to customize the Open Responses provider instance:

- **apiKey** *string*

  API key that is being sent using the `Authorization` header.

- **headers** *Record\<string,string>*

  Custom headers to include in the requests.

- **fetch** *(input: RequestInfo, init?: RequestInit) => Promise\<Response>*

  Custom [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch) implementation.
  Defaults to the global `fetch` function.

- **strictResponseInput** *boolean*

  Serializes assistant history using strict OpenAI Responses input schemas.
  Assistant messages without an item ID are sent as easy input messages, while
  messages with a genuine provider item ID are sent as complete output items.
  Defaults to `false`.

## Language Models

The Open Responses provider instance is a function that you can invoke to create a language model:

```ts
const model = openResponses('mistralai/ministral-3-14b-reasoning');
```

You can use Open Responses models with the `generateText` and `streamText` functions,
and they support structured data generation with [`Output`](/v6/docs/reference/ai-sdk-core/output)
(see [AI SDK Core](/v6/docs/ai-sdk-core)).

### Example

```ts
import { createOpenResponses } from '@ai-sdk/open-responses';
import { generateText } from 'ai';

const openResponses = createOpenResponses({
  name: 'aProvider',
  url: 'http://localhost:1234/v1/responses',
});

const { text } = await generateText({
  model: openResponses('mistralai/ministral-3-14b-reasoning'),
  prompt: 'Invent a new holiday and describe its traditions.',
});
```

## Notes

- Stop sequences, `topK`, and `seed` are not supported and are ignored with warnings.
- Image inputs are supported for user messages with `file` parts using image media types.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)