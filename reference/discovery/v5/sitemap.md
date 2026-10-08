# AI SDK v5 documentation

## Purpose

This file is a high-level semantic index of the documentation.
It is intended for:

- LLM-assisted navigation (ChatGPT, Claude, etc.)
- Quick orientation for contributors
- Identifying relevant documentation areas during development

It is not intended to replace individual docs.

---

## Documentation

- [Advanced](/v5/docs/advanced) | Type: Conceptual | Summary: Learn how to use advanced functionality within the AI SDK and RSC API. | Topics: v5, docs, advanced

    - [Backpressure](/v5/docs/advanced/backpressure) | Type: Conceptual | Summary: How to handle backpressure and cancellation when working with the AI SDK | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Caching](/v5/docs/advanced/caching) | Type: Conceptual | Summary: How to handle caching when working with the AI SDK | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Language Models as Routers](/v5/docs/advanced/model-as-router) | Type: Conceptual | Summary: Generative User Interfaces and Language Models as Routers | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Multiple Streamables](/v5/docs/advanced/multiple-streamables) | Type: Conceptual | Summary: Learn to handle multiple streamables in your application. | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Multistep Interfaces](/v5/docs/advanced/multistep-interfaces) | Type: Conceptual | Summary: Concepts behind building multistep interfaces | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Prompt Engineering](/v5/docs/advanced/prompt-engineering) | Type: Conceptual | Summary: Learn how to engineer prompts for LLMs with the AI SDK | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Rate Limiting](/v5/docs/advanced/rate-limiting) | Type: Conceptual | Summary: Learn how to rate limit your application. | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Rendering UI with Language Models](/v5/docs/advanced/rendering-ui-with-language-models) | Type: Conceptual | Summary: Rendering UI with Language Models | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Sequential Generations](/v5/docs/advanced/sequential-generations) | Type: Conceptual | Summary: Learn how to implement sequential generations ("chains") with the AI SDK | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Stopping Streams](/v5/docs/advanced/stopping-streams) | Type: Conceptual | Summary: Learn how to cancel streams with the AI SDK | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

    - [Vercel Deployment Guide](/v5/docs/advanced/vercel-deployment-guide) | Type: Conceptual | Summary: Learn how to deploy an AI application to production on Vercel | Prerequisites: /v5/docs/advanced | Topics: v5, docs, advanced

- [Building Agents](/v5/docs/agents/building-agents) | Type: Conceptual | Summary: Complete guide to creating agents with the Agent class. | Topics: v5, docs, agents

- [Loop Control](/v5/docs/agents/loop-control) | Type: Conceptual | Summary: Control agent execution with built-in loop management using stopWhen and prepareStep | Topics: v5, docs, agents

- [Agents](/v5/docs/agents/overview) | Type: Conceptual | Summary: Learn how to build agents with the AI SDK. | Topics: v5, docs, agents

- [Workflow Patterns](/v5/docs/agents/workflows) | Type: Conceptual | Summary: Learn workflow patterns for building reliable agents with the AI SDK. | Topics: v5, docs, agents

- [Embeddings](/v5/docs/ai-sdk-core/embeddings) | Type: Conceptual | Summary: Learn how to embed values with the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Error Handling](/v5/docs/ai-sdk-core/error-handling) | Type: Conceptual | Summary: Learn how to handle errors in the AI SDK Core | Topics: v5, docs, ai-sdk-core

- [Generating Structured Data](/v5/docs/ai-sdk-core/generating-structured-data) | Type: Conceptual | Summary: Learn how to generate structured data with the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Generating Text](/v5/docs/ai-sdk-core/generating-text) | Type: Conceptual | Summary: Learn how to generate text with the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Image Generation](/v5/docs/ai-sdk-core/image-generation) | Type: Conceptual | Summary: Learn how to generate images with the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Model Context Protocol (MCP)](/v5/docs/ai-sdk-core/mcp-tools) | Type: Conceptual | Summary: Learn how to connect to Model Context Protocol (MCP) servers and use their tools with AI SDK Core. | Topics: v5, docs, ai-sdk-core

- [Language Model Middleware](/v5/docs/ai-sdk-core/middleware) | Type: Conceptual | Summary: Learn how to use middleware to enhance the behavior of language models | Topics: v5, docs, ai-sdk-core

- [Overview](/v5/docs/ai-sdk-core/overview) | Type: Conceptual | Summary: An overview of AI SDK Core. | Topics: v5, docs, ai-sdk-core

- [Prompt Engineering](/v5/docs/ai-sdk-core/prompt-engineering) | Type: Conceptual | Summary: Learn how to develop prompts with AI SDK Core. | Topics: v5, docs, ai-sdk-core

- [Provider & Model Management](/v5/docs/ai-sdk-core/provider-management) | Type: Conceptual | Summary: Learn how to work with multiple providers and models | Topics: v5, docs, ai-sdk-core

- [Settings](/v5/docs/ai-sdk-core/settings) | Type: Conceptual | Summary: Learn how to configure the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Speech](/v5/docs/ai-sdk-core/speech) | Type: Conceptual | Summary: Learn how to generate speech from text with the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Telemetry](/v5/docs/ai-sdk-core/telemetry) | Type: Conceptual | Summary: Using OpenTelemetry with AI SDK Core | Topics: v5, docs, ai-sdk-core

- [Testing](/v5/docs/ai-sdk-core/testing) | Type: Conceptual | Summary: Learn how to use AI SDK Core mock providers for testing. | Topics: v5, docs, ai-sdk-core

- [Tool Calling](/v5/docs/ai-sdk-core/tools-and-tool-calling) | Type: Conceptual | Summary: Learn about tool calling and multi-step calls (using stopWhen) with AI SDK Core. | Topics: v5, docs, ai-sdk-core

- [Transcription](/v5/docs/ai-sdk-core/transcription) | Type: Conceptual | Summary: Learn how to transcribe audio with the AI SDK. | Topics: v5, docs, ai-sdk-core

- [Handling Authentication](/v5/docs/ai-sdk-rsc/authentication) | Type: Conceptual | Summary: Learn how to authenticate with the AI SDK. | Topics: v5, docs, ai-sdk-rsc

- [Error Handling](/v5/docs/ai-sdk-rsc/error-handling) | Type: Conceptual | Summary: Learn how to handle errors with the AI SDK. | Topics: v5, docs, ai-sdk-rsc

- [Managing Generative UI State](/v5/docs/ai-sdk-rsc/generative-ui-state) | Type: Conceptual | Summary: Overview of the AI and UI states | Topics: v5, docs, ai-sdk-rsc

- [Handling Loading State](/v5/docs/ai-sdk-rsc/loading-state) | Type: Conceptual | Summary: Overview of handling loading state with AI SDK RSC | Topics: v5, docs, ai-sdk-rsc

- [Migrating from RSC to UI](/v5/docs/ai-sdk-rsc/migrating-to-ui) | Type: Conceptual | Summary: Learn how to migrate from AI SDK RSC to AI SDK UI. | Topics: v5, docs, ai-sdk-rsc

- [Multistep Interfaces](/v5/docs/ai-sdk-rsc/multistep-interfaces) | Type: Conceptual | Summary: Overview of Building Multistep Interfaces with AI SDK RSC | Topics: v5, docs, ai-sdk-rsc

- [Overview](/v5/docs/ai-sdk-rsc/overview) | Type: Conceptual | Summary: An overview of AI SDK RSC. | Topics: v5, docs, ai-sdk-rsc

- [Saving and Restoring States](/v5/docs/ai-sdk-rsc/saving-and-restoring-states) | Type: Conceptual | Summary: Saving and restoring AI and UI states with onGetUIState and onSetAIState | Topics: v5, docs, ai-sdk-rsc

- [Streaming React Components](/v5/docs/ai-sdk-rsc/streaming-react-components) | Type: Conceptual | Summary: Overview of streaming RSCs | Topics: v5, docs, ai-sdk-rsc

- [Streaming Values](/v5/docs/ai-sdk-rsc/streaming-values) | Type: Conceptual | Summary: Overview of streaming RSCs | Topics: v5, docs, ai-sdk-rsc

- [Chatbot](/v5/docs/ai-sdk-ui/chatbot) | Type: Conceptual | Summary: Learn how to use the useChat hook. | Topics: v5, docs, ai-sdk-ui

- [Chatbot Message Persistence](/v5/docs/ai-sdk-ui/chatbot-message-persistence) | Type: Conceptual | Summary: Learn how to store and load chat messages in a chatbot. | Topics: v5, docs, ai-sdk-ui

- [Chatbot Resume Streams](/v5/docs/ai-sdk-ui/chatbot-resume-streams) | Type: Conceptual | Summary: Learn how to resume chatbot streams after client disconnects. | Topics: v5, docs, ai-sdk-ui

- [Chatbot Tool Usage](/v5/docs/ai-sdk-ui/chatbot-tool-usage) | Type: Conceptual | Summary: Learn how to use tools with the useChat hook. | Topics: v5, docs, ai-sdk-ui

- [Completion](/v5/docs/ai-sdk-ui/completion) | Type: Conceptual | Summary: Learn how to use the useCompletion hook. | Topics: v5, docs, ai-sdk-ui

- [Error Handling](/v5/docs/ai-sdk-ui/error-handling) | Type: Conceptual | Summary: Learn how to handle errors in the AI SDK UI | Topics: v5, docs, ai-sdk-ui

- [Generative User Interfaces](/v5/docs/ai-sdk-ui/generative-user-interfaces) | Type: Conceptual | Summary: Learn how to build Generative UI with AI SDK UI. | Topics: v5, docs, ai-sdk-ui

- [Message Metadata](/v5/docs/ai-sdk-ui/message-metadata) | Type: Conceptual | Summary: Learn how to attach and use metadata with messages in AI SDK UI | Topics: v5, docs, ai-sdk-ui

- [Object Generation](/v5/docs/ai-sdk-ui/object-generation) | Type: Conceptual | Summary: Learn how to use the useObject hook. | Topics: v5, docs, ai-sdk-ui

- [Overview](/v5/docs/ai-sdk-ui/overview) | Type: Conceptual | Summary: An overview of AI SDK UI. | Topics: v5, docs, ai-sdk-ui

- [Reading UIMessage Streams](/v5/docs/ai-sdk-ui/reading-ui-message-streams) | Type: Conceptual | Summary: Learn how to read UIMessage streams. | Topics: v5, docs, ai-sdk-ui

- [Stream Protocols](/v5/docs/ai-sdk-ui/stream-protocol) | Type: Conceptual | Summary: Learn more about the supported stream protocols in the AI SDK. | Topics: v5, docs, ai-sdk-ui

- [Streaming Custom Data](/v5/docs/ai-sdk-ui/streaming-data) | Type: Conceptual | Summary: Learn how to stream custom data from the server to the client. | Topics: v5, docs, ai-sdk-ui

- [Transport](/v5/docs/ai-sdk-ui/transport) | Type: Conceptual | Summary: Learn how to use custom transports with useChat. | Topics: v5, docs, ai-sdk-ui

- [AI SDK 6 Beta](/v5/docs/announcing-ai-sdk-6-beta) | Type: Conceptual | Summary: Get started with the Beta version of AI SDK 6. | Topics: v5, docs, announcing-ai-sdk-6-beta

- [Overview](/v5/docs/foundations/overview) | Type: Conceptual | Summary: An overview of foundational concepts critical to understanding the AI SDK | Topics: v5, docs, foundations

- [Prompts](/v5/docs/foundations/prompts) | Type: Conceptual | Summary: Learn about the Prompt structure used in the AI SDK. | Topics: v5, docs, foundations

- [Providers and Models](/v5/docs/foundations/providers-and-models) | Type: Conceptual | Summary: Learn about the providers and models available in the AI SDK. | Topics: v5, docs, foundations

- [Streaming](/v5/docs/foundations/streaming) | Type: Conceptual | Summary: Why use streaming for AI applications? | Topics: v5, docs, foundations

- [Tools](/v5/docs/foundations/tools) | Type: Conceptual | Summary: Learn about tools with the AI SDK. | Topics: v5, docs, foundations

- [Getting Started](/v5/docs/getting-started) | Type: Guide | Summary: Welcome to the AI SDK documentation! | Topics: v5, docs, getting-started

    - [Choosing a Provider](/v5/docs/getting-started/choosing-a-provider) | Type: Guide | Summary: Learn how to configure and authenticate with AI providers in the AI SDK. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Expo](/v5/docs/getting-started/expo) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Expo. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Navigating the Library](/v5/docs/getting-started/navigating-the-library) | Type: Guide | Summary: Learn how to navigate the AI SDK. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Next.js App Router](/v5/docs/getting-started/nextjs-app-router) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Next.js App Router. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Next.js Pages Router](/v5/docs/getting-started/nextjs-pages-router) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Next.js Pages Router. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Node.js](/v5/docs/getting-started/nodejs) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Node.js. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Vue.js (Nuxt)](/v5/docs/getting-started/nuxt) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Vue.js (Nuxt). | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [Svelte](/v5/docs/getting-started/svelte) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Svelte. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

    - [TanStack Start](/v5/docs/getting-started/tanstack-start) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and TanStack Start. | Prerequisites: /v5/docs/getting-started | Topics: v5, docs, getting-started

- [AI SDK by Vercel](/v5/docs/introduction) | Type: Conceptual | Summary: The AI SDK is the TypeScript toolkit for building AI applications and agents with React, Next.js, Vue, Svelte, Node.js, and more. | Topics: v5, docs, introduction

- [Migration Guides](/v5/docs/migration-guides) | Type: Conceptual | Summary: Learn how to upgrade between Vercel AI versions. | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 3.0 to 3.1](/v5/docs/migration-guides/migration-guide-3-1) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.0 to 3.1. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 3.1 to 3.2](/v5/docs/migration-guides/migration-guide-3-2) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.1 to 3.2. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 3.2 to 3.3](/v5/docs/migration-guides/migration-guide-3-3) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.2 to 3.3. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 3.3 to 3.4](/v5/docs/migration-guides/migration-guide-3-4) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.3 to 3.4. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 3.4 to 4.0](/v5/docs/migration-guides/migration-guide-4-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.4 to 4.0. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 4.0 to 4.1](/v5/docs/migration-guides/migration-guide-4-1) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.0 to 4.1. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 4.1 to 4.2](/v5/docs/migration-guides/migration-guide-4-2) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.1 to 4.2. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 4.x to 5.0](/v5/docs/migration-guides/migration-guide-5-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.x to 5.0. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate Your Data to AI SDK 5.0](/v5/docs/migration-guides/migration-guide-5-0-data) | Type: Conceptual | Summary: Learn how to migrate your persisted messages and chat data from AI SDK 4.x to 5.0. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Migrate AI SDK 5.x to 6.0 Beta](/v5/docs/migration-guides/migration-guide-6-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 5 to 6.0 Beta. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

    - [Versioning](/v5/docs/migration-guides/versioning) | Type: Conceptual | Summary: Understand how the AI SDK approaches versioning. | Prerequisites: /v5/docs/migration-guides | Topics: v5, docs, migration-guides

- [Reference](/v5/docs/reference) | Type: Reference | Summary: Reference documentation for the AI SDK | Topics: v5, docs, reference

    - [AI SDK Core](/v5/docs/reference/ai-sdk-core) | Type: Reference | Summary: Reference documentation for the AI SDK Core | Prerequisites: /v5/docs/reference | Topics: v5, docs, reference

        - [cosineSimilarity](/v5/docs/reference/ai-sdk-core/cosine-similarity) | Type: Reference | Summary: Calculate the cosine similarity between two vectors (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [createIdGenerator](/v5/docs/reference/ai-sdk-core/create-id-generator) | Type: Reference | Summary: Create a customizable unique identifier generator (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [experimental_createMCPClient](/v5/docs/reference/ai-sdk-core/create-mcp-client) | Type: Reference | Summary: Create a client for connecting to MCP servers | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [customProvider](/v5/docs/reference/ai-sdk-core/custom-provider) | Type: Reference | Summary: Custom provider that uses models from a different provider (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [defaultSettingsMiddleware](/v5/docs/reference/ai-sdk-core/default-settings-middleware) | Type: Reference | Summary: Middleware that applies default settings for language models | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [dynamicTool](/v5/docs/reference/ai-sdk-core/dynamic-tool) | Type: Reference | Summary: Helper function for creating dynamic tools with unknown types | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [embed](/v5/docs/reference/ai-sdk-core/embed) | Type: Reference | Summary: API Reference for embed. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [embedMany](/v5/docs/reference/ai-sdk-core/embed-many) | Type: Reference | Summary: API Reference for embedMany. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [extractReasoningMiddleware](/v5/docs/reference/ai-sdk-core/extract-reasoning-middleware) | Type: Reference | Summary: Middleware that extracts XML-tagged reasoning sections from generated text | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [generateId](/v5/docs/reference/ai-sdk-core/generate-id) | Type: Reference | Summary: Generate a unique identifier (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [generateImage](/v5/docs/reference/ai-sdk-core/generate-image) | Type: Reference | Summary: API Reference for generateImage. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [generateObject](/v5/docs/reference/ai-sdk-core/generate-object) | Type: Reference | Summary: API Reference for generateObject. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [generateSpeech](/v5/docs/reference/ai-sdk-core/generate-speech) | Type: Reference | Summary: API Reference for generateSpeech. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [generateText](/v5/docs/reference/ai-sdk-core/generate-text) | Type: Reference | Summary: API Reference for generateText. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [hasToolCall](/v5/docs/reference/ai-sdk-core/has-tool-call) | Type: Reference | Summary: API Reference for hasToolCall. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [jsonSchema](/v5/docs/reference/ai-sdk-core/json-schema) | Type: Reference | Summary: Helper function for creating JSON schemas | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [LanguageModelV2Middleware](/v5/docs/reference/ai-sdk-core/language-model-v2-middleware) | Type: Reference | Summary: Middleware for enhancing language model behavior (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [Experimental_StdioMCPTransport](/v5/docs/reference/ai-sdk-core/mcp-stdio-transport) | Type: Reference | Summary: Create a transport for Model Context Protocol (MCP) clients to communicate with MCP servers using standard input and output streams | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [ModelMessage](/v5/docs/reference/ai-sdk-core/model-message) | Type: Reference | Summary: Message types for AI SDK Core (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [createProviderRegistry](/v5/docs/reference/ai-sdk-core/provider-registry) | Type: Reference | Summary: Registry for managing multiple providers and models (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [safeValidateUIMessages](/v5/docs/reference/ai-sdk-core/safe-validate-ui-messages) | Type: Reference | Summary: API Reference for safeValidateUIMessages | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [simulateReadableStream](/v5/docs/reference/ai-sdk-core/simulate-readable-stream) | Type: Reference | Summary: Create a ReadableStream that emits values with configurable delays | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [simulateStreamingMiddleware](/v5/docs/reference/ai-sdk-core/simulate-streaming-middleware) | Type: Reference | Summary: Middleware that simulates streaming for non-streaming language models | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [smoothStream](/v5/docs/reference/ai-sdk-core/smooth-stream) | Type: Reference | Summary: Stream transformer for smoothing text output | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [stepCountIs](/v5/docs/reference/ai-sdk-core/step-count-is) | Type: Reference | Summary: API Reference for stepCountIs. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [streamObject](/v5/docs/reference/ai-sdk-core/stream-object) | Type: Reference | Summary: API Reference for streamObject | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [streamText](/v5/docs/reference/ai-sdk-core/stream-text) | Type: Reference | Summary: API Reference for streamText. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [tool](/v5/docs/reference/ai-sdk-core/tool) | Type: Reference | Summary: Helper function for tool type inference | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [transcribe](/v5/docs/reference/ai-sdk-core/transcribe) | Type: Reference | Summary: API Reference for transcribe. | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [UIMessage](/v5/docs/reference/ai-sdk-core/ui-message) | Type: Reference | Summary: API Reference for UIMessage | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [valibotSchema](/v5/docs/reference/ai-sdk-core/valibot-schema) | Type: Reference | Summary: Helper function for creating Valibot schemas | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [validateUIMessages](/v5/docs/reference/ai-sdk-core/validate-ui-messages) | Type: Reference | Summary: API Reference for validateUIMessages | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [wrapLanguageModel](/v5/docs/reference/ai-sdk-core/wrap-language-model) | Type: Reference | Summary: Function for wrapping a language model with middleware (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

        - [zodSchema](/v5/docs/reference/ai-sdk-core/zod-schema) | Type: Reference | Summary: Helper function for creating Zod schemas | Prerequisites: /v5/docs/reference/ai-sdk-core | Topics: v5, docs, reference

    - [AI SDK Errors](/v5/docs/reference/ai-sdk-errors) | Type: Reference | Summary: Reference for AI SDK error classes and typed error handling. | Prerequisites: /v5/docs/reference | Topics: v5, docs, reference

        - [AI_APICallError](/v5/docs/reference/ai-sdk-errors/ai-api-call-error) | Type: Reference | Summary: Learn how to fix AI_APICallError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_DownloadError](/v5/docs/reference/ai-sdk-errors/ai-download-error) | Type: Reference | Summary: Learn how to fix AI_DownloadError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_EmptyResponseBodyError](/v5/docs/reference/ai-sdk-errors/ai-empty-response-body-error) | Type: Reference | Summary: Learn how to fix AI_EmptyResponseBodyError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidArgumentError](/v5/docs/reference/ai-sdk-errors/ai-invalid-argument-error) | Type: Reference | Summary: Learn how to fix AI_InvalidArgumentError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidDataContent](/v5/docs/reference/ai-sdk-errors/ai-invalid-data-content) | Type: Reference | Summary: Learn how to fix AI_InvalidDataContent | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidDataContentError](/v5/docs/reference/ai-sdk-errors/ai-invalid-data-content-error) | Type: Reference | Summary: How to fix AI_InvalidDataContentError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidMessageRoleError](/v5/docs/reference/ai-sdk-errors/ai-invalid-message-role-error) | Type: Reference | Summary: Learn how to fix AI_InvalidMessageRoleError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidPromptError](/v5/docs/reference/ai-sdk-errors/ai-invalid-prompt-error) | Type: Reference | Summary: Learn how to fix AI_InvalidPromptError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidResponseDataError](/v5/docs/reference/ai-sdk-errors/ai-invalid-response-data-error) | Type: Reference | Summary: Learn how to fix AI_InvalidResponseDataError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_InvalidToolInputError](/v5/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolInputError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_JSONParseError](/v5/docs/reference/ai-sdk-errors/ai-json-parse-error) | Type: Reference | Summary: Learn how to fix AI_JSONParseError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_LoadAPIKeyError](/v5/docs/reference/ai-sdk-errors/ai-load-api-key-error) | Type: Reference | Summary: Learn how to fix AI_LoadAPIKeyError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_LoadSettingError](/v5/docs/reference/ai-sdk-errors/ai-load-setting-error) | Type: Reference | Summary: Learn how to fix AI_LoadSettingError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_MessageConversionError](/v5/docs/reference/ai-sdk-errors/ai-message-conversion-error) | Type: Reference | Summary: Learn how to fix AI_MessageConversionError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoContentGeneratedError](/v5/docs/reference/ai-sdk-errors/ai-no-content-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoContentGeneratedError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoImageGeneratedError](/v5/docs/reference/ai-sdk-errors/ai-no-image-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoImageGeneratedError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoObjectGeneratedError](/v5/docs/reference/ai-sdk-errors/ai-no-object-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoObjectGeneratedError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoOutputSpecifiedError](/v5/docs/reference/ai-sdk-errors/ai-no-output-specified-error) | Type: Reference | Summary: Learn how to fix AI_NoOutputSpecifiedError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoSpeechGeneratedError](/v5/docs/reference/ai-sdk-errors/ai-no-speech-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoSpeechGeneratedError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoSuchModelError](/v5/docs/reference/ai-sdk-errors/ai-no-such-model-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchModelError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoSuchProviderError](/v5/docs/reference/ai-sdk-errors/ai-no-such-provider-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchProviderError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoSuchToolError](/v5/docs/reference/ai-sdk-errors/ai-no-such-tool-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchToolError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_NoTranscriptGeneratedError](/v5/docs/reference/ai-sdk-errors/ai-no-transcript-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoTranscriptGeneratedError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_RetryError](/v5/docs/reference/ai-sdk-errors/ai-retry-error) | Type: Reference | Summary: Learn how to fix AI_RetryError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_TooManyEmbeddingValuesForCallError](/v5/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error) | Type: Reference | Summary: Learn how to fix AI_TooManyEmbeddingValuesForCallError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [ToolCallRepairError](/v5/docs/reference/ai-sdk-errors/ai-tool-call-repair-error) | Type: Reference | Summary: Learn how to fix AI SDK ToolCallRepairError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_TypeValidationError](/v5/docs/reference/ai-sdk-errors/ai-type-validation-error) | Type: Reference | Summary: Learn how to fix AI_TypeValidationError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

        - [AI_UnsupportedFunctionalityError](/v5/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error) | Type: Reference | Summary: Learn how to fix AI_UnsupportedFunctionalityError | Prerequisites: /v5/docs/reference/ai-sdk-errors | Topics: v5, docs, reference

    - [AI SDK RSC](/v5/docs/reference/ai-sdk-rsc) | Type: Reference | Summary: Reference documentation for the AI SDK UI | Prerequisites: /v5/docs/reference | Topics: v5, docs, reference

        - [createAI](/v5/docs/reference/ai-sdk-rsc/create-ai) | Type: Reference | Summary: Reference for the createAI function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [createStreamableUI](/v5/docs/reference/ai-sdk-rsc/create-streamable-ui) | Type: Reference | Summary: Reference for the createStreamableUI function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [createStreamableValue](/v5/docs/reference/ai-sdk-rsc/create-streamable-value) | Type: Reference | Summary: Reference for the createStreamableValue function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [getAIState](/v5/docs/reference/ai-sdk-rsc/get-ai-state) | Type: Reference | Summary: Reference for the getAIState function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [getMutableAIState](/v5/docs/reference/ai-sdk-rsc/get-mutable-ai-state) | Type: Reference | Summary: Reference for the getMutableAIState function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [readStreamableValue](/v5/docs/reference/ai-sdk-rsc/read-streamable-value) | Type: Reference | Summary: Reference for the readStreamableValue function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [render (Removed)](/v5/docs/reference/ai-sdk-rsc/render) | Type: Reference | Summary: Reference for the render function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [streamUI](/v5/docs/reference/ai-sdk-rsc/stream-ui) | Type: Reference | Summary: Reference for the streamUI function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [useActions](/v5/docs/reference/ai-sdk-rsc/use-actions) | Type: Reference | Summary: Reference for the useActions function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [useAIState](/v5/docs/reference/ai-sdk-rsc/use-ai-state) | Type: Reference | Summary: Reference for the useAIState function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [useStreamableValue](/v5/docs/reference/ai-sdk-rsc/use-streamable-value) | Type: Reference | Summary: Reference for the useStreamableValue function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

        - [useUIState](/v5/docs/reference/ai-sdk-rsc/use-ui-state) | Type: Reference | Summary: Reference for the useUIState function from the AI SDK RSC | Prerequisites: /v5/docs/reference/ai-sdk-rsc | Topics: v5, docs, reference

    - [AI SDK UI](/v5/docs/reference/ai-sdk-ui) | Type: Reference | Summary: Reference documentation for the AI SDK UI | Prerequisites: /v5/docs/reference | Topics: v5, docs, reference

        - [convertToModelMessages](/v5/docs/reference/ai-sdk-ui/convert-to-model-messages) | Type: Reference | Summary: Convert useChat messages to ModelMessages for AI functions (API Reference) | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [createUIMessageStream](/v5/docs/reference/ai-sdk-ui/create-ui-message-stream) | Type: Reference | Summary: API Reference for createUIMessageStream. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [createUIMessageStreamResponse](/v5/docs/reference/ai-sdk-ui/create-ui-message-stream-response) | Type: Reference | Summary: API Reference for createUIMessageStreamResponse. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [InferUITool](/v5/docs/reference/ai-sdk-ui/infer-ui-tool) | Type: Reference | Summary: API Reference for InferUITool. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [InferUITools](/v5/docs/reference/ai-sdk-ui/infer-ui-tools) | Type: Reference | Summary: API Reference for InferUITools. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [pipeUIMessageStreamToResponse](/v5/docs/reference/ai-sdk-ui/pipe-ui-message-stream-to-response) | Type: Reference | Summary: Learn to use pipeUIMessageStreamToResponse helper function to pipe streaming data to a ServerResponse object. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [pruneMessages](/v5/docs/reference/ai-sdk-ui/prune-messages) | Type: Reference | Summary: API Reference for pruneMessages. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [readUIMessageStream](/v5/docs/reference/ai-sdk-ui/read-ui-message-stream) | Type: Reference | Summary: API Reference for readUIMessageStream. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [useChat](/v5/docs/reference/ai-sdk-ui/use-chat) | Type: Reference | Summary: API reference for the useChat hook. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [useCompletion](/v5/docs/reference/ai-sdk-ui/use-completion) | Type: Reference | Summary: API reference for the useCompletion hook. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

        - [useObject](/v5/docs/reference/ai-sdk-ui/use-object) | Type: Reference | Summary: API reference for the useObject hook. | Prerequisites: /v5/docs/reference/ai-sdk-ui | Topics: v5, docs, reference

    - [Stream Helpers](/v5/docs/reference/stream-helpers) | Type: Reference | Summary: Learn to use help functions that help stream generations from different providers. | Prerequisites: /v5/docs/reference | Topics: v5, docs, reference

        - [AIStream](/v5/docs/reference/stream-helpers/ai-stream) | Type: Reference | Summary: Learn to use AIStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [AnthropicStream](/v5/docs/reference/stream-helpers/anthropic-stream) | Type: Reference | Summary: Learn to use AnthropicStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [AWSBedrockAnthropicStream](/v5/docs/reference/stream-helpers/aws-bedrock-anthropic-stream) | Type: Reference | Summary: Learn to use AWSBedrockAnthropicStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [AWSBedrockCohereStream](/v5/docs/reference/stream-helpers/aws-bedrock-cohere-stream) | Type: Reference | Summary: Learn to use AWSBedrockCohereStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [AWSBedrockLlama2Stream](/v5/docs/reference/stream-helpers/aws-bedrock-llama-2-stream) | Type: Reference | Summary: Learn to use AWSBedrockLlama2Stream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [AWSBedrockAnthropicMessagesStream](/v5/docs/reference/stream-helpers/aws-bedrock-messages-stream) | Type: Reference | Summary: Learn to use AWSBedrockAnthropicMessagesStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [AWSBedrockStream](/v5/docs/reference/stream-helpers/aws-bedrock-stream) | Type: Reference | Summary: Learn to use AWSBedrockStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [CohereStream](/v5/docs/reference/stream-helpers/cohere-stream) | Type: Reference | Summary: Learn to use CohereStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [GoogleGenerativeAIStream](/v5/docs/reference/stream-helpers/google-generative-ai-stream) | Type: Reference | Summary: Learn to use GoogleGenerativeAIStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [HuggingFaceStream](/v5/docs/reference/stream-helpers/hugging-face-stream) | Type: Reference | Summary: Learn to use HuggingFaceStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [InkeepStream](/v5/docs/reference/stream-helpers/inkeep-stream) | Type: Reference | Summary: Learn to use InkeepStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [@ai-sdk/langchain Adapter](/v5/docs/reference/stream-helpers/langchain-adapter) | Type: Reference | Summary: API Reference for the LangChain Adapter. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [@ai-sdk/llamaindex Adapter](/v5/docs/reference/stream-helpers/llamaindex-adapter) | Type: Reference | Summary: API Reference for the LlamaIndex Adapter. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [MistralStream](/v5/docs/reference/stream-helpers/mistral-stream) | Type: Reference | Summary: Learn to use MistralStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [OpenAIStream](/v5/docs/reference/stream-helpers/openai-stream) | Type: Reference | Summary: Learn to use OpenAIStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [ReplicateStream](/v5/docs/reference/stream-helpers/replicate-stream) | Type: Reference | Summary: Learn to use ReplicateStream helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [streamToResponse](/v5/docs/reference/stream-helpers/stream-to-response) | Type: Reference | Summary: Learn to use streamToResponse helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

        - [StreamingTextResponse](/v5/docs/reference/stream-helpers/streaming-text-response) | Type: Reference | Summary: Learn to use StreamingTextResponse helper function in your application. | Prerequisites: /v5/docs/reference/stream-helpers | Topics: v5, docs, reference

- [Troubleshooting](/v5/docs/troubleshooting) | Type: Conceptual | Summary: Troubleshooting information for common issues encountered with the AI SDK. | Topics: v5, docs, troubleshooting

    - [Abort breaks resumable streams](/v5/docs/troubleshooting/abort-breaks-resumable-streams) | Type: Conceptual | Summary: Troubleshooting stream resumption failures when using abort functionality | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Azure OpenAI Slow to Stream](/v5/docs/troubleshooting/azure-stream-slow) | Type: Conceptual | Summary: Learn to troubleshoot Azure OpenAI slow to stream issues. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Client-Side Function Calls Not Invoked](/v5/docs/troubleshooting/client-side-function-calls-not-invoked) | Type: Conceptual | Summary: Troubleshooting client-side function calls not being invoked. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Server Action Plain Objects Error](/v5/docs/troubleshooting/client-stream-error) | Type: Conceptual | Summary: Troubleshooting errors related to using AI SDK Core functions with Server Actions. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Jest: cannot find module '@ai-sdk/rsc'](/v5/docs/troubleshooting/jest-cannot-find-module-ai-rsc) | Type: Conceptual | Summary: Troubleshooting AI SDK errors related to the Jest: cannot find module '@ai-sdk/rsc' error | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Model is not assignable to type "LanguageModelV1"](/v5/docs/troubleshooting/model-is-not-assignable-to-type) | Type: Conceptual | Summary: Troubleshooting errors related to incompatible models. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Object generation failed with OpenAI](/v5/docs/troubleshooting/no-object-generated-content-filter) | Type: Conceptual | Summary: Troubleshooting NoObjectGeneratedError with finish-reason content-filter caused by incompatible Zod schema types when using OpenAI structured outputs | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Type Error with onToolCall](/v5/docs/troubleshooting/ontoolcall-type-narrowing) | Type: Conceptual | Summary: How to handle TypeScript type errors when using the onToolCall callback | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [React error "Maximum update depth exceeded"](/v5/docs/troubleshooting/react-maximum-update-depth-exceeded) | Type: Conceptual | Summary: Troubleshooting errors related to the "Maximum update depth exceeded" error. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Repeated assistant messages in useChat](/v5/docs/troubleshooting/repeated-assistant-messages) | Type: Conceptual | Summary: Troubleshooting duplicate assistant messages when using useChat with streamText | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Server Actions in Client Components](/v5/docs/troubleshooting/server-actions-in-client-components) | Type: Conceptual | Summary: Troubleshooting errors related to server actions in client components. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [useChat/useCompletion stream output contains 0:... instead of text](/v5/docs/troubleshooting/strange-stream-output) | Type: Conceptual | Summary: How to fix strange stream output in the UI | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [onFinish not called when stream is aborted](/v5/docs/troubleshooting/stream-abort-handling) | Type: Conceptual | Summary: Troubleshooting onFinish callback not executing when streams are aborted with toUIMessageStreamResponse | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [streamText fails silently](/v5/docs/troubleshooting/stream-text-not-working) | Type: Conceptual | Summary: Troubleshooting errors related to the streamText function not working. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Streamable UI Errors](/v5/docs/troubleshooting/streamable-ui-errors) | Type: Conceptual | Summary: Troubleshooting errors related to streamable UI. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Streaming Not Working When Deployed](/v5/docs/troubleshooting/streaming-not-working-when-deployed) | Type: Conceptual | Summary: Troubleshooting streaming issues in deployed apps. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Streaming Not Working When Proxied](/v5/docs/troubleshooting/streaming-not-working-when-proxied) | Type: Conceptual | Summary: Troubleshooting streaming issues in proxied apps. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Streaming Status Shows But No Text Appears](/v5/docs/troubleshooting/streaming-status-delay) | Type: Conceptual | Summary: Why useChat shows "streaming" status without any visible content | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Getting Timeouts When Deploying on Vercel](/v5/docs/troubleshooting/timeout-on-vercel) | Type: Conceptual | Summary: Learn how to fix timeouts and cut off responses when deploying to Vercel. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Tool calling with generateObject and streamObject](/v5/docs/troubleshooting/tool-calling-with-structured-outputs) | Type: Conceptual | Summary: Troubleshooting tool calling when combined with generateObject and streamObject | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Tool Invocation Missing Result Error](/v5/docs/troubleshooting/tool-invocation-missing-result) | Type: Conceptual | Summary: How to fix the "ToolInvocation must have a result" error when using tools without execute functions | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [TypeScript error "Cannot find namespace 'JSX'"](/v5/docs/troubleshooting/typescript-cannot-find-namespace-jsx) | Type: Conceptual | Summary: Troubleshooting errors related to TypeScript and JSX. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [TypeScript performance issues with Zod and AI SDK 5](/v5/docs/troubleshooting/typescript-performance-zod) | Type: Conceptual | Summary: Troubleshooting TypeScript server crashes and slow performance when using Zod with AI SDK 5 | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Unclosed Streams](/v5/docs/troubleshooting/unclosed-streams) | Type: Conceptual | Summary: Troubleshooting errors related to unclosed streams. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Unsupported model version error](/v5/docs/troubleshooting/unsupported-model-version) | Type: Conceptual | Summary: Troubleshooting the AI_UnsupportedModelVersionError when migrating to AI SDK 5 | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [useChat "An error occurred"](/v5/docs/troubleshooting/use-chat-an-error-occurred) | Type: Conceptual | Summary: Troubleshooting errors related to the "An error occurred" error in useChat. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Custom headers, body, and credentials not working with useChat](/v5/docs/troubleshooting/use-chat-custom-request-options) | Type: Conceptual | Summary: Troubleshooting errors related to custom request configuration in useChat hook | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [useChat Failed to Parse Stream](/v5/docs/troubleshooting/use-chat-failed-to-parse-stream) | Type: Conceptual | Summary: Troubleshooting errors related to the Use Chat Failed to Parse Stream error. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [Stale body values with useChat](/v5/docs/troubleshooting/use-chat-stale-body-data) | Type: Conceptual | Summary: Troubleshooting stale values when passing information via the body parameter of useChat | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

    - [useChat No Response](/v5/docs/troubleshooting/use-chat-tools-no-response) | Type: Conceptual | Summary: Troubleshooting errors related to the Use Chat Failed to Parse Stream error. | Prerequisites: /v5/docs/troubleshooting | Topics: v5, docs, troubleshooting

## Providers

- [Adapters](/v5/providers/adapters) | Type: Conceptual | Summary: Learn how to use AI SDK Adapters. | Topics: v5, providers, adapters

    - [LangChain](/v5/providers/adapters/langchain) | Type: Conceptual | Summary: Learn how to use LangChain with the AI SDK. | Prerequisites: /v5/providers/adapters | Topics: v5, providers, adapters

    - [LlamaIndex](/v5/providers/adapters/llamaindex) | Type: Conceptual | Summary: Learn how to use LlamaIndex with the AI SDK. | Prerequisites: /v5/providers/adapters | Topics: v5, providers, adapters

- [AI SDK Providers](/v5/providers/ai-sdk-providers) | Type: Conceptual | Summary: Learn how to use AI SDK providers. | Topics: v5, providers, ai-sdk-providers

    - [AI Gateway](/v5/providers/ai-sdk-providers/ai-gateway) | Type: Conceptual | Summary: Learn how to use the AI Gateway provider with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Alibaba](/v5/providers/ai-sdk-providers/alibaba) | Type: Conceptual | Summary: Learn how to use Alibaba Cloud Model Studio (Qwen) models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Amazon Bedrock](/v5/providers/ai-sdk-providers/amazon-bedrock) | Type: Conceptual | Summary: Learn how to use the Amazon Bedrock provider. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Anthropic](/v5/providers/ai-sdk-providers/anthropic) | Type: Conceptual | Summary: Learn how to use the Anthropic provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [AssemblyAI](/v5/providers/ai-sdk-providers/assemblyai) | Type: Conceptual | Summary: Learn how to use the AssemblyAI provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Azure OpenAI](/v5/providers/ai-sdk-providers/azure) | Type: Conceptual | Summary: Learn how to use the Azure OpenAI provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Baseten](/v5/providers/ai-sdk-providers/baseten) | Type: Conceptual | Summary: Learn how to use Baseten models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Black Forest Labs](/v5/providers/ai-sdk-providers/black-forest-labs) | Type: Conceptual | Summary: Learn how to use Black Forest Labs models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Cerebras](/v5/providers/ai-sdk-providers/cerebras) | Type: Conceptual | Summary: Learn how to use Cerebras's models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Cohere](/v5/providers/ai-sdk-providers/cohere) | Type: Conceptual | Summary: Learn how to use the Cohere provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Deepgram](/v5/providers/ai-sdk-providers/deepgram) | Type: Conceptual | Summary: Learn how to use the Deepgram provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra) | Type: Conceptual | Summary: Learn how to use DeepInfra's models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [DeepSeek](/v5/providers/ai-sdk-providers/deepseek) | Type: Conceptual | Summary: Learn how to use DeepSeek's models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [ElevenLabs](/v5/providers/ai-sdk-providers/elevenlabs) | Type: Conceptual | Summary: Learn how to use the ElevenLabs provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Fal](/v5/providers/ai-sdk-providers/fal) | Type: Conceptual | Summary: Learn how to use Fal AI models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Fireworks](/v5/providers/ai-sdk-providers/fireworks) | Type: Conceptual | Summary: Learn how to use Fireworks models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Gladia](/v5/providers/ai-sdk-providers/gladia) | Type: Conceptual | Summary: Learn how to use the Gladia provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [GMI Cloud](/v5/providers/ai-sdk-providers/gmicloud) | Type: Conceptual | Summary: Learn how to use GMI Cloud's models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | Type: Conceptual | Summary: Learn how to use Google Generative AI Provider. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Google Vertex AI](/v5/providers/ai-sdk-providers/google-vertex) | Type: Conceptual | Summary: Learn how to use the Google Vertex AI provider. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Groq](/v5/providers/ai-sdk-providers/groq) | Type: Conceptual | Summary: Learn how to use Groq. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Hugging Face](/v5/providers/ai-sdk-providers/huggingface) | Type: Conceptual | Summary: Learn how to use Hugging Face Provider. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Hume](/v5/providers/ai-sdk-providers/hume) | Type: Conceptual | Summary: Learn how to use the Hume provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Luma](/v5/providers/ai-sdk-providers/luma) | Type: Conceptual | Summary: Learn how to use Luma AI models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Mistral AI](/v5/providers/ai-sdk-providers/mistral) | Type: Conceptual | Summary: Learn how to use Mistral. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Moonshot AI](/v5/providers/ai-sdk-providers/moonshotai) | Type: Conceptual | Summary: Learn how to use Moonshot AI models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [OpenAI](/v5/providers/ai-sdk-providers/openai) | Type: Conceptual | Summary: Learn how to use the OpenAI provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Perplexity](/v5/providers/ai-sdk-providers/perplexity) | Type: Conceptual | Summary: Learn how to use Perplexity's Sonar API with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Replicate](/v5/providers/ai-sdk-providers/replicate) | Type: Conceptual | Summary: Learn how to use Replicate models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Rev.ai](/v5/providers/ai-sdk-providers/revai) | Type: Conceptual | Summary: Learn how to use the Rev.ai provider for the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Together.ai](/v5/providers/ai-sdk-providers/togetherai) | Type: Conceptual | Summary: Learn how to use Together.ai's models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Vercel](/v5/providers/ai-sdk-providers/vercel) | Type: Conceptual | Summary: Learn how to use Vercel's v0 models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [xAI Grok](/v5/providers/ai-sdk-providers/xai) | Type: Conceptual | Summary: Learn how to use xAI Grok. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

    - [Z.AI](/v5/providers/ai-sdk-providers/zai) | Type: Conceptual | Summary: Learn how to use Z.AI's GLM models with the AI SDK. | Prerequisites: /v5/providers/ai-sdk-providers | Topics: v5, providers, ai-sdk-providers

- [Community Providers](/v5/providers/community-providers) | Type: Conceptual | Summary: Learn how to use Language Model Specification. | Topics: v5, providers, community-providers

    - [A2A](/v5/providers/community-providers/a2a) | Type: Conceptual | Summary: A2A Protocol Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [ACP (Agent Client Protocol)](/v5/providers/community-providers/acp) | Type: Conceptual | Summary: ACP Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Aihubmix](/v5/providers/community-providers/aihubmix) | Type: Conceptual | Summary: Learn how to use Aihubmix with the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [AI/ML API](/v5/providers/community-providers/aimlapi) | Type: Conceptual | Summary: Learn how to use the AI/ML API provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Anthropic Vertex](/v5/providers/community-providers/anthropic-vertex-ai) | Type: Conceptual | Summary: Learn how to use the Anthropic Vertex provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Automatic1111](/v5/providers/community-providers/automatic1111) | Type: Conceptual | Summary: Automatic1111 Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Azure AI](/v5/providers/community-providers/azure-ai) | Type: Conceptual | Summary: Learn how to use the @quail-ai/azure-ai-provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Built-in AI](/v5/providers/community-providers/built-in-ai) | Type: Conceptual | Summary: Learn how to use the Built-in AI provider (browser models) for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Claude Code](/v5/providers/community-providers/claude-code) | Type: Conceptual | Summary: Learn how to use the Claude Code community provider to access Claude through your Pro/Max subscription. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Cloudflare AI Gateway](/v5/providers/community-providers/cloudflare-ai-gateway) | Type: Conceptual | Summary: Learn how to use the Cloudflare AI Gateway provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Cloudflare Workers AI](/v5/providers/community-providers/cloudflare-workers-ai) | Type: Conceptual | Summary: Learn how to use the Cloudflare Workers AI provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Crosshatch](/v5/providers/community-providers/crosshatch) | Type: Conceptual | Summary: Learn how to use the Crosshatch provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Writing a Custom Provider](/v5/providers/community-providers/custom-providers) | Type: Conceptual | Summary: Learn how to write a custom provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Dify](/v5/providers/community-providers/dify) | Type: Conceptual | Summary: Learn how to use the Dify provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [FriendliAI](/v5/providers/community-providers/friendliai) | Type: Conceptual | Summary: Learn how to use the FriendliAI Provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Gemini CLI](/v5/providers/community-providers/gemini-cli) | Type: Conceptual | Summary: Learn how to use the Gemini CLI community provider to access Google's Gemini models through the official CLI/SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Helicone](/v5/providers/community-providers/helicone) | Type: Conceptual | Summary: Helicone Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Inflection AI](/v5/providers/community-providers/inflection-ai) | Type: Conceptual | Summary: Learn how to use the unofficial Inflection AI provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Jina AI](/v5/providers/community-providers/jina-ai) | Type: Conceptual | Summary: Learn how to use the Jina AI provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [LangDB](/v5/providers/community-providers/langdb) | Type: Conceptual | Summary: Learn how to use LangDB with the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Letta](/v5/providers/community-providers/letta) | Type: Conceptual | Summary: Learn how to use the Letta provider with the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [MCP Sampling AI Provider](/v5/providers/community-providers/mcp-sampling) | Type: Conceptual | Summary: Learn how to use the MCP Sampling AI Provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Mem0](/v5/providers/community-providers/mem0) | Type: Conceptual | Summary: Learn how to use the Mem0 AI SDK provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [MiniMax](/v5/providers/community-providers/minimax) | Type: Conceptual | Summary: Learn how to use MiniMax provider with the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Mixedbread](/v5/providers/community-providers/mixedbread) | Type: Conceptual | Summary: Learn how to use the Mixedbread provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Ollama](/v5/providers/community-providers/ollama) | Type: Conceptual | Summary: Learn how to use the Ollama provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [OpenRouter](/v5/providers/community-providers/openrouter) | Type: Conceptual | Summary: OpenRouter Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Portkey](/v5/providers/community-providers/portkey) | Type: Conceptual | Summary: Learn how to use the Portkey provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Qwen](/v5/providers/community-providers/qwen) | Type: Conceptual | Summary: Learn how to use the Qwen provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [React Native Apple](/v5/providers/community-providers/react-native-apple) | Type: Conceptual | Summary: Learn how to use the Apple provider for on-device AI. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Requesty](/v5/providers/community-providers/requesty) | Type: Conceptual | Summary: Requesty Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [SambaNova](/v5/providers/community-providers/sambanova) | Type: Conceptual | Summary: Learn how to use the SambaNova provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [SAP AI Core](/v5/providers/community-providers/sap-ai) | Type: Conceptual | Summary: SAP AI Core Provider for the AI SDK | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Sarvam](/v5/providers/community-providers/sarvam) | Type: Conceptual | Summary: Learn how to use the Sarvam AI provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Spark](/v5/providers/community-providers/spark) | Type: Conceptual | Summary: Learn how to use the Spark provider for the AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Supermemory](/v5/providers/community-providers/supermemory) | Type: Conceptual | Summary: Learn how to use the Supermemory AI SDK provider for the Vercel AI SDK. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Voyage AI](/v5/providers/community-providers/voyage-ai) | Type: Conceptual | Summary: Learn how to use the Voyage AI provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

    - [Zhipu AI](/v5/providers/community-providers/zhipu) | Type: Conceptual | Summary: Learn how to use the Zhipu provider. | Prerequisites: /v5/providers/community-providers | Topics: v5, providers, community-providers

- [Observability Integrations](/v5/providers/observability) | Type: Conceptual | Summary: AI SDK Integration for monitoring and tracing LLM applications | Topics: v5, providers, observability

    - [Axiom](/v5/providers/observability/axiom) | Type: Conceptual | Summary: Measure, observe, and improve your AI SDK application with Axiom | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Braintrust](/v5/providers/observability/braintrust) | Type: Conceptual | Summary: Monitoring and tracing LLM applications with Braintrust | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Helicone](/v5/providers/observability/helicone) | Type: Conceptual | Summary: Monitor and optimize your AI SDK applications with minimal configuration using Helicone | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Laminar](/v5/providers/observability/laminar) | Type: Conceptual | Summary: Monitor your AI SDK applications with Laminar | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Langfuse](/v5/providers/observability/langfuse) | Type: Conceptual | Summary: Monitor, evaluate and debug your AI SDK application with Langfuse | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [LangSmith](/v5/providers/observability/langsmith) | Type: Conceptual | Summary: Monitor and evaluate your AI SDK application with LangSmith | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [LangWatch](/v5/providers/observability/langwatch) | Type: Conceptual | Summary: Track, monitor, guardrail and evaluate your AI SDK applications with LangWatch. | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Maxim](/v5/providers/observability/maxim) | Type: Conceptual | Summary: Evaluate & Observe LLM applications with Maxim | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Patronus](/v5/providers/observability/patronus) | Type: Conceptual | Summary: Monitor, evaluate and debug your AI SDK application with Patronus | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Scorecard](/v5/providers/observability/scorecard) | Type: Conceptual | Summary: Monitoring and evaluating LLM applications with Scorecard | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [SigNoz](/v5/providers/observability/signoz) | Type: Conceptual | Summary: Monitor, obeserve and debug your AI SDK application with SigNoz | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Traceloop](/v5/providers/observability/traceloop) | Type: Conceptual | Summary: Monitoring and evaluating LLM applications with Traceloop | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

    - [Weave](/v5/providers/observability/weave) | Type: Conceptual | Summary: Monitor and evaluate LLM applications with Weave. | Prerequisites: /v5/providers/observability | Topics: v5, providers, observability

- [OpenAI Compatible Providers](/v5/providers/openai-compatible-providers) | Type: Conceptual | Summary: Use OpenAI compatible providers with the AI SDK. | Topics: v5, providers, openai-compatible-providers

    - [Clarifai](/v5/providers/openai-compatible-providers/clarifai) | Type: Conceptual | Summary: Use Clarifai OpenAI compatible API with the AI SDK. | Prerequisites: /v5/providers/openai-compatible-providers | Topics: v5, providers, openai-compatible-providers

    - [Writing a Custom Provider](/v5/providers/openai-compatible-providers/custom-providers) | Type: Conceptual | Summary: Create a custom provider package for an OpenAI-compatible provider leveraging the AI SDK OpenAI Compatible package. | Prerequisites: /v5/providers/openai-compatible-providers | Topics: v5, providers, openai-compatible-providers

    - [Heroku](/v5/providers/openai-compatible-providers/heroku) | Type: Conceptual | Summary: Use a Heroku OpenAI compatible API with the AI SDK. | Prerequisites: /v5/providers/openai-compatible-providers | Topics: v5, providers, openai-compatible-providers

    - [LM Studio](/v5/providers/openai-compatible-providers/lmstudio) | Type: Conceptual | Summary: Use the LM Studio OpenAI compatible API with the AI SDK. | Prerequisites: /v5/providers/openai-compatible-providers | Topics: v5, providers, openai-compatible-providers

    - [ModelRush](/v5/providers/openai-compatible-providers/modelrush) | Type: Conceptual | Summary: Use the ModelRush OpenAI compatible API with the AI SDK. | Prerequisites: /v5/providers/openai-compatible-providers | Topics: v5, providers, openai-compatible-providers

    - [NVIDIA NIM](/v5/providers/openai-compatible-providers/nim) | Type: Conceptual | Summary: Use NVIDIA NIM OpenAI compatible API with the AI SDK. | Prerequisites: /v5/providers/openai-compatible-providers | Topics: v5, providers, openai-compatible-providers

## Cookbook

- [Express](/v5/cookbook/api-servers/express) | Type: Conceptual | Summary: Learn how to use the AI SDK in an Express server | Topics: v5, cookbook, api-servers

- [Fastify](/v5/cookbook/api-servers/fastify) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Fastify server | Topics: v5, cookbook, api-servers

- [Hono](/v5/cookbook/api-servers/hono) | Type: Conceptual | Summary: Example of using the AI SDK in a Hono server. | Topics: v5, cookbook, api-servers

- [Nest.js](/v5/cookbook/api-servers/nest) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Nest.js server | Topics: v5, cookbook, api-servers

- [Node.js HTTP Server](/v5/cookbook/api-servers/node-http-server) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Node.js HTTP server | Topics: v5, cookbook, api-servers

- [Guides](/v5/cookbook/guides) | Type: Conceptual | Summary: Learn how to build AI applications with the AI SDK | Topics: v5, cookbook, guides

    - [Get started with Claude 4](/v5/cookbook/guides/claude-4) | Type: Guide | Summary: Get started with Claude 4 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with Computer Use](/v5/cookbook/guides/computer-use) | Type: Guide | Summary: Get started with Claude's Computer Use capabilities with the AI SDK | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with DeepSeek V3.2](/v5/cookbook/guides/deepseek-v3-2) | Type: Guide | Summary: Get started with DeepSeek V3.2 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with Gemini 3](/v5/cookbook/guides/gemini) | Type: Guide | Summary: Get started with Gemini 3 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Google Gemini Image Generation](/v5/cookbook/guides/google-gemini-image-generation) | Type: Guide | Summary: Generate and edit images with Google Gemini 2.5 Flash Image using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with GPT-5](/v5/cookbook/guides/gpt-5) | Type: Guide | Summary: Get started with GPT-5 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with Llama 3.1](/v5/cookbook/guides/llama-3_1) | Type: Guide | Summary: Get started with Llama 3.1 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Multi-Modal Agent](/v5/cookbook/guides/multi-modal-chatbot) | Type: Guide | Summary: Learn how to build a multi-modal agent that can process images and PDFs with the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Natural Language Postgres](/v5/cookbook/guides/natural-language-postgres) | Type: Guide | Summary: Learn how to build a Next.js app that lets you talk to a PostgreSQL database in natural language. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with OpenAI o1](/v5/cookbook/guides/o1) | Type: Guide | Summary: Get started with OpenAI o1 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with OpenAI o3-mini](/v5/cookbook/guides/o3) | Type: Guide | Summary: Get started with OpenAI o3-mini using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [OpenAI Responses API](/v5/cookbook/guides/openai-responses) | Type: Guide | Summary: Get started with the OpenAI Responses API using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with DeepSeek R1](/v5/cookbook/guides/r1) | Type: Guide | Summary: Get started with DeepSeek R1 using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [RAG Agent](/v5/cookbook/guides/rag-chatbot) | Type: Guide | Summary: Learn how to build a RAG Agent with the AI SDK and Next.js | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Slackbot Agent Guide](/v5/cookbook/guides/slackbot) | Type: Guide | Summary: Learn how to use the AI SDK to build an AI Agent in Slack. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

    - [Get started with Claude 3.7 Sonnet](/v5/cookbook/guides/sonnet-3-7) | Type: Guide | Summary: Get started with Claude 3.7 Sonnet using the AI SDK. | Prerequisites: /v5/cookbook/guides | Topics: v5, cookbook, guides

- [Caching Middleware](/v5/cookbook/next/caching-middleware) | Type: Conceptual | Summary: Learn how to create a caching middleware with Next.js and KV. | Topics: v5, cookbook, next

- [Call Tools](/v5/cookbook/next/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Call Tools in Multiple Steps](/v5/cookbook/next/call-tools-multiple-steps) | Type: Conceptual | Summary: Learn how to call tools in multiple steps using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Chat with PDFs](/v5/cookbook/next/chat-with-pdf) | Type: Conceptual | Summary: Learn how to build a chatbot that can understand PDFs using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Streaming with Custom Format](/v5/cookbook/next/custom-stream-format) | Type: Conceptual | Summary: Build a custom format to stream LLM responses | Topics: v5, cookbook, next

- [Generate Image with Chat Prompt](/v5/cookbook/next/generate-image-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate an image with a chat prompt using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Generate Object](/v5/cookbook/next/generate-object) | Type: Conceptual | Summary: Learn how to generate object using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Generate Object with File Prompt through Form Submission](/v5/cookbook/next/generate-object-with-file-prompt) | Type: Conceptual | Summary: Learn how to generate object with file prompt through form submission using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Generate Text](/v5/cookbook/next/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Next.js. | Topics: v5, cookbook, next

- [Generate Text with Chat Prompt](/v5/cookbook/next/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Human-in-the-Loop Agent with Next.js](/v5/cookbook/next/human-in-the-loop) | Type: Conceptual | Summary: Add a human approval step to your agentic system with Next.js and the AI SDK | Topics: v5, cookbook, next

- [Markdown Chatbot with Memoization](/v5/cookbook/next/markdown-chatbot-with-memoization) | Type: Conceptual | Summary: Build a chatbot that renders and memoizes Markdown responses with Next.js and the AI SDK. | Topics: v5, cookbook, next

- [Model Context Protocol (MCP) Tools](/v5/cookbook/next/mcp-tools) | Type: Conceptual | Summary: Learn how to use MCP tools with the AI SDK and Next.js | Topics: v5, cookbook, next

- [Render Visual Interface in Chat](/v5/cookbook/next/render-visual-interface-in-chat) | Type: Conceptual | Summary: Learn how to render visual interfaces in chat using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Send Custom Body from useChat](/v5/cookbook/next/send-custom-body-from-use-chat) | Type: Conceptual | Summary: Learn how to send a custom body from the useChat hook using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Stream Object](/v5/cookbook/next/stream-object) | Type: Conceptual | Summary: Learn how to stream object using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Stream Text](/v5/cookbook/next/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and Next.js | Topics: v5, cookbook, next

- [streamText Multi-Step Cookbook](/v5/cookbook/next/stream-text-multistep) | Type: Conceptual | Summary: Learn how to create several streamText steps with different settings | Topics: v5, cookbook, next

- [Stream Text with Chat Prompt](/v5/cookbook/next/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Stream Text with Image Prompt](/v5/cookbook/next/stream-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream text with an image prompt using the AI SDK and Next.js | Topics: v5, cookbook, next

- [Share useChat State Across Components](/v5/cookbook/next/use-shared-chat-context) | Type: Conceptual | Summary: Learn how to share a chat instance across multiple components with useChat and easily reset the chat. | Topics: v5, cookbook, next

- [Call Tools](/v5/cookbook/node/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and Node | Topics: v5, cookbook, node

- [Call Tools in Multiple Steps](/v5/cookbook/node/call-tools-multiple-steps) | Type: Conceptual | Summary: Learn how to call tools with multiple steps using the AI SDK and Node | Topics: v5, cookbook, node

- [Call Tools with Image Prompt](/v5/cookbook/node/call-tools-with-image-prompt) | Type: Conceptual | Summary: Learn how to call tools with image prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Embed Text](/v5/cookbook/node/embed-text) | Type: Conceptual | Summary: Learn how to embed text using the AI SDK and Node | Topics: v5, cookbook, node

- [Embed Text in Batch](/v5/cookbook/node/embed-text-batch) | Type: Conceptual | Summary: Learn how to embed multiple text using the AI SDK and Node | Topics: v5, cookbook, node

- [Generate Object](/v5/cookbook/node/generate-object) | Type: Conceptual | Summary: Learn how to generate structured data using the AI SDK and Node | Topics: v5, cookbook, node

- [Generate Object with a Reasoning Model](/v5/cookbook/node/generate-object-reasoning) | Type: Conceptual | Summary: Learn how to generate structured data with a reasoning model using the AI SDK and Node | Topics: v5, cookbook, node

- [Generate Text](/v5/cookbook/node/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Node | Topics: v5, cookbook, node

- [Generate Text with Chat Prompt](/v5/cookbook/node/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Generate Text with Image Prompt](/v5/cookbook/node/generate-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to generate text with image prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Intercepting Fetch Requests](/v5/cookbook/node/intercept-fetch-requests) | Type: Conceptual | Summary: Learn how to intercept fetch requests using the AI SDK and Node | Topics: v5, cookbook, node

- [Knowledge Base Agent](/v5/cookbook/node/knowledge-base-agent) | Type: Conceptual | Summary: Build an AI agent that can read from and write to a knowledge base using Upstash Search and the AI SDK | Topics: v5, cookbook, node

- [Local Caching Middleware](/v5/cookbook/node/local-caching-middleware) | Type: Conceptual | Summary: Learn how to create a caching middleware for local development. | Topics: v5, cookbook, node

- [Manual Agent Loop](/v5/cookbook/node/manual-agent-loop) | Type: Conceptual | Summary: Learn how to create your own agentic loop with full control over tool execution | Topics: v5, cookbook, node

- [Model Context Protocol (MCP) Elicitation](/v5/cookbook/node/mcp-elicitation) | Type: Conceptual | Summary: Learn how to handle elicitation requests from MCP servers with the AI SDK | Topics: v5, cookbook, node

- [Model Context Protocol (MCP) Tools](/v5/cookbook/node/mcp-tools) | Type: Conceptual | Summary: Learn how to use MCP tools with the AI SDK and Node | Topics: v5, cookbook, node

- [Retrieval Augmented Generation](/v5/cookbook/node/retrieval-augmented-generation) | Type: Conceptual | Summary: Learn how to use retrieval augmented generation using the AI SDK and Node | Topics: v5, cookbook, node

- [Stream Object](/v5/cookbook/node/stream-object) | Type: Conceptual | Summary: Learn how to stream structured data using the AI SDK and Node | Topics: v5, cookbook, node

- [Record Final Object after Streaming Object](/v5/cookbook/node/stream-object-record-final-object) | Type: Conceptual | Summary: Learn how to record the final object after streaming an object using the AI SDK and Node | Topics: v5, cookbook, node

- [Record Token Usage After Streaming Object](/v5/cookbook/node/stream-object-record-token-usage) | Type: Conceptual | Summary: Learn how to record token usage when streaming structured data using the AI SDK and Node | Topics: v5, cookbook, node

- [Stream Object with Image Prompt](/v5/cookbook/node/stream-object-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream structured data with an image prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Stream Text](/v5/cookbook/node/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and Node | Topics: v5, cookbook, node

- [Stream Text with Chat Prompt](/v5/cookbook/node/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to stream text with chat prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Stream Text with File Prompt](/v5/cookbook/node/stream-text-with-file-prompt) | Type: Conceptual | Summary: Learn how to stream text with file prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Stream Text with Image Prompt](/v5/cookbook/node/stream-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream text with image prompt using the AI SDK and Node | Topics: v5, cookbook, node

- [Web Search Agent](/v5/cookbook/node/web-search-agent) | Type: Conceptual | Summary: Learn how to build an agent that has access to web with the AI SDK and Node | Topics: v5, cookbook, node

- [Call Tools](/v5/cookbook/rsc/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Call Tools in Parallel](/v5/cookbook/rsc/call-tools-in-parallel) | Type: Conceptual | Summary: Learn how to tools in parallel text using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Generate Object](/v5/cookbook/rsc/generate-object) | Type: Conceptual | Summary: Learn how to generate object using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Generate Text](/v5/cookbook/rsc/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Generate Text with Chat Prompt](/v5/cookbook/rsc/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Render Visual Interface in Chat](/v5/cookbook/rsc/render-visual-interface-in-chat) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Restore Messages From Database](/v5/cookbook/rsc/restore-messages-from-database) | Type: Conceptual | Summary: Learn how to restore messages from an external database using the AI SDK and React Server Components | Topics: v5, cookbook, rsc

- [Save Messages To Database](/v5/cookbook/rsc/save-messages-to-database) | Type: Conceptual | Summary: Learn how to save messages to an external database using the AI SDK and React Server Components | Topics: v5, cookbook, rsc

- [Stream Object](/v5/cookbook/rsc/stream-object) | Type: Conceptual | Summary: Learn how to stream object using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Stream Text](/v5/cookbook/rsc/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Stream Text with Chat Prompt](/v5/cookbook/rsc/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to stream text with chat prompt using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc

- [Record Token Usage after Streaming User Interfaces](/v5/cookbook/rsc/stream-ui-record-token-usage) | Type: Conceptual | Summary: Learn how to record token usage after streaming user interfaces using the AI SDK and React Server Components | Topics: v5, cookbook, rsc

- [Stream Updates to Visual Interfaces](/v5/cookbook/rsc/stream-updates-to-visual-interfaces) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: v5, cookbook, rsc