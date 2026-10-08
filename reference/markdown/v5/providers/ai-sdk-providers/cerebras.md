---
title: Cerebras
description: "Learn how to use Cerebras's models with the AI SDK."
url: "https://ai-sdk.dev/v5/providers/ai-sdk-providers/cerebras"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The [Cerebras](https://cerebras.ai) provider offers access to powerful language models through the Cerebras API, including their high-speed inference capabilities powered by Wafer-Scale Engines and CS-3 systems.

API keys can be obtained from the [Cerebras Platform](https://cloud.cerebras.ai).

## Setup

The Cerebras provider is available via the `@ai-sdk/cerebras` module. You can install it with:

#### pnpm

```
pnpm add @ai-sdk/cerebras
```

#### npm

```
npm install @ai-sdk/cerebras
```

#### yarn

```
yarn add @ai-sdk/cerebras
```

#### bun

```
bun add @ai-sdk/cerebras
```

## Provider Instance

You can import the default provider instance `cerebras` from `@ai-sdk/cerebras`:

```ts
import { cerebras } from '@ai-sdk/cerebras';
```

For custom configuration, you can import `createCerebras` and create a provider instance with your settings:

```ts
import { createCerebras } from '@ai-sdk/cerebras';

const cerebras = createCerebras({
  apiKey: process.env.CEREBRAS_API_KEY ?? '',
});
```

You can use the following optional settings to customize the Cerebras provider instance:

- **baseURL** *string*

  Use a different URL prefix for API calls.
  The default prefix is `https://api.cerebras.ai/v1`.

- **apiKey** *string*

  API key that is being sent using the `Authorization` header. It defaults to
  the `CEREBRAS_API_KEY` environment variable.

- **headers** *Record\<string,string>*

  Custom headers to include in the requests.

- **fetch** *(input: RequestInfo, init?: RequestInit) => Promise\<Response>*

  Custom [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch) implementation.

## Language Models

You can create language models using a provider instance:

```ts
import { cerebras } from '@ai-sdk/cerebras';
import { generateText } from 'ai';

const { text } = await generateText({
  model: cerebras('llama3.1-8b'),
  prompt: 'Write a vegetarian lasagna recipe for 4 people.',
});
```

Cerebras language models can be used in the `streamText` function
(see [AI SDK Core](/v5/docs/ai-sdk-core)).

You can create Cerebras language models using a provider instance. The first argument is the model ID, e.g. `llama-3.3-70b`:

```ts
const model = cerebras('llama-3.3-70b');
```

You can also use the `.languageModel()` and `.chat()` methods:

```ts
const model = cerebras.languageModel('llama-3.3-70b');
const model = cerebras.chat('llama-3.3-70b');
```

## Model Capabilities

| Model                            | Image Input | Object Generation | Tool Usage | Tool Streaming |
| -------------------------------- | ----------- | ----------------- | ---------- | -------------- |
| `llama3.1-8b`                    | ✗           | ✓                 | ✓          | ✓              |
| `llama-3.3-70b`                  | ✗           | ✓                 | ✓          | ✓              |
| `gpt-oss-120b`                   | ✗           | ✓                 | ✓          | ✓              |
| `qwen-3-32b`                     | ✗           | ✓                 | ✓          | ✓              |
| `qwen-3-235b-a22b-instruct-2507` | ✗           | ✓                 | ✓          | ✓              |
| `qwen-3-235b-a22b-thinking-2507` | ✗           | ✓                 | ✓          | ✓              |
| `zai-glm-4.6`                    | ✗           | ✓                 | ✓          | ✓              |

Please see the [Cerebras
docs](https://inference-docs.cerebras.ai/introduction) for more details about
the available models. Note that context windows are temporarily limited to
8192 tokens in the Free Tier. You can also pass any available provider model
ID as a string if needed.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)