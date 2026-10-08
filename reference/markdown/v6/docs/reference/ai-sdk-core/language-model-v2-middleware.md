---
title: LanguageModelV3Middleware
description: Middleware for enhancing language model behavior (API Reference)
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/language-model-v2-middleware"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Language model middleware is an experimental feature.

Language model middleware provides a way to enhance the behavior of language models
by intercepting and modifying the calls to the language model. It can be used to add
features like guardrails, RAG, caching, and logging in a language model agnostic way.

See [Language Model Middleware](/v6/docs/ai-sdk-core/middleware) for more information.

## Import

```
import { LanguageModelV3Middleware } from "ai"
```

## API Signature

- `specificationVersion` (`'v3'`): The specification version of the middleware. Must be "v3".
- `transformParams?` (`({ type: "generate" | "stream", params: LanguageModelV3CallOptions, model: LanguageModelV3 }) => PromiseLike<LanguageModelV3CallOptions>`): Transforms the parameters before they are passed to the language model.
- `wrapGenerate?` (`({ doGenerate: () => PromiseLike<LanguageModelV3GenerateResult>, doStream: () => PromiseLike<LanguageModelV3StreamResult>, params: LanguageModelV3CallOptions, model: LanguageModelV3 }) => PromiseLike<LanguageModelV3GenerateResult>`): Wraps the generate operation of the language model. Receives both doGenerate and doStream functions.
- `wrapStream?` (`({ doGenerate: () => PromiseLike<LanguageModelV3GenerateResult>, doStream: () => PromiseLike<LanguageModelV3StreamResult>, params: LanguageModelV3CallOptions, model: LanguageModelV3 }) => PromiseLike<LanguageModelV3StreamResult>`): Wraps the stream operation of the language model. Receives both doGenerate and doStream functions.
- `overrideProvider?` (`(options: { model: LanguageModelV3 }) => string`): Override the provider ID of the model.
- `overrideModelId?` (`(options: { model: LanguageModelV3 }) => string`): Override the model ID of the model.
- `overrideSupportedUrls?` (`(options: { model: LanguageModelV3 }) => PromiseLike<Record<string, RegExp[]>> | Record<string, RegExp[]>`): Override the supported URLs for the model.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)