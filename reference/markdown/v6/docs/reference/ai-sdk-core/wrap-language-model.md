---
title: wrapLanguageModel
description: Function for wrapping a language model with middleware (API Reference)
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/wrap-language-model"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The `wrapLanguageModel` function provides a way to enhance the behavior of language models
by wrapping them with middleware.
See [Language Model Middleware](/v6/docs/ai-sdk-core/middleware) for more information on middleware.

```ts
import { wrapLanguageModel, gateway } from 'ai';

const wrappedLanguageModel = wrapLanguageModel({
  model: gateway('openai/gpt-4.1'),
  middleware: yourLanguageModelMiddleware,
});
```

## Import

```
import { wrapLanguageModel } from "ai"
```

## API Signature

### Parameters

- `model` (`LanguageModelV3`): The original LanguageModelV3 instance to be wrapped.
- `middleware` (`LanguageModelV3Middleware | LanguageModelV3Middleware[]`): The middleware to be applied to the language model. When multiple middlewares are provided, the first middleware will transform the input first, and the last middleware will be wrapped directly around the model.
- `modelId` (`string`): Optional custom model ID to override the original model's ID.
- `providerId` (`string`): Optional custom provider ID to override the original model's provider.

### Returns

A new `LanguageModelV3` instance with middleware applied.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)