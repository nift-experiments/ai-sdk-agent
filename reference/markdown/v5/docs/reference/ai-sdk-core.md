---
title: AI SDK Core
description: Reference documentation for the AI SDK Core
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-core"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

[AI SDK Core](/v5/docs/ai-sdk-core) is a set of functions that allow you to interact with language models and other AI models.
These functions are designed to be easy-to-use and flexible, allowing you to generate text, structured data,
and embeddings from language models and other AI models.

AI SDK Core contains the following main functions:

#### [generateText()](/v5/docs/reference/ai-sdk-core/generate-text)

Generate text and call tools from a language model.

#### [streamText()](/v5/docs/reference/ai-sdk-core/stream-text)

Stream text and call tools from a language model.

#### [generateObject()](/v5/docs/reference/ai-sdk-core/generate-object)

Generate structured data from a language model.

#### [streamObject()](/v5/docs/reference/ai-sdk-core/stream-object)

Stream structured data from a language model.

#### [embed()](/v5/docs/reference/ai-sdk-core/embed)

Generate an embedding for a single value using an embedding model.

#### [embedMany()](/v5/docs/reference/ai-sdk-core/embed-many)

Generate embeddings for several values using an embedding model (batch embedding).

#### [experimental\_generateImage()](/v5/docs/reference/ai-sdk-core/generate-image)

Generate images based on a given prompt using an image model.

#### [experimental\_transcribe()](/v5/docs/reference/ai-sdk-core/transcribe)

Generate a transcript from an audio file.

#### [experimental\_generateSpeech()](/v5/docs/reference/ai-sdk-core/generate-speech)

Generate speech audio from text.

It also contains the following helper functions:

#### [tool()](/v5/docs/reference/ai-sdk-core/tool)

Type inference helper function for tools.

#### [experimental\_createMCPClient()](/v5/docs/reference/ai-sdk-core/create-mcp-client)

Creates a client for connecting to MCP servers.

#### [jsonSchema()](/v5/docs/reference/ai-sdk-core/json-schema)

Creates AI SDK compatible JSON schema objects.

#### [zodSchema()](/v5/docs/reference/ai-sdk-core/zod-schema)

Creates AI SDK compatible Zod schema objects.

#### [createProviderRegistry()](/v5/docs/reference/ai-sdk-core/provider-registry)

Creates a registry for using models from multiple providers.

#### [cosineSimilarity()](/v5/docs/reference/ai-sdk-core/cosine-similarity)

Calculates the cosine similarity between two vectors, e.g. embeddings.

#### [simulateReadableStream()](/v5/docs/reference/ai-sdk-core/simulate-readable-stream)

Creates a ReadableStream that emits values with configurable delays.

#### [wrapLanguageModel()](/v5/docs/reference/ai-sdk-core/wrap-language-model)

Wraps a language model with middleware.

#### [extractReasoningMiddleware()](/v5/docs/reference/ai-sdk-core/extract-reasoning-middleware)

Extracts reasoning from the generated text and exposes it as a \`reasoning\` property on the result.

#### [simulateStreamingMiddleware()](/v5/docs/reference/ai-sdk-core/simulate-streaming-middleware)

Simulates streaming behavior with responses from non-streaming language models.

#### [defaultSettingsMiddleware()](/v5/docs/reference/ai-sdk-core/default-settings-middleware)

Applies default settings to a language model.

#### [smoothStream()](/v5/docs/reference/ai-sdk-core/smooth-stream)

Smooths text streaming output.

#### [generateId()](/v5/docs/reference/ai-sdk-core/generate-id)

Helper function for generating unique IDs

#### [createIdGenerator()](/v5/docs/reference/ai-sdk-core/create-id-generator)

Creates an ID generator

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)