---
title: customProvider
description: Custom provider that uses models from a different provider (API Reference)
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/custom-provider"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

With a custom provider, you can map ids to any model.
This allows you to set up custom model configurations, alias names, and more.
The custom provider also supports a fallback provider, which is useful for
wrapping existing providers and adding additional functionality.

### Example: custom model settings

You can create a custom provider using `customProvider`.

```ts
import { openai } from '@ai-sdk/openai';
import { customProvider } from 'ai';

// custom provider with different model settings:
export const myOpenAI = customProvider({
  languageModels: {
    // replacement model with custom settings:
    'gpt-5': wrapLanguageModel({
      model: openai('gpt-5'),
      middleware: defaultSettingsMiddleware({
        settings: {
          providerOptions: {
            openai: {
              reasoningEffort: 'high',
            },
          },
        },
      }),
    }),
    // alias model with custom settings:
    'gpt-4o-reasoning-high': wrapLanguageModel({
      model: openai('gpt-4o'),
      middleware: defaultSettingsMiddleware({
        settings: {
          providerOptions: {
            openai: {
              reasoningEffort: 'high',
            },
          },
        },
      }),
    }),
  },
  fallbackProvider: openai,
});
```

## Import

```
import {  customProvider } from "ai"
```

## API Signature

### Parameters

- `languageModels?` (`Record<string, LanguageModel>`): A record of language models, where keys are model IDs and values are LanguageModel instances.
- `.embeddingModels?` (`Record<string, EmbeddingModel<string>>`): A record of text embedding models, where keys are model IDs and values are EmbeddingModel\<string> instances.
- `imageModels?` (`Record<string, ImageModel>`): A record of image models, where keys are model IDs and values are image model instances.
- `transcriptionModels?` (`Record<string, TranscriptionModel>`): A record of transcription models, where keys are model IDs and values are TranscriptionModel instances.
- `speechModels?` (`Record<string, SpeechModel>`): A record of speech models, where keys are model IDs and values are SpeechModel instances.
- `rerankingModels?` (`Record<string, RerankingModel>`): A record of reranking models, where keys are model IDs and values are RerankingModel instances.
- `fallbackProvider?` (`Provider`): An optional fallback provider to use when a requested model is not found in the custom provider.

### Returns

The `customProvider` function returns a `Provider` instance. It has the following methods:

- `languageModel` (`(id: string) => LanguageModel`): A function that returns a language model by its id (format: providerId:modelId)
- `embeddingModel` (`(id: string) => EmbeddingModel<string>`): A function that returns a text embedding model by its id (format: providerId:modelId)
- `imageModel` (`(id: string) => ImageModel`): A function that returns an image model by its id (format: providerId:modelId)
- `transcriptionModel` (`(id: string) => TranscriptionModel`): A function that returns a transcription model by its id.
- `speechModel` (`(id: string) => SpeechModel`): A function that returns a speech model by its id.
- `rerankingModel` (`(id: string) => RerankingModel`): A function that returns a reranking model by its id.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)