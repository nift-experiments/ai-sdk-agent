---
title: LanguageModelV2Middleware
description: Middleware for enhancing language model behavior (API Reference)
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-core/language-model-v2-middleware"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Language model middleware is an experimental feature.

Language model middleware provides a way to enhance the behavior of language models
by intercepting and modifying the calls to the language model. It can be used to add
features like guardrails, RAG, caching, and logging in a language model agnostic way.

See [Language Model Middleware](/v5/docs/ai-sdk-core/middleware) for more information.

## Import

```
import { LanguageModelV2Middleware } from "ai"
```

## API Signature

- `transformParams` (`({ type: "generate" | "stream", params: LanguageModelV2CallOptions }) => Promise<LanguageModelV2CallOptions>`): Transforms the parameters before they are passed to the language model.
- `wrapGenerate` (`({ doGenerate: DoGenerateFunction, params: LanguageModelV2CallOptions, model: LanguageModelV2 }) => Promise<DoGenerateResult>`): Wraps the generate operation of the language model.
- `wrapStream` (`({ doStream: DoStreamFunction, params: LanguageModelV2CallOptions, model: LanguageModelV2 }) => Promise<DoStreamResult>`): Wraps the stream operation of the language model.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)