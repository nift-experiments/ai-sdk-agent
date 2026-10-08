---
title: AI SDK Core
description: Reference documentation for the AI SDK Core
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

[AI SDK Core](/v6/docs/ai-sdk-core) is a set of functions that allow you to interact with language models and other AI models.
These functions are designed to be easy-to-use and flexible, allowing you to generate text, structured data,
and embeddings from language models and other AI models.

AI SDK Core contains the following main functions:

#### [generateText()](/v6/docs/reference/ai-sdk-core/generate-text)

Generate text and call tools from a language model.

#### [streamText()](/v6/docs/reference/ai-sdk-core/stream-text)

Stream text and call tools from a language model.

#### [Output](/v6/docs/reference/ai-sdk-core/output)

Structured output types for generateText and streamText.

#### [embed()](/v6/docs/reference/ai-sdk-core/embed)

Generate an embedding for a single value using an embedding model.

#### [embedMany()](/v6/docs/reference/ai-sdk-core/embed-many)

Generate embeddings for several values using an embedding model (batch embedding).

#### [generateImage()](/v6/docs/reference/ai-sdk-core/generate-image)

Generate images based on a given prompt using an image model.

#### [experimental\_generateVideo()](/v6/docs/reference/ai-sdk-core/generate-video)

Generate videos based on a given prompt using a video model.

#### [experimental\_transcribe()](/v6/docs/reference/ai-sdk-core/transcribe)

Generate a transcript from an audio file.

#### [experimental\_generateSpeech()](/v6/docs/reference/ai-sdk-core/generate-speech)

Generate speech audio from text.

It also contains the following helper functions:

#### [tool()](/v6/docs/reference/ai-sdk-core/tool)

Type inference helper function for tools.

#### [createMCPClient()](/v6/docs/reference/ai-sdk-core/create-mcp-client)

Creates a client for connecting to MCP servers.

#### [validateJSONRPCMessage()](/v6/docs/reference/ai-sdk-core/validate-json-rpc-message)

Validates unknown values as MCP JSON-RPC messages.

#### [jsonSchema()](/v6/docs/reference/ai-sdk-core/json-schema)

Creates AI SDK compatible JSON schema objects.

#### [zodSchema()](/v6/docs/reference/ai-sdk-core/zod-schema)

Creates AI SDK compatible Zod schema objects.

#### [createProviderRegistry()](/v6/docs/reference/ai-sdk-core/provider-registry)

Creates a registry for using models from multiple providers.

#### [cosineSimilarity()](/v6/docs/reference/ai-sdk-core/cosine-similarity)

Calculates the cosine similarity between two vectors, e.g. embeddings.

#### [simulateReadableStream()](/v6/docs/reference/ai-sdk-core/simulate-readable-stream)

Creates a ReadableStream that emits values with configurable delays.

#### [wrapLanguageModel()](/v6/docs/reference/ai-sdk-core/wrap-language-model)

Wraps a language model with middleware.

#### [wrapImageModel()](/v6/docs/reference/ai-sdk-core/wrap-image-model)

Wraps an image model with middleware.

#### [extractReasoningMiddleware()](/v6/docs/reference/ai-sdk-core/extract-reasoning-middleware)

Extracts reasoning from the generated text and exposes it as a \`reasoning\` property on the result.

#### [extractJsonMiddleware()](/v6/docs/reference/ai-sdk-core/extract-json-middleware)

Extracts JSON from text content by stripping markdown code fences.

#### [stepCountIs()](/v6/docs/reference/ai-sdk-core/step-count-is)

Creates a stop condition that triggers after a specified number of steps.

#### [hasToolCall()](/v6/docs/reference/ai-sdk-core/has-tool-call)

Creates a stop condition that triggers when a specific tool is called.

#### [isLoopFinished()](/v6/docs/reference/ai-sdk-core/loop-finished)

Creates a stop condition that lets the agent loop run until it naturally finishes.

#### [simulateStreamingMiddleware()](/v6/docs/reference/ai-sdk-core/simulate-streaming-middleware)

Simulates streaming behavior with responses from non-streaming language models.

#### [defaultSettingsMiddleware()](/v6/docs/reference/ai-sdk-core/default-settings-middleware)

Applies default settings to a language model.

#### [smoothStream()](/v6/docs/reference/ai-sdk-core/smooth-stream)

Smooths text and reasoning streaming output.

#### [generateId()](/v6/docs/reference/ai-sdk-core/generate-id)

Helper function for generating unique IDs

#### [createIdGenerator()](/v6/docs/reference/ai-sdk-core/create-id-generator)

Creates an ID generator

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)