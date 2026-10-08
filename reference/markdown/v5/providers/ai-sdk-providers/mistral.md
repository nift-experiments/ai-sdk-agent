---
title: Mistral AI
description: Learn how to use Mistral.
url: "https://ai-sdk.dev/v5/providers/ai-sdk-providers/mistral"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The [Mistral AI](https://mistral.ai/) provider contains language model,
embedding model, and speech model support for Mistral APIs.

## Setup

The Mistral provider is available in the `@ai-sdk/mistral` module. You can install it with

#### pnpm

```
pnpm add @ai-sdk/mistral
```

#### npm

```
npm install @ai-sdk/mistral
```

#### yarn

```
yarn add @ai-sdk/mistral
```

#### bun

```
bun add @ai-sdk/mistral
```

## Provider Instance

You can import the default provider instance `mistral` from `@ai-sdk/mistral`:

```ts
import { mistral } from '@ai-sdk/mistral';
```

If you need a customized setup, you can import `createMistral` from `@ai-sdk/mistral`
and create a provider instance with your settings:

```ts
import { createMistral } from '@ai-sdk/mistral';

const mistral = createMistral({
  // custom settings
});
```

You can use the following optional settings to customize the Mistral provider instance:

- **baseURL** *string*

  Use a different URL prefix for API calls, e.g. to use proxy servers.
  The default prefix is `https://api.mistral.ai/v1`.

- **apiKey** *string*

  API key that is being sent using the `Authorization` header.
  It defaults to the `MISTRAL_API_KEY` environment variable.

- **headers** *Record\<string,string>*

  Custom headers to include in the requests.

- **fetch** *(input: RequestInfo, init?: RequestInit) => Promise\<Response>*

  Custom [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch) implementation.
  Defaults to the global `fetch` function.
  You can use it as a middleware to intercept requests,
  or to provide a custom fetch implementation for e.g. testing.

## Language Models

You can create models that call the [Mistral chat API](https://docs.mistral.ai/api/#operation/createChatCompletion) using a provider instance.
The first argument is the model id, e.g. `mistral-large-latest`.
Some Mistral chat models support tool calls.

```ts
const model = mistral('mistral-large-latest');
```

Mistral chat models also support additional model settings that are not part of the [standard call settings](/v5/docs/ai-sdk-core/settings).
You can pass them as an options argument and utilize `MistralLanguageModelOptions` for typing:

```ts
import { mistral, type MistralLanguageModelOptions } from '@ai-sdk/mistral';
const model = mistral('mistral-large-latest');

await generateText({
  model,
  providerOptions: {
    mistral: {
      safePrompt: true, // optional safety prompt injection
      parallelToolCalls: false, // disable parallel tool calls (one tool per response)
    } satisfies MistralLanguageModelOptions,
  },
});
```

The following optional provider options are available for Mistral models:

- **safePrompt** *boolean*

  Whether to inject a safety prompt before all conversations.

  Defaults to `false`.

- **documentImageLimit** *number*

  Maximum number of images to process in a document.

- **documentPageLimit** *number*

  Maximum number of pages to process in a document.

- **strictJsonSchema** *boolean*

  Whether to use strict JSON schema validation for structured outputs. Only applies when a schema is provided and only sets the [`strict` flag](https://docs.mistral.ai/api/#tag/chat/operation/chat_completion_v1_chat_completions_post) in addition to using [Custom Structured Outputs](https://docs.mistral.ai/capabilities/structured-output/custom_structured_output/), which is used by default if a schema is provided.

  Defaults to `false`.

- **structuredOutputs** *boolean*

  Whether to use [structured outputs](#structured-outputs). When enabled, tool calls and object generation will be strict and follow the provided schema.

  Defaults to `true`.

- **parallelToolCalls** *boolean*

  Whether to enable parallel function calling during tool use. When set to false, the model will use at most one tool per response.

  Defaults to `true`.

### Document OCR

Mistral chat models support document OCR for PDF files.
You can optionally set image and page limits using the provider options.

```ts
const result = await generateText({
  model: mistral('mistral-small-latest'),
  messages: [
    {
      role: 'user',
      content: [
        {
          type: 'text',
          text: 'What is an embedding model according to this document?',
        },
        {
          type: 'file',
          data: new URL(
            'https://github.com/vercel/ai/blob/main/examples/ai-core/data/ai.pdf?raw=true',
          ),
          mediaType: 'application/pdf',
        },
      ],
    },
  ],
  // optional settings:
  providerOptions: {
    mistral: {
      documentImageLimit: 8,
      documentPageLimit: 64,
    },
  },
});
```

### Reasoning Models

Mistral offers reasoning models that provide step-by-step thinking capabilities:

- **magistral-small-2506**: Smaller reasoning model for efficient step-by-step thinking
- **magistral-medium-2506**: More powerful reasoning model balancing performance and cost

These models return content that includes `<think>...</think>` tags containing the reasoning process. To properly extract and separate the reasoning from the final answer, use the [extract reasoning middleware](/v5/docs/reference/ai-sdk-core/extract-reasoning-middleware):

```ts
import { mistral } from '@ai-sdk/mistral';
import {
  extractReasoningMiddleware,
  generateText,
  wrapLanguageModel,
} from 'ai';

const result = await generateText({
  model: wrapLanguageModel({
    model: mistral('magistral-small-2506'),
    middleware: extractReasoningMiddleware({
      tagName: 'think',
    }),
  }),
  prompt: 'What is 15 * 24?',
});

console.log('REASONING:', result.reasoningText);
// Output: "Let me calculate this step by step..."

console.log('ANSWER:', result.text);
// Output: "360"
```

The middleware automatically parses the `<think>` tags and provides separate `reasoningText` and `text` properties in the result.

### Example

You can use Mistral language models to generate text with the `generateText` function:

```ts
import { mistral } from '@ai-sdk/mistral';
import { generateText } from 'ai';

const { text } = await generateText({
  model: mistral('mistral-large-latest'),
  prompt: 'Write a vegetarian lasagna recipe for 4 people.',
});
```

Mistral language models can also be used in the `streamText`, `generateObject`, and `streamObject` functions
(see [AI SDK Core](/v5/docs/ai-sdk-core)).

#### Structured Outputs

Mistral chat models support structured outputs using JSON Schema. You can use `generateObject` or `streamObject`
with Zod, Valibot, or raw JSON Schema. The SDK sends your schema via Mistral's `response_format: { type: 'json_schema' }`.

```ts
import { mistral } from '@ai-sdk/mistral';
import { generateObject } from 'ai';
import { z } from 'zod';

const result = await generateObject({
  model: mistral('mistral-large-latest'),
  schema: z.object({
    recipe: z.object({
      name: z.string(),
      ingredients: z.array(z.string()),
      instructions: z.array(z.string()),
    }),
  }),
  prompt: 'Generate a simple pasta recipe.',
});

console.log(JSON.stringify(result.object, null, 2));
```

You can enable strict JSON Schema validation using a provider option:

```ts {7-11}
import { mistral } from '@ai-sdk/mistral';
import { generateObject } from 'ai';
import { z } from 'zod';

const result = await generateObject({
  model: mistral('mistral-large-latest'),
  providerOptions: {
    mistral: {
      strictJsonSchema: true, // reject outputs that don't strictly match the schema
    },
  },
  schema: z.object({
    title: z.string(),
    items: z.array(z.object({ id: z.string(), qty: z.number().int().min(1) })),
  }),
  prompt: 'Generate a small shopping list.',
});
```

When using structured outputs, the SDK no longer injects an extra "answer with
JSON" instruction. It relies on Mistral's native `json_schema`/`json_object`
response formats instead. You can customize the schema name/description via
the standard structured-output APIs.

### Model Capabilities

| Model                   | Image Input | Object Generation | Tool Usage | Tool Streaming |
| ----------------------- | ----------- | ----------------- | ---------- | -------------- |
| `pixtral-large-latest`  | ✓           | ✓                 | ✓          | ✓              |
| `mistral-large-latest`  | ✗           | ✓                 | ✓          | ✓              |
| `mistral-medium-latest` | ✗           | ✓                 | ✓          | ✓              |
| `mistral-medium-2505`   | ✗           | ✓                 | ✓          | ✓              |
| `mistral-small-latest`  | ✗           | ✓                 | ✓          | ✓              |
| `magistral-small-2506`  | ✗           | ✓                 | ✓          | ✓              |
| `magistral-medium-2506` | ✗           | ✓                 | ✓          | ✓              |
| `ministral-3b-latest`   | ✗           | ✓                 | ✓          | ✓              |
| `ministral-8b-latest`   | ✗           | ✓                 | ✓          | ✓              |
| `pixtral-12b-2409`      | ✓           | ✓                 | ✓          | ✓              |
| `open-mistral-7b`       | ✗           | ✓                 | ✓          | ✓              |
| `open-mixtral-8x7b`     | ✗           | ✓                 | ✓          | ✓              |
| `open-mixtral-8x22b`    | ✗           | ✓                 | ✓          | ✓              |

The table above lists popular models. Please see the [Mistral
docs](https://docs.mistral.ai/getting-started/models/models_overview/) for a
full list of available models. The table above lists popular models. You can
also pass any available provider model ID as a string if needed.

## Speech Models

You can create models that call the
[Mistral speech API](https://docs.mistral.ai/api/endpoint/audio/speech) using
the `.speech()` factory method:

```ts
const model = mistral.speech('voxtral-mini-tts-2603');
```

Use a preset or saved voice ID with [`generateSpeech`](/v5/docs/reference/ai-sdk-core/generate-speech):

```ts
import { mistral } from '@ai-sdk/mistral';
import { generateSpeech } from 'ai';

const result = await generateSpeech({
  model: mistral.speech('voxtral-mini-tts-2603'),
  text: 'Hello from the AI SDK!',
  voice: 'en_paul_neutral',
  outputFormat: 'mp3',
});

const audio = result.audio.uint8Array;
```

The Mistral speech model maps `voice` to Mistral's `voice_id`. It supports
`mp3`, `wav`, `pcm`, `flac`, and `opus` output formats and defaults to `mp3`.
The `instructions`, `speed`, and `language` settings are not supported and
produce warnings when provided.

Mistral also supports one-off voice cloning with base64-encoded reference
audio. Pass it through `providerOptions.mistral.refAudio` and use
`MistralSpeechModelOptions` for type checking:

```ts {9-13}
import { readFile } from 'node:fs/promises';
import { mistral, type MistralSpeechModelOptions } from '@ai-sdk/mistral';
import { generateSpeech } from 'ai';

const referenceAudio = await readFile('./reference.mp3');

const result = await generateSpeech({
  model: mistral.speech('voxtral-mini-tts-2603'),
  text: 'Hello from the AI SDK!',
  providerOptions: {
    mistral: {
      refAudio: referenceAudio.toString('base64'),
    } satisfies MistralSpeechModelOptions,
  },
});
```

When `refAudio` is provided, it takes precedence over `voice`. Reference audio
is redacted from request metadata and API call errors returned by the provider.

Only use reference audio with the speaker's explicit consent. Follow Mistral's
voice cloning usage policy and disclose AI-generated audio when required. This
provider integration supports non-streaming speech generation; Mistral's
streaming speech API is not exposed through `SpeechModelV2`.

### Model Capabilities

| Model                   | Saved Voices | Reference Audio | Non-Streaming |
| ----------------------- | ------------ | --------------- | ------------- |
| `voxtral-mini-tts-2603` | ✓            | ✓               | ✓             |

## Embedding Models

You can create models that call the [Mistral embeddings API](https://docs.mistral.ai/api/#operation/createEmbedding)
using the `.textEmbedding()` factory method.

```ts
const model = mistral.textEmbedding('mistral-embed');
```

You can use Mistral embedding models to generate embeddings with the `embed` function:

```ts
import { mistral } from '@ai-sdk/mistral';
import { embed } from 'ai';

const { embedding } = await embed({
  model: mistral.textEmbedding('mistral-embed'),
  value: 'sunny day at the beach',
});
```

### Model Capabilities

| Model           | Default Dimensions |
| --------------- | ------------------ |
| `mistral-embed` | 1024               |

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)