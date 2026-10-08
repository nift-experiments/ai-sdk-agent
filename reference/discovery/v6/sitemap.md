# AI SDK v6 documentation

## Purpose

This file is a high-level semantic index of the documentation.
It is intended for:

- LLM-assisted navigation (ChatGPT, Claude, etc.)
- Quick orientation for contributors
- Identifying relevant documentation areas during development

It is not intended to replace individual docs.

---

## Documentation

- [Advanced](/v6/docs/advanced) | Type: Conceptual | Summary: Learn how to use advanced functionality within the AI SDK and RSC API. | Topics: v6, docs, advanced

    - [Backpressure](/v6/docs/advanced/backpressure) | Type: Conceptual | Summary: How to handle backpressure and cancellation when working with the AI SDK | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Caching](/v6/docs/advanced/caching) | Type: Conceptual | Summary: How to handle caching when working with the AI SDK | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Language Models as Routers](/v6/docs/advanced/model-as-router) | Type: Conceptual | Summary: Generative User Interfaces and Language Models as Routers | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Multiple Streamables](/v6/docs/advanced/multiple-streamables) | Type: Conceptual | Summary: Learn to handle multiple streamables in your application. | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Multistep Interfaces](/v6/docs/advanced/multistep-interfaces) | Type: Conceptual | Summary: Concepts behind building multistep interfaces | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Prompt Engineering](/v6/docs/advanced/prompt-engineering) | Type: Conceptual | Summary: Learn how to engineer prompts for LLMs with the AI SDK | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Rate Limiting](/v6/docs/advanced/rate-limiting) | Type: Conceptual | Summary: Learn how to rate limit your application. | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Rendering UI with Language Models](/v6/docs/advanced/rendering-ui-with-language-models) | Type: Conceptual | Summary: Rendering UI with Language Models | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Sequential Generations](/v6/docs/advanced/sequential-generations) | Type: Conceptual | Summary: Learn how to implement sequential generations ("chains") with the AI SDK | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Stopping Streams](/v6/docs/advanced/stopping-streams) | Type: Conceptual | Summary: Learn how to cancel streams with the AI SDK | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

    - [Vercel Deployment Guide](/v6/docs/advanced/vercel-deployment-guide) | Type: Conceptual | Summary: Learn how to deploy an AI application to production on Vercel | Prerequisites: /v6/docs/advanced | Topics: v6, docs, advanced

- [Building Agents](/v6/docs/agents/building-agents) | Type: Conceptual | Summary: Complete guide to creating agents with the ToolLoopAgent. | Topics: v6, docs, agents

- [Configuring Call Options](/v6/docs/agents/configuring-call-options) | Type: Conceptual | Summary: Pass type-safe runtime inputs to dynamically configure agent behavior. | Topics: v6, docs, agents

- [Loop Control](/v6/docs/agents/loop-control) | Type: Conceptual | Summary: Control agent execution with built-in loop management using stopWhen and prepareStep | Topics: v6, docs, agents

- [Memory](/v6/docs/agents/memory) | Type: Conceptual | Summary: Add persistent memory to your agent using provider-defined tools, memory providers, or a custom tool. | Topics: v6, docs, agents

- [Overview](/v6/docs/agents/overview) | Type: Conceptual | Summary: Learn how to build agents with the AI SDK. | Topics: v6, docs, agents

- [Subagents](/v6/docs/agents/subagents) | Type: Conceptual | Summary: Delegate context-heavy tasks to specialized subagents while keeping the main agent focused. | Topics: v6, docs, agents

- [Workflow Patterns](/v6/docs/agents/workflows) | Type: Conceptual | Summary: Learn workflow patterns for building reliable agents with the AI SDK. | Topics: v6, docs, agents

- [DevTools](/v6/docs/ai-sdk-core/devtools) | Type: Conceptual | Summary: Debug and inspect AI SDK applications with DevTools | Topics: v6, docs, ai-sdk-core

- [Embeddings](/v6/docs/ai-sdk-core/embeddings) | Type: Conceptual | Summary: Learn how to embed values with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Error Handling](/v6/docs/ai-sdk-core/error-handling) | Type: Conceptual | Summary: Learn how to handle errors in the AI SDK Core | Topics: v6, docs, ai-sdk-core

- [Event Callbacks](/v6/docs/ai-sdk-core/event-listeners) | Type: Conceptual | Summary: Subscribe to lifecycle events in generateText and streamText calls | Topics: v6, docs, ai-sdk-core

- [Generating Structured Data](/v6/docs/ai-sdk-core/generating-structured-data) | Type: Conceptual | Summary: Learn how to generate structured data with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Generating Text](/v6/docs/ai-sdk-core/generating-text) | Type: Conceptual | Summary: Learn how to generate text with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Image Generation](/v6/docs/ai-sdk-core/image-generation) | Type: Conceptual | Summary: Learn how to generate images with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Model Context Protocol (MCP)](/v6/docs/ai-sdk-core/mcp-tools) | Type: Conceptual | Summary: Learn how to connect to Model Context Protocol (MCP) servers and use their tools with AI SDK Core. | Topics: v6, docs, ai-sdk-core

- [Language Model Middleware](/v6/docs/ai-sdk-core/middleware) | Type: Conceptual | Summary: Learn how to use middleware to enhance the behavior of language models | Topics: v6, docs, ai-sdk-core

- [Overview](/v6/docs/ai-sdk-core/overview) | Type: Conceptual | Summary: An overview of AI SDK Core. | Topics: v6, docs, ai-sdk-core

- [Prompt Engineering](/v6/docs/ai-sdk-core/prompt-engineering) | Type: Conceptual | Summary: Learn how to develop prompts with AI SDK Core. | Topics: v6, docs, ai-sdk-core

- [Provider & Model Management](/v6/docs/ai-sdk-core/provider-management) | Type: Conceptual | Summary: Learn how to work with multiple providers and models | Topics: v6, docs, ai-sdk-core

- [Reranking](/v6/docs/ai-sdk-core/reranking) | Type: Conceptual | Summary: Learn how to rerank documents with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Settings](/v6/docs/ai-sdk-core/settings) | Type: Conceptual | Summary: Learn how to configure the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Speech](/v6/docs/ai-sdk-core/speech) | Type: Conceptual | Summary: Learn how to generate speech from text with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Telemetry](/v6/docs/ai-sdk-core/telemetry) | Type: Conceptual | Summary: Using OpenTelemetry with AI SDK Core | Topics: v6, docs, ai-sdk-core

- [Testing](/v6/docs/ai-sdk-core/testing) | Type: Conceptual | Summary: Learn how to use AI SDK Core mock providers for testing. | Topics: v6, docs, ai-sdk-core

- [Tool Calling](/v6/docs/ai-sdk-core/tools-and-tool-calling) | Type: Conceptual | Summary: Learn about tool calling and multi-step calls (using stopWhen) with AI SDK Core. | Topics: v6, docs, ai-sdk-core

- [Transcription](/v6/docs/ai-sdk-core/transcription) | Type: Conceptual | Summary: Learn how to transcribe audio with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Video Generation](/v6/docs/ai-sdk-core/video-generation) | Type: Conceptual | Summary: Learn how to generate videos with the AI SDK. | Topics: v6, docs, ai-sdk-core

- [Handling Authentication](/v6/docs/ai-sdk-rsc/authentication) | Type: Conceptual | Summary: Learn how to authenticate with the AI SDK. | Topics: v6, docs, ai-sdk-rsc

- [Error Handling](/v6/docs/ai-sdk-rsc/error-handling) | Type: Conceptual | Summary: Learn how to handle errors with the AI SDK. | Topics: v6, docs, ai-sdk-rsc

- [Managing Generative UI State](/v6/docs/ai-sdk-rsc/generative-ui-state) | Type: Conceptual | Summary: Overview of the AI and UI states | Topics: v6, docs, ai-sdk-rsc

- [Handling Loading State](/v6/docs/ai-sdk-rsc/loading-state) | Type: Conceptual | Summary: Overview of handling loading state with AI SDK RSC | Topics: v6, docs, ai-sdk-rsc

- [Migrating from RSC to UI](/v6/docs/ai-sdk-rsc/migrating-to-ui) | Type: Conceptual | Summary: Learn how to migrate from AI SDK RSC to AI SDK UI. | Topics: v6, docs, ai-sdk-rsc

- [Multistep Interfaces](/v6/docs/ai-sdk-rsc/multistep-interfaces) | Type: Conceptual | Summary: Overview of Building Multistep Interfaces with AI SDK RSC | Topics: v6, docs, ai-sdk-rsc

- [Overview](/v6/docs/ai-sdk-rsc/overview) | Type: Conceptual | Summary: An overview of AI SDK RSC. | Topics: v6, docs, ai-sdk-rsc

- [Saving and Restoring States](/v6/docs/ai-sdk-rsc/saving-and-restoring-states) | Type: Conceptual | Summary: Saving and restoring AI and UI states with onGetUIState and onSetAIState | Topics: v6, docs, ai-sdk-rsc

- [Streaming React Components](/v6/docs/ai-sdk-rsc/streaming-react-components) | Type: Conceptual | Summary: Overview of streaming RSCs | Topics: v6, docs, ai-sdk-rsc

- [Streaming Values](/v6/docs/ai-sdk-rsc/streaming-values) | Type: Conceptual | Summary: Overview of streaming RSCs | Topics: v6, docs, ai-sdk-rsc

- [Chatbot](/v6/docs/ai-sdk-ui/chatbot) | Type: Conceptual | Summary: Learn how to use the useChat hook. | Topics: v6, docs, ai-sdk-ui

- [Chatbot Message Persistence](/v6/docs/ai-sdk-ui/chatbot-message-persistence) | Type: Conceptual | Summary: Learn how to store and load chat messages in a chatbot. | Topics: v6, docs, ai-sdk-ui

- [Chatbot Resume Streams](/v6/docs/ai-sdk-ui/chatbot-resume-streams) | Type: Conceptual | Summary: Learn how to resume chatbot streams after client disconnects. | Topics: v6, docs, ai-sdk-ui

- [Chatbot Tool Usage](/v6/docs/ai-sdk-ui/chatbot-tool-usage) | Type: Conceptual | Summary: Learn how to use tools with the useChat hook. | Topics: v6, docs, ai-sdk-ui

- [Completion](/v6/docs/ai-sdk-ui/completion) | Type: Conceptual | Summary: Learn how to use the useCompletion hook. | Topics: v6, docs, ai-sdk-ui

- [Error Handling](/v6/docs/ai-sdk-ui/error-handling) | Type: Conceptual | Summary: Learn how to handle errors in the AI SDK UI | Topics: v6, docs, ai-sdk-ui

- [Generative User Interfaces](/v6/docs/ai-sdk-ui/generative-user-interfaces) | Type: Conceptual | Summary: Learn how to build Generative UI with AI SDK UI. | Topics: v6, docs, ai-sdk-ui

- [Message Metadata](/v6/docs/ai-sdk-ui/message-metadata) | Type: Conceptual | Summary: Learn how to attach and use metadata with messages in AI SDK UI | Topics: v6, docs, ai-sdk-ui

- [Object Generation](/v6/docs/ai-sdk-ui/object-generation) | Type: Conceptual | Summary: Learn how to use the useObject hook. | Topics: v6, docs, ai-sdk-ui

- [Overview](/v6/docs/ai-sdk-ui/overview) | Type: Conceptual | Summary: An overview of AI SDK UI. | Topics: v6, docs, ai-sdk-ui

- [Reading UIMessage Streams](/v6/docs/ai-sdk-ui/reading-ui-message-streams) | Type: Conceptual | Summary: Learn how to read UIMessage streams. | Topics: v6, docs, ai-sdk-ui

- [Stream Protocols](/v6/docs/ai-sdk-ui/stream-protocol) | Type: Conceptual | Summary: Learn more about the supported stream protocols in the AI SDK. | Topics: v6, docs, ai-sdk-ui

- [Streaming Custom Data](/v6/docs/ai-sdk-ui/streaming-data) | Type: Conceptual | Summary: Learn how to stream custom data from the server to the client. | Topics: v6, docs, ai-sdk-ui

- [Transport](/v6/docs/ai-sdk-ui/transport) | Type: Conceptual | Summary: Learn how to use custom transports with useChat. | Topics: v6, docs, ai-sdk-ui

- [Overview](/v6/docs/foundations/overview) | Type: Conceptual | Summary: An overview of foundational concepts critical to understanding the AI SDK | Topics: v6, docs, foundations

- [Prompts](/v6/docs/foundations/prompts) | Type: Conceptual | Summary: Learn about the Prompt structure used in the AI SDK. | Topics: v6, docs, foundations

- [Provider Options](/v6/docs/foundations/provider-options) | Type: Conceptual | Summary: Learn how to use provider-specific options to control reasoning, caching, and other advanced features. | Topics: v6, docs, foundations

- [Providers and Models](/v6/docs/foundations/providers-and-models) | Type: Conceptual | Summary: Learn about the providers and models available in the AI SDK. | Topics: v6, docs, foundations

- [Streaming](/v6/docs/foundations/streaming) | Type: Conceptual | Summary: Why use streaming for AI applications? | Topics: v6, docs, foundations

- [Tools](/v6/docs/foundations/tools) | Type: Conceptual | Summary: Learn about tools with the AI SDK. | Topics: v6, docs, foundations

- [Getting Started](/v6/docs/getting-started) | Type: Guide | Summary: Welcome to the AI SDK documentation! | Topics: v6, docs, getting-started

    - [Choosing a Provider](/v6/docs/getting-started/choosing-a-provider) | Type: Guide | Summary: Learn how to configure and authenticate with AI providers in the AI SDK. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Coding Agents](/v6/docs/getting-started/coding-agents) | Type: Guide | Summary: Learn how to set up the AI SDK for use with coding agents, including installing skills, accessing bundled docs, and using DevTools. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Expo](/v6/docs/getting-started/expo) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Expo. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Navigating the Library](/v6/docs/getting-started/navigating-the-library) | Type: Guide | Summary: Learn how to navigate the AI SDK. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Next.js App Router](/v6/docs/getting-started/nextjs-app-router) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Next.js App Router. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Next.js Pages Router](/v6/docs/getting-started/nextjs-pages-router) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Next.js Pages Router. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Node.js](/v6/docs/getting-started/nodejs) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Node.js. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Vue.js (Nuxt)](/v6/docs/getting-started/nuxt) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Vue.js (Nuxt). | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [Svelte](/v6/docs/getting-started/svelte) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Svelte. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

    - [TanStack Start](/v6/docs/getting-started/tanstack-start) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and TanStack Start. | Prerequisites: /v6/docs/getting-started | Topics: v6, docs, getting-started

- [AI SDK by Vercel](/v6/docs/introduction) | Type: Conceptual | Summary: The AI SDK is the TypeScript toolkit for building AI applications and agents with React, Next.js, Vue, Svelte, Node.js, and more. | Topics: v6, docs, introduction

- [Migration Guides](/v6/docs/migration-guides) | Type: Conceptual | Summary: Learn how to upgrade between Vercel AI versions. | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 3.0 to 3.1](/v6/docs/migration-guides/migration-guide-3-1) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.0 to 3.1. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 3.1 to 3.2](/v6/docs/migration-guides/migration-guide-3-2) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.1 to 3.2. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 3.2 to 3.3](/v6/docs/migration-guides/migration-guide-3-3) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.2 to 3.3. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 3.3 to 3.4](/v6/docs/migration-guides/migration-guide-3-4) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.3 to 3.4. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 3.4 to 4.0](/v6/docs/migration-guides/migration-guide-4-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.4 to 4.0. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 4.0 to 4.1](/v6/docs/migration-guides/migration-guide-4-1) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.0 to 4.1. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 4.1 to 4.2](/v6/docs/migration-guides/migration-guide-4-2) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.1 to 4.2. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 4.x to 5.0](/v6/docs/migration-guides/migration-guide-5-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.x to 5.0. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate Your Data to AI SDK 5.0](/v6/docs/migration-guides/migration-guide-5-0-data) | Type: Conceptual | Summary: Learn how to migrate your persisted messages and chat data from AI SDK 4.x to 5.0. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Migrate AI SDK 5.x to 6.0](/v6/docs/migration-guides/migration-guide-6-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 5.x to 6.0. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

    - [Versioning](/v6/docs/migration-guides/versioning) | Type: Conceptual | Summary: Understand how the AI SDK approaches versioning. | Prerequisites: /v6/docs/migration-guides | Topics: v6, docs, migration-guides

- [Reference](/v6/docs/reference) | Type: Reference | Summary: Reference documentation for the AI SDK | Topics: v6, docs, reference

    - [AI SDK Core](/v6/docs/reference/ai-sdk-core) | Type: Reference | Summary: Reference documentation for the AI SDK Core | Prerequisites: /v6/docs/reference | Topics: v6, docs, reference

        - [addToolInputExamplesMiddleware](/v6/docs/reference/ai-sdk-core/add-tool-input-examples-middleware) | Type: Reference | Summary: Middleware that appends tool input examples to tool descriptions. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [Agent (Interface)](/v6/docs/reference/ai-sdk-core/agent) | Type: Reference | Summary: API Reference for the Agent interface. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [cosineSimilarity](/v6/docs/reference/ai-sdk-core/cosine-similarity) | Type: Reference | Summary: Calculate the cosine similarity between two vectors (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [createAgentUIStream](/v6/docs/reference/ai-sdk-core/create-agent-ui-stream) | Type: Reference | Summary: API Reference for the createAgentUIStream utility. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [createAgentUIStreamResponse](/v6/docs/reference/ai-sdk-core/create-agent-ui-stream-response) | Type: Reference | Summary: API Reference for the createAgentUIStreamResponse utility. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [createIdGenerator](/v6/docs/reference/ai-sdk-core/create-id-generator) | Type: Reference | Summary: Create a customizable unique identifier generator (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [createMCPClient](/v6/docs/reference/ai-sdk-core/create-mcp-client) | Type: Reference | Summary: Create a client for connecting to MCP servers | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [customProvider](/v6/docs/reference/ai-sdk-core/custom-provider) | Type: Reference | Summary: Custom provider that uses models from a different provider (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [DefaultGeneratedFile](/v6/docs/reference/ai-sdk-core/default-generated-file) | Type: Reference | Summary: API Reference for DefaultGeneratedFile. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [defaultSettingsMiddleware](/v6/docs/reference/ai-sdk-core/default-settings-middleware) | Type: Reference | Summary: Middleware that applies default settings for language models | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [dynamicTool](/v6/docs/reference/ai-sdk-core/dynamic-tool) | Type: Reference | Summary: Helper function for creating dynamic tools with unknown types | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [embed](/v6/docs/reference/ai-sdk-core/embed) | Type: Reference | Summary: API Reference for embed. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [embedMany](/v6/docs/reference/ai-sdk-core/embed-many) | Type: Reference | Summary: API Reference for embedMany. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [extractJsonMiddleware](/v6/docs/reference/ai-sdk-core/extract-json-middleware) | Type: Reference | Summary: Middleware that extracts JSON from text content by stripping markdown code fences | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [extractReasoningMiddleware](/v6/docs/reference/ai-sdk-core/extract-reasoning-middleware) | Type: Reference | Summary: Middleware that extracts XML-tagged reasoning sections from generated text | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [generateId](/v6/docs/reference/ai-sdk-core/generate-id) | Type: Reference | Summary: Generate a unique identifier (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [generateImage](/v6/docs/reference/ai-sdk-core/generate-image) | Type: Reference | Summary: API Reference for generateImage. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [generateSpeech](/v6/docs/reference/ai-sdk-core/generate-speech) | Type: Reference | Summary: API Reference for generateSpeech. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [generateText](/v6/docs/reference/ai-sdk-core/generate-text) | Type: Reference | Summary: API Reference for generateText. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [experimental_generateVideo](/v6/docs/reference/ai-sdk-core/generate-video) | Type: Reference | Summary: API Reference for experimental_generateVideo. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [hasToolCall](/v6/docs/reference/ai-sdk-core/has-tool-call) | Type: Reference | Summary: API Reference for hasToolCall. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [jsonSchema](/v6/docs/reference/ai-sdk-core/json-schema) | Type: Reference | Summary: Helper function for creating JSON schemas | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [LanguageModelV3Middleware](/v6/docs/reference/ai-sdk-core/language-model-v2-middleware) | Type: Reference | Summary: Middleware for enhancing language model behavior (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [isLoopFinished](/v6/docs/reference/ai-sdk-core/loop-finished) | Type: Reference | Summary: API Reference for isLoopFinished. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [Experimental_StdioMCPTransport](/v6/docs/reference/ai-sdk-core/mcp-stdio-transport) | Type: Reference | Summary: Create a transport for Model Context Protocol (MCP) clients to communicate with MCP servers using standard input and output streams | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [ModelMessage](/v6/docs/reference/ai-sdk-core/model-message) | Type: Reference | Summary: Message types for AI SDK Core (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [Output](/v6/docs/reference/ai-sdk-core/output) | Type: Reference | Summary: API Reference for Output. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [pipeAgentUIStreamToResponse](/v6/docs/reference/ai-sdk-core/pipe-agent-ui-stream-to-response) | Type: Reference | Summary: API Reference for the pipeAgentUIStreamToResponse utility. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [createProviderRegistry](/v6/docs/reference/ai-sdk-core/provider-registry) | Type: Reference | Summary: Registry for managing multiple providers and models (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [rerank](/v6/docs/reference/ai-sdk-core/rerank) | Type: Reference | Summary: API Reference for rerank. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [safeValidateUIMessages](/v6/docs/reference/ai-sdk-core/safe-validate-ui-messages) | Type: Reference | Summary: API Reference for safeValidateUIMessages | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [simulateReadableStream](/v6/docs/reference/ai-sdk-core/simulate-readable-stream) | Type: Reference | Summary: Create a ReadableStream that emits values with configurable delays | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [simulateStreamingMiddleware](/v6/docs/reference/ai-sdk-core/simulate-streaming-middleware) | Type: Reference | Summary: Middleware that simulates streaming for non-streaming language models | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [smoothStream](/v6/docs/reference/ai-sdk-core/smooth-stream) | Type: Reference | Summary: Stream transformer for smoothing text and reasoning output | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [stepCountIs](/v6/docs/reference/ai-sdk-core/step-count-is) | Type: Reference | Summary: API Reference for stepCountIs. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [streamText](/v6/docs/reference/ai-sdk-core/stream-text) | Type: Reference | Summary: API Reference for streamText. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [tool](/v6/docs/reference/ai-sdk-core/tool) | Type: Reference | Summary: Helper function for tool type inference | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [ToolLoopAgent](/v6/docs/reference/ai-sdk-core/tool-loop-agent) | Type: Reference | Summary: API Reference for the ToolLoopAgent class. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [transcribe](/v6/docs/reference/ai-sdk-core/transcribe) | Type: Reference | Summary: API Reference for transcribe. | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [UIMessage](/v6/docs/reference/ai-sdk-core/ui-message) | Type: Reference | Summary: API Reference for UIMessage | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [valibotSchema](/v6/docs/reference/ai-sdk-core/valibot-schema) | Type: Reference | Summary: Helper function for creating Valibot schemas | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [validateUIMessages](/v6/docs/reference/ai-sdk-core/validate-ui-messages) | Type: Reference | Summary: API Reference for validateUIMessages | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [wrapImageModel](/v6/docs/reference/ai-sdk-core/wrap-image-model) | Type: Reference | Summary: Function for wrapping an image model with middleware (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [wrapLanguageModel](/v6/docs/reference/ai-sdk-core/wrap-language-model) | Type: Reference | Summary: Function for wrapping a language model with middleware (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

        - [zodSchema](/v6/docs/reference/ai-sdk-core/zod-schema) | Type: Reference | Summary: Helper function for creating Zod schemas | Prerequisites: /v6/docs/reference/ai-sdk-core | Topics: v6, docs, reference

    - [AI SDK Errors](/v6/docs/reference/ai-sdk-errors) | Type: Reference | Summary: Reference for AI SDK error classes and typed error handling. | Prerequisites: /v6/docs/reference | Topics: v6, docs, reference

        - [AI_APICallError](/v6/docs/reference/ai-sdk-errors/ai-api-call-error) | Type: Reference | Summary: Learn how to fix AI_APICallError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_DownloadError](/v6/docs/reference/ai-sdk-errors/ai-download-error) | Type: Reference | Summary: Learn how to fix AI_DownloadError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_EmptyResponseBodyError](/v6/docs/reference/ai-sdk-errors/ai-empty-response-body-error) | Type: Reference | Summary: Learn how to fix AI_EmptyResponseBodyError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidArgumentError](/v6/docs/reference/ai-sdk-errors/ai-invalid-argument-error) | Type: Reference | Summary: Learn how to fix AI_InvalidArgumentError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidDataContentError](/v6/docs/reference/ai-sdk-errors/ai-invalid-data-content-error) | Type: Reference | Summary: How to fix AI_InvalidDataContentError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidMessageRoleError](/v6/docs/reference/ai-sdk-errors/ai-invalid-message-role-error) | Type: Reference | Summary: Learn how to fix AI_InvalidMessageRoleError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidPromptError](/v6/docs/reference/ai-sdk-errors/ai-invalid-prompt-error) | Type: Reference | Summary: Learn how to fix AI_InvalidPromptError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidResponseDataError](/v6/docs/reference/ai-sdk-errors/ai-invalid-response-data-error) | Type: Reference | Summary: Learn how to fix AI_InvalidResponseDataError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidToolApprovalError](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolApprovalError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidToolApprovalSignatureError](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-signature-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolApprovalSignatureError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_InvalidToolInputError](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolInputError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_JSONParseError](/v6/docs/reference/ai-sdk-errors/ai-json-parse-error) | Type: Reference | Summary: Learn how to fix AI_JSONParseError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_LoadAPIKeyError](/v6/docs/reference/ai-sdk-errors/ai-load-api-key-error) | Type: Reference | Summary: Learn how to fix AI_LoadAPIKeyError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_LoadSettingError](/v6/docs/reference/ai-sdk-errors/ai-load-setting-error) | Type: Reference | Summary: Learn how to fix AI_LoadSettingError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_MessageConversionError](/v6/docs/reference/ai-sdk-errors/ai-message-conversion-error) | Type: Reference | Summary: Learn how to fix AI_MessageConversionError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoContentGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-content-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoContentGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoImageGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-image-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoImageGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoObjectGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-object-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoObjectGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoOutputGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-output-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoOutputGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoSpeechGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-speech-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoSpeechGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoSuchModelError](/v6/docs/reference/ai-sdk-errors/ai-no-such-model-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchModelError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoSuchProviderError](/v6/docs/reference/ai-sdk-errors/ai-no-such-provider-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchProviderError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoSuchToolError](/v6/docs/reference/ai-sdk-errors/ai-no-such-tool-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchToolError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoTranscriptGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-transcript-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoTranscriptGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_NoVideoGeneratedError](/v6/docs/reference/ai-sdk-errors/ai-no-video-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoVideoGeneratedError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_RetryError](/v6/docs/reference/ai-sdk-errors/ai-retry-error) | Type: Reference | Summary: Learn how to fix AI_RetryError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_TooManyEmbeddingValuesForCallError](/v6/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error) | Type: Reference | Summary: Learn how to fix AI_TooManyEmbeddingValuesForCallError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_ToolCallNotFoundForApprovalError](/v6/docs/reference/ai-sdk-errors/ai-tool-call-not-found-for-approval-error) | Type: Reference | Summary: Learn how to fix AI_ToolCallNotFoundForApprovalError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [ToolCallRepairError](/v6/docs/reference/ai-sdk-errors/ai-tool-call-repair-error) | Type: Reference | Summary: Learn how to fix AI SDK ToolCallRepairError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_ToolChoiceViolationError](/v6/docs/reference/ai-sdk-errors/ai-tool-choice-violation-error) | Type: Reference | Summary: Learn how to handle AI_ToolChoiceViolationError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_TypeValidationError](/v6/docs/reference/ai-sdk-errors/ai-type-validation-error) | Type: Reference | Summary: Learn how to fix AI_TypeValidationError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_UIMessageStreamError](/v6/docs/reference/ai-sdk-errors/ai-ui-message-stream-error) | Type: Reference | Summary: Learn how to fix AI_UIMessageStreamError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

        - [AI_UnsupportedFunctionalityError](/v6/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error) | Type: Reference | Summary: Learn how to fix AI_UnsupportedFunctionalityError | Prerequisites: /v6/docs/reference/ai-sdk-errors | Topics: v6, docs, reference

    - [AI SDK RSC](/v6/docs/reference/ai-sdk-rsc) | Type: Reference | Summary: Reference documentation for the AI SDK RSC | Prerequisites: /v6/docs/reference | Topics: v6, docs, reference

        - [createAI](/v6/docs/reference/ai-sdk-rsc/create-ai) | Type: Reference | Summary: Reference for the createAI function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [createStreamableUI](/v6/docs/reference/ai-sdk-rsc/create-streamable-ui) | Type: Reference | Summary: Reference for the createStreamableUI function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [createStreamableValue](/v6/docs/reference/ai-sdk-rsc/create-streamable-value) | Type: Reference | Summary: Reference for the createStreamableValue function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [getAIState](/v6/docs/reference/ai-sdk-rsc/get-ai-state) | Type: Reference | Summary: Reference for the getAIState function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [getMutableAIState](/v6/docs/reference/ai-sdk-rsc/get-mutable-ai-state) | Type: Reference | Summary: Reference for the getMutableAIState function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [readStreamableValue](/v6/docs/reference/ai-sdk-rsc/read-streamable-value) | Type: Reference | Summary: Reference for the readStreamableValue function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [render (Removed)](/v6/docs/reference/ai-sdk-rsc/render) | Type: Reference | Summary: Reference for the render function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [streamUI](/v6/docs/reference/ai-sdk-rsc/stream-ui) | Type: Reference | Summary: Reference for the streamUI function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [useActions](/v6/docs/reference/ai-sdk-rsc/use-actions) | Type: Reference | Summary: Reference for the useActions function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [useAIState](/v6/docs/reference/ai-sdk-rsc/use-ai-state) | Type: Reference | Summary: Reference for the useAIState function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [useStreamableValue](/v6/docs/reference/ai-sdk-rsc/use-streamable-value) | Type: Reference | Summary: Reference for the useStreamableValue function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

        - [useUIState](/v6/docs/reference/ai-sdk-rsc/use-ui-state) | Type: Reference | Summary: Reference for the useUIState function from the AI SDK RSC | Prerequisites: /v6/docs/reference/ai-sdk-rsc | Topics: v6, docs, reference

    - [AI SDK UI](/v6/docs/reference/ai-sdk-ui) | Type: Reference | Summary: Reference documentation for the AI SDK UI | Prerequisites: /v6/docs/reference | Topics: v6, docs, reference

        - [convertToModelMessages](/v6/docs/reference/ai-sdk-ui/convert-to-model-messages) | Type: Reference | Summary: Convert useChat messages to ModelMessages for AI functions (API Reference) | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [createUIMessageStream](/v6/docs/reference/ai-sdk-ui/create-ui-message-stream) | Type: Reference | Summary: API Reference for createUIMessageStream. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [createUIMessageStreamResponse](/v6/docs/reference/ai-sdk-ui/create-ui-message-stream-response) | Type: Reference | Summary: API Reference for createUIMessageStreamResponse. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [DirectChatTransport](/v6/docs/reference/ai-sdk-ui/direct-chat-transport) | Type: Reference | Summary: API Reference for the DirectChatTransport class. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [InferUITool](/v6/docs/reference/ai-sdk-ui/infer-ui-tool) | Type: Reference | Summary: API Reference for InferUITool. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [InferUITools](/v6/docs/reference/ai-sdk-ui/infer-ui-tools) | Type: Reference | Summary: API Reference for InferUITools. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [pipeUIMessageStreamToResponse](/v6/docs/reference/ai-sdk-ui/pipe-ui-message-stream-to-response) | Type: Reference | Summary: Learn to use pipeUIMessageStreamToResponse helper function to pipe streaming data to a ServerResponse object. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [pruneMessages](/v6/docs/reference/ai-sdk-ui/prune-messages) | Type: Reference | Summary: API Reference for pruneMessages. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [readUIMessageStream](/v6/docs/reference/ai-sdk-ui/read-ui-message-stream) | Type: Reference | Summary: API Reference for readUIMessageStream. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [useChat](/v6/docs/reference/ai-sdk-ui/use-chat) | Type: Reference | Summary: API reference for the useChat hook. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [useCompletion](/v6/docs/reference/ai-sdk-ui/use-completion) | Type: Reference | Summary: API reference for the useCompletion hook. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

        - [useObject](/v6/docs/reference/ai-sdk-ui/use-object) | Type: Reference | Summary: API reference for the useObject hook. | Prerequisites: /v6/docs/reference/ai-sdk-ui | Topics: v6, docs, reference

- [Troubleshooting](/v6/docs/troubleshooting) | Type: Conceptual | Summary: Troubleshooting information for common issues encountered with the AI SDK. | Topics: v6, docs, troubleshooting

    - [Abort and resumable streams](/v6/docs/troubleshooting/abort-breaks-resumable-streams) | Type: Conceptual | Summary: Troubleshooting abort and stop behavior with resumable streams | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Azure OpenAI Slow to Stream](/v6/docs/troubleshooting/azure-stream-slow) | Type: Conceptual | Summary: Learn to troubleshoot Azure OpenAI slow to stream issues. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Server Action Plain Objects Error](/v6/docs/troubleshooting/client-stream-error) | Type: Conceptual | Summary: Troubleshooting errors related to using AI SDK Core functions with Server Actions. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [High memory usage when processing many images](/v6/docs/troubleshooting/high-memory-usage-with-images) | Type: Conceptual | Summary: Troubleshooting high memory usage when using generateText or streamText with many images | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Jest: cannot find module '@ai-sdk/rsc'](/v6/docs/troubleshooting/jest-cannot-find-module-ai-rsc) | Type: Conceptual | Summary: Troubleshooting AI SDK errors related to the Jest: cannot find module '@ai-sdk/rsc' error | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Missing Tool Results Error](/v6/docs/troubleshooting/missing-tool-results-error) | Type: Conceptual | Summary: How to fix the "Tool results are missing for tool calls" error when using the AI SDK. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Model is not assignable to type "LanguageModelV1"](/v6/docs/troubleshooting/model-is-not-assignable-to-type) | Type: Conceptual | Summary: Troubleshooting errors related to incompatible models. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Object generation failed with OpenAI](/v6/docs/troubleshooting/no-object-generated-content-filter) | Type: Conceptual | Summary: Troubleshooting NoObjectGeneratedError with finish-reason content-filter caused by incompatible Zod schema types when using OpenAI structured outputs | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Type Error with onToolCall](/v6/docs/troubleshooting/ontoolcall-type-narrowing) | Type: Conceptual | Summary: How to handle TypeScript type errors when using the onToolCall callback | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [React error "Maximum update depth exceeded"](/v6/docs/troubleshooting/react-maximum-update-depth-exceeded) | Type: Conceptual | Summary: Troubleshooting errors related to the "Maximum update depth exceeded" error. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Repeated assistant messages in useChat](/v6/docs/troubleshooting/repeated-assistant-messages) | Type: Conceptual | Summary: Troubleshooting duplicate assistant messages when using useChat with streamText | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Server Actions in Client Components](/v6/docs/troubleshooting/server-actions-in-client-components) | Type: Conceptual | Summary: Troubleshooting errors related to server actions in client components. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [useChat/useCompletion stream output contains 0:... instead of text](/v6/docs/troubleshooting/strange-stream-output) | Type: Conceptual | Summary: How to fix strange stream output in the UI | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [onFinish not called when stream is aborted](/v6/docs/troubleshooting/stream-abort-handling) | Type: Conceptual | Summary: Troubleshooting onFinish callback not executing when streams are aborted with toUIMessageStreamResponse | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [streamText fails silently](/v6/docs/troubleshooting/stream-text-not-working) | Type: Conceptual | Summary: Troubleshooting errors related to the streamText function not working. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Streamable UI Errors](/v6/docs/troubleshooting/streamable-ui-errors) | Type: Conceptual | Summary: Troubleshooting errors related to streamable UI. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Streaming Not Working When Deployed](/v6/docs/troubleshooting/streaming-not-working-when-deployed) | Type: Conceptual | Summary: Troubleshooting streaming issues in deployed apps. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Streaming Not Working When Proxied](/v6/docs/troubleshooting/streaming-not-working-when-proxied) | Type: Conceptual | Summary: Troubleshooting streaming issues in proxied apps. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Streaming Status Shows But No Text Appears](/v6/docs/troubleshooting/streaming-status-delay) | Type: Conceptual | Summary: Why useChat shows "streaming" status without any visible content | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Getting Timeouts When Deploying on Vercel](/v6/docs/troubleshooting/timeout-on-vercel) | Type: Conceptual | Summary: Learn how to fix timeouts and cut off responses when deploying to Vercel. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Tool calling with structured outputs](/v6/docs/troubleshooting/tool-calling-with-structured-outputs) | Type: Conceptual | Summary: Troubleshooting tool calling when combined with structured output generation | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Tool Invocation Missing Result Error](/v6/docs/troubleshooting/tool-invocation-missing-result) | Type: Conceptual | Summary: How to fix the "ToolInvocation must have a result" error when using tools without execute functions | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [TypeScript error "Cannot find namespace 'JSX'"](/v6/docs/troubleshooting/typescript-cannot-find-namespace-jsx) | Type: Conceptual | Summary: Troubleshooting errors related to TypeScript and JSX. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [TypeScript performance issues with Zod and AI SDK 5](/v6/docs/troubleshooting/typescript-performance-zod) | Type: Conceptual | Summary: Troubleshooting TypeScript server crashes and slow performance when using Zod with AI SDK 5 | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Unclosed Streams](/v6/docs/troubleshooting/unclosed-streams) | Type: Conceptual | Summary: Troubleshooting errors related to unclosed streams. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Unsupported model version error](/v6/docs/troubleshooting/unsupported-model-version) | Type: Conceptual | Summary: Troubleshooting the AI_UnsupportedModelVersionError when migrating to AI SDK 5 | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [useChat "An error occurred"](/v6/docs/troubleshooting/use-chat-an-error-occurred) | Type: Conceptual | Summary: Troubleshooting errors related to the "An error occurred" error in useChat. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Custom headers, body, and credentials not working with useChat](/v6/docs/troubleshooting/use-chat-custom-request-options) | Type: Conceptual | Summary: Troubleshooting errors related to custom request configuration in useChat hook | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [useChat Failed to Parse Stream](/v6/docs/troubleshooting/use-chat-failed-to-parse-stream) | Type: Conceptual | Summary: Troubleshooting errors related to the Use Chat Failed to Parse Stream error. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [Stale body values with useChat](/v6/docs/troubleshooting/use-chat-stale-body-data) | Type: Conceptual | Summary: Troubleshooting stale values when passing information via the body parameter of useChat | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

    - [useChat No Response](/v6/docs/troubleshooting/use-chat-tools-no-response) | Type: Conceptual | Summary: Troubleshooting errors related to the Use Chat Failed to Parse Stream error. | Prerequisites: /v6/docs/troubleshooting | Topics: v6, docs, troubleshooting

## Providers

- [Adapters](/v6/providers/adapters) | Type: Conceptual | Summary: Learn how to use AI SDK Adapters. | Topics: v6, providers, adapters

    - [LangChain](/v6/providers/adapters/langchain) | Type: Conceptual | Summary: Learn how to use LangChain with the AI SDK. | Prerequisites: /v6/providers/adapters | Topics: v6, providers, adapters

    - [LlamaIndex](/v6/providers/adapters/llamaindex) | Type: Conceptual | Summary: Learn how to use LlamaIndex with the AI SDK. | Prerequisites: /v6/providers/adapters | Topics: v6, providers, adapters

- [AI SDK Providers](/v6/providers/ai-sdk-providers) | Type: Conceptual | Summary: Learn how to use AI SDK providers. | Topics: v6, providers, ai-sdk-providers

    - [AI Gateway](/v6/providers/ai-sdk-providers/ai-gateway) | Type: Conceptual | Summary: Learn how to use the AI Gateway provider with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Alibaba](/v6/providers/ai-sdk-providers/alibaba) | Type: Conceptual | Summary: Learn how to use Alibaba Cloud Model Studio (Qwen) models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Amazon Bedrock](/v6/providers/ai-sdk-providers/amazon-bedrock) | Type: Conceptual | Summary: Learn how to use the Amazon Bedrock provider. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Anthropic](/v6/providers/ai-sdk-providers/anthropic) | Type: Conceptual | Summary: Learn how to use the Anthropic provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Claude Platform on AWS](/v6/providers/ai-sdk-providers/anthropic-aws) | Type: Conceptual | Summary: Learn how to use the Claude Platform on AWS provider. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [AssemblyAI](/v6/providers/ai-sdk-providers/assemblyai) | Type: Conceptual | Summary: Learn how to use the AssemblyAI provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Azure OpenAI](/v6/providers/ai-sdk-providers/azure) | Type: Conceptual | Summary: Learn how to use the Azure OpenAI provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Baseten](/v6/providers/ai-sdk-providers/baseten) | Type: Conceptual | Summary: Learn how to use Baseten models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Black Forest Labs](/v6/providers/ai-sdk-providers/black-forest-labs) | Type: Conceptual | Summary: Learn how to use Black Forest Labs models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [ByteDance](/v6/providers/ai-sdk-providers/bytedance) | Type: Conceptual | Summary: Learn how to use ByteDance Seedance video and Seedream image models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Cerebras](/v6/providers/ai-sdk-providers/cerebras) | Type: Conceptual | Summary: Learn how to use Cerebras's models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Cohere](/v6/providers/ai-sdk-providers/cohere) | Type: Conceptual | Summary: Learn how to use the Cohere provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Deepgram](/v6/providers/ai-sdk-providers/deepgram) | Type: Conceptual | Summary: Learn how to use the Deepgram provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [DeepInfra](/v6/providers/ai-sdk-providers/deepinfra) | Type: Conceptual | Summary: Learn how to use DeepInfra's models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [DeepSeek](/v6/providers/ai-sdk-providers/deepseek) | Type: Conceptual | Summary: Learn how to use DeepSeek's models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs) | Type: Conceptual | Summary: Learn how to use the ElevenLabs provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Fal](/v6/providers/ai-sdk-providers/fal) | Type: Conceptual | Summary: Learn how to use Fal AI models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Fireworks](/v6/providers/ai-sdk-providers/fireworks) | Type: Conceptual | Summary: Learn how to use Fireworks models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Fish Audio](/v6/providers/ai-sdk-providers/fish-audio) | Type: Conceptual | Summary: Learn how to use the Fish Audio provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Gladia](/v6/providers/ai-sdk-providers/gladia) | Type: Conceptual | Summary: Learn how to use the Gladia provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [GMI Cloud](/v6/providers/ai-sdk-providers/gmicloud) | Type: Conceptual | Summary: Learn how to use GMI Cloud's models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Google Generative AI](/v6/providers/ai-sdk-providers/google-generative-ai) | Type: Conceptual | Summary: Learn how to use Google Generative AI Provider. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Google Vertex AI](/v6/providers/ai-sdk-providers/google-vertex) | Type: Conceptual | Summary: Learn how to use the Google Vertex AI provider. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Groq](/v6/providers/ai-sdk-providers/groq) | Type: Conceptual | Summary: Learn how to use Groq. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Hugging Face](/v6/providers/ai-sdk-providers/huggingface) | Type: Conceptual | Summary: Learn how to use Hugging Face Provider. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Hume](/v6/providers/ai-sdk-providers/hume) | Type: Conceptual | Summary: Learn how to use the Hume provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Kling AI](/v6/providers/ai-sdk-providers/klingai) | Type: Conceptual | Summary: Learn how to use the Kling AI provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Luma](/v6/providers/ai-sdk-providers/luma) | Type: Conceptual | Summary: Learn how to use Luma AI models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [MiniMax](/v6/providers/ai-sdk-providers/minimax) | Type: Conceptual | Summary: Learn how to use MiniMax models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Mistral AI](/v6/providers/ai-sdk-providers/mistral) | Type: Conceptual | Summary: Learn how to use Mistral. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Moonshot AI](/v6/providers/ai-sdk-providers/moonshotai) | Type: Conceptual | Summary: Learn how to use Moonshot AI models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Open Responses](/v6/providers/ai-sdk-providers/open-responses) | Type: Conceptual | Summary: Learn how to use the Open Responses provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [OpenAI](/v6/providers/ai-sdk-providers/openai) | Type: Conceptual | Summary: Learn how to use the OpenAI provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Perplexity](/v6/providers/ai-sdk-providers/perplexity) | Type: Conceptual | Summary: Learn how to use Perplexity's Sonar API with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Prodia](/v6/providers/ai-sdk-providers/prodia) | Type: Conceptual | Summary: Learn how to use Prodia models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [QuiverAI](/v6/providers/ai-sdk-providers/quiverai) | Type: Conceptual | Summary: Learn how to use QuiverAI models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Replicate](/v6/providers/ai-sdk-providers/replicate) | Type: Conceptual | Summary: Learn how to use Replicate models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Rev.ai](/v6/providers/ai-sdk-providers/revai) | Type: Conceptual | Summary: Learn how to use the Rev.ai provider for the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Together.ai](/v6/providers/ai-sdk-providers/togetherai) | Type: Conceptual | Summary: Learn how to use Together.ai's models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Vercel](/v6/providers/ai-sdk-providers/vercel) | Type: Conceptual | Summary: Learn how to use Vercel's v0 models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Voyage AI](/v6/providers/ai-sdk-providers/voyage) | Type: Conceptual | Summary: Learn how to use the Voyage AI provider for embedding and reranking with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [xAI Grok](/v6/providers/ai-sdk-providers/xai) | Type: Conceptual | Summary: Learn how to use xAI Grok and Imagine. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

    - [Z.AI](/v6/providers/ai-sdk-providers/zai) | Type: Conceptual | Summary: Learn how to use Z.AI's GLM models with the AI SDK. | Prerequisites: /v6/providers/ai-sdk-providers | Topics: v6, providers, ai-sdk-providers

- [Community Providers](/v6/providers/community-providers) | Type: Conceptual | Summary: Learn how to use Language Model Specification. | Topics: v6, providers, community-providers

    - [A2A](/v6/providers/community-providers/a2a) | Type: Conceptual | Summary: A2A Protocol Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [ACP (Agent Client Protocol)](/v6/providers/community-providers/acp) | Type: Conceptual | Summary: ACP Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Aihubmix](/v6/providers/community-providers/aihubmix) | Type: Conceptual | Summary: Learn how to use Aihubmix with the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [AI/ML API](/v6/providers/community-providers/aimlapi) | Type: Conceptual | Summary: Learn how to use the AI/ML API provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Anthropic Vertex](/v6/providers/community-providers/anthropic-vertex-ai) | Type: Conceptual | Summary: Learn how to use the Anthropic Vertex provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Apertis](/v6/providers/community-providers/apertis) | Type: Conceptual | Summary: Apertis AI Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Automatic1111](/v6/providers/community-providers/automatic1111) | Type: Conceptual | Summary: Automatic1111 Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Azure AI](/v6/providers/community-providers/azure-ai) | Type: Conceptual | Summary: Learn how to use the @quail-ai/azure-ai-provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Browser AI](/v6/providers/community-providers/browser-ai) | Type: Conceptual | Summary: Learn how to use browser AI model providers for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Cencori](/v6/providers/community-providers/cencori) | Type: Conceptual | Summary: Cencori Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Claude Code](/v6/providers/community-providers/claude-code) | Type: Conceptual | Summary: Learn how to use the Claude Code provider to access Claude models through the Claude Agent SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Cloudflare AI Gateway](/v6/providers/community-providers/cloudflare-ai-gateway) | Type: Conceptual | Summary: Learn how to use the Cloudflare AI Gateway provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Cloudflare Workers AI](/v6/providers/community-providers/cloudflare-workers-ai) | Type: Conceptual | Summary: Learn how to use the Cloudflare Workers AI provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Codex CLI (App Server)](/v6/providers/community-providers/codex-app-server) | Type: Conceptual | Summary: Learn how to use the Codex CLI App Server provider for mid-execution message injection and persistent threads. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Codex CLI](/v6/providers/community-providers/codex-cli) | Type: Conceptual | Summary: Learn how to use the Codex CLI provider to access OpenAI GPT-5 models through the Codex CLI. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Crosshatch](/v6/providers/community-providers/crosshatch) | Type: Conceptual | Summary: Learn how to use the Crosshatch provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Writing a Custom Provider](/v6/providers/community-providers/custom-providers) | Type: Conceptual | Summary: Learn how to write a custom provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Dify](/v6/providers/community-providers/dify) | Type: Conceptual | Summary: Learn how to use the Dify provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Firemoon](/v6/providers/community-providers/firemoon) | Type: Conceptual | Summary: Firemoon provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Flowise](/v6/providers/community-providers/flowise) | Type: Conceptual | Summary: Learn how to use the Flowise provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [FriendliAI](/v6/providers/community-providers/friendliai) | Type: Conceptual | Summary: Learn how to use the FriendliAI Provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Gemini CLI](/v6/providers/community-providers/gemini-cli) | Type: Conceptual | Summary: Learn how to use the Gemini CLI provider to access Google's Gemini models. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Helicone](/v6/providers/community-providers/helicone) | Type: Conceptual | Summary: Helicone Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Hindsight](/v6/providers/community-providers/hindsight) | Type: Conceptual | Summary: Learn how to use Hindsight persistent memory with the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Inflection AI](/v6/providers/community-providers/inflection-ai) | Type: Conceptual | Summary: Learn how to use the unofficial Inflection AI provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Jina AI](/v6/providers/community-providers/jina-ai) | Type: Conceptual | Summary: Learn how to use the Jina AI provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [LangDB](/v6/providers/community-providers/langdb) | Type: Conceptual | Summary: Learn how to use LangDB with the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Letta](/v6/providers/community-providers/letta) | Type: Conceptual | Summary: Learn how to use the Letta provider with the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [llama.cpp](/v6/providers/community-providers/llama-cpp) | Type: Conceptual | Summary: Learn how to use the llama.cpp provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [LlamaGate](/v6/providers/community-providers/llamagate) | Type: Conceptual | Summary: LlamaGate Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [MCP Sampling AI Provider](/v6/providers/community-providers/mcp-sampling) | Type: Conceptual | Summary: Learn how to use the MCP Sampling AI Provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Mem0](/v6/providers/community-providers/mem0) | Type: Conceptual | Summary: Learn how to use the Mem0 AI SDK provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [MiniMax](/v6/providers/community-providers/minimax) | Type: Conceptual | Summary: Learn how to use MiniMax provider with the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Mixedbread](/v6/providers/community-providers/mixedbread) | Type: Conceptual | Summary: Learn how to use the Mixedbread provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Neon AI Gateway](/v6/providers/community-providers/neon-ai-gateway) | Type: Conceptual | Summary: Learn how to use the Neon AI Gateway provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Nia](/v6/providers/community-providers/nia) | Type: Conceptual | Summary: Learn how to use Nia with the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Ollama](/v6/providers/community-providers/ollama) | Type: Conceptual | Summary: Learn how to use the Ollama provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [OLLM](/v6/providers/community-providers/ollm) | Type: Conceptual | Summary: OLLM Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [OpenCode](/v6/providers/community-providers/opencode-sdk) | Type: Conceptual | Summary: Learn how to use the OpenCode provider to access multiple AI models through a unified interface. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [OpenRouter](/v6/providers/community-providers/openrouter) | Type: Conceptual | Summary: OpenRouter Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Portkey](/v6/providers/community-providers/portkey) | Type: Conceptual | Summary: Learn how to use the Portkey provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Qwen](/v6/providers/community-providers/qwen) | Type: Conceptual | Summary: Learn how to use the Qwen provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [React Native Apple](/v6/providers/community-providers/react-native-apple) | Type: Conceptual | Summary: Learn how to use the Apple provider for on-device AI. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Requesty](/v6/providers/community-providers/requesty) | Type: Conceptual | Summary: Requesty Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Runpod](/v6/providers/community-providers/runpod) | Type: Conceptual | Summary: Runpod Provider for the AI SDK | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [SambaNova](/v6/providers/community-providers/sambanova) | Type: Conceptual | Summary: Learn how to use the SambaNova provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [SAP AI Core](/v6/providers/community-providers/sap-ai) | Type: Conceptual | Summary: Learn how to use the SAP AI Core provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Sarvam](/v6/providers/community-providers/sarvam) | Type: Conceptual | Summary: Learn how to use the Sarvam AI provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Soniox](/v6/providers/community-providers/soniox) | Type: Conceptual | Summary: Learn how to use the Soniox provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Spark](/v6/providers/community-providers/spark) | Type: Conceptual | Summary: Learn how to use the Spark provider for the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Supermemory](/v6/providers/community-providers/supermemory) | Type: Conceptual | Summary: Learn how to use the Supermemory AI SDK provider for the Vercel AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [vectorstores](/v6/providers/community-providers/vectorstores) | Type: Conceptual | Summary: Learn how to use vector databases with the AI SDK. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Voyage AI](/v6/providers/community-providers/voyage-ai) | Type: Conceptual | Summary: Learn how to use the Voyage AI provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [ZeroEntropy](/v6/providers/community-providers/zeroentropy) | Type: Conceptual | Summary: Learn how to use the ZeroEntropy community provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

    - [Zhipu AI (Z.AI)](/v6/providers/community-providers/zhipu) | Type: Conceptual | Summary: Learn how to use the Zhipu (Z.AI) provider. | Prerequisites: /v6/providers/community-providers | Topics: v6, providers, community-providers

- [Observability Integrations](/v6/providers/observability) | Type: Conceptual | Summary: AI SDK Integration for monitoring and tracing LLM applications | Topics: v6, providers, observability

    - [Arize AX](/v6/providers/observability/arize-ax) | Type: Conceptual | Summary: Trace, monitor, and evaluate LLM applications with Arize AX | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Axiom](/v6/providers/observability/axiom) | Type: Conceptual | Summary: Measure, observe, and improve your AI SDK application with Axiom | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Braintrust](/v6/providers/observability/braintrust) | Type: Conceptual | Summary: Monitoring and tracing LLM applications with Braintrust | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Confident AI](/v6/providers/observability/confident-ai) | Type: Conceptual | Summary: Trace and Evaluate your LLM applications using Confident AI | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Helicone](/v6/providers/observability/helicone) | Type: Conceptual | Summary: Monitor and optimize your AI SDK applications with minimal configuration using Helicone | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Laminar](/v6/providers/observability/laminar) | Type: Conceptual | Summary: Monitor your AI SDK applications with Laminar | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Langfuse](/v6/providers/observability/langfuse) | Type: Conceptual | Summary: Monitor, evaluate and debug your AI SDK application with Langfuse | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [LangSmith](/v6/providers/observability/langsmith) | Type: Conceptual | Summary: Monitor and evaluate your AI SDK application with LangSmith | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [LangWatch](/v6/providers/observability/langwatch) | Type: Conceptual | Summary: Track, monitor, guardrail and evaluate your AI SDK applications with LangWatch. | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Latitude](/v6/providers/observability/latitude) | Type: Conceptual | Summary: Monitor and debug your AI SDK application with Latitude | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Maxim](/v6/providers/observability/maxim) | Type: Conceptual | Summary: Evaluate & Observe LLM applications with Maxim | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [MLflow](/v6/providers/observability/mlflow) | Type: Conceptual | Summary: Track, visualize, and debug Vercel AI SDK traces with MLflow Tracing | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Patronus](/v6/providers/observability/patronus) | Type: Conceptual | Summary: Monitor, evaluate and debug your AI SDK application with Patronus | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [PostHog](/v6/providers/observability/posthog) | Type: Conceptual | Summary: Monitor and analyze LLM usage with PostHog | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Respan](/v6/providers/observability/respan) | Type: Conceptual | Summary: Trace and monitor your AI SDK application with Respan | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Scorecard](/v6/providers/observability/scorecard) | Type: Conceptual | Summary: Monitoring and evaluating LLM applications with Scorecard | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [SigNoz](/v6/providers/observability/signoz) | Type: Conceptual | Summary: Monitor, observe and debug your AI SDK application with SigNoz | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Traceloop](/v6/providers/observability/traceloop) | Type: Conceptual | Summary: Monitoring and evaluating LLM applications with Traceloop | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

    - [Weave](/v6/providers/observability/weave) | Type: Conceptual | Summary: Monitor and evaluate LLM applications with Weave. | Prerequisites: /v6/providers/observability | Topics: v6, providers, observability

- [OpenAI Compatible Providers](/v6/providers/openai-compatible-providers) | Type: Conceptual | Summary: Use OpenAI compatible providers with the AI SDK. | Topics: v6, providers, openai-compatible-providers

    - [Clarifai](/v6/providers/openai-compatible-providers/clarifai) | Type: Conceptual | Summary: Use Clarifai OpenAI compatible API with the AI SDK. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

    - [Writing a Custom Provider](/v6/providers/openai-compatible-providers/custom-providers) | Type: Conceptual | Summary: Create a custom provider package for an OpenAI-compatible provider leveraging the AI SDK OpenAI Compatible package. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

    - [Heroku](/v6/providers/openai-compatible-providers/heroku) | Type: Conceptual | Summary: Use a Heroku OpenAI compatible API with the AI SDK. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

    - [LM Studio](/v6/providers/openai-compatible-providers/lmstudio) | Type: Conceptual | Summary: Use the LM Studio OpenAI compatible API with the AI SDK. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

    - [ModelRush](/v6/providers/openai-compatible-providers/modelrush) | Type: Conceptual | Summary: Use the ModelRush OpenAI compatible API with the AI SDK. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

    - [NEAR AI Cloud](/v6/providers/openai-compatible-providers/nearai) | Type: Conceptual | Summary: Use the NEAR AI Cloud OpenAI compatible API with the AI SDK. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

    - [NVIDIA NIM](/v6/providers/openai-compatible-providers/nim) | Type: Conceptual | Summary: Use NVIDIA NIM OpenAI compatible API with the AI SDK. | Prerequisites: /v6/providers/openai-compatible-providers | Topics: v6, providers, openai-compatible-providers

## Cookbook

- [Express](/v6/cookbook/api-servers/express) | Type: Conceptual | Summary: Learn how to use the AI SDK in an Express server | Topics: v6, cookbook, api-servers

- [Fastify](/v6/cookbook/api-servers/fastify) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Fastify server | Topics: v6, cookbook, api-servers

- [Hono](/v6/cookbook/api-servers/hono) | Type: Conceptual | Summary: Example of using the AI SDK in a Hono server. | Topics: v6, cookbook, api-servers

- [Nest.js](/v6/cookbook/api-servers/nest) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Nest.js server | Topics: v6, cookbook, api-servers

- [Node.js HTTP Server](/v6/cookbook/api-servers/node-http-server) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Node.js HTTP server | Topics: v6, cookbook, api-servers

- [Guides](/v6/cookbook/guides) | Type: Conceptual | Summary: Learn how to build AI applications with the AI SDK | Topics: v6, cookbook, guides

    - [Add Skills to Your Agent](/v6/cookbook/guides/agent-skills) | Type: Guide | Summary: Learn how to extend your agent with specialized capabilities loaded at runtime with Agent Skills. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with Claude 4](/v6/cookbook/guides/claude-4) | Type: Guide | Summary: Get started with Claude 4 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with Computer Use](/v6/cookbook/guides/computer-use) | Type: Guide | Summary: Get started with Claude's Computer Use capabilities with the AI SDK | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Build a Custom Memory Tool](/v6/cookbook/guides/custom-memory-tool) | Type: Guide | Summary: Build an agent that persists memories using a filesystem-backed memory tool. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with DeepSeek V3.2](/v6/cookbook/guides/deepseek-v3-2) | Type: Guide | Summary: Get started with DeepSeek V3.2 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with Gemini 3](/v6/cookbook/guides/gemini) | Type: Guide | Summary: Get started with Gemini 3 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Google Gemini Image Generation](/v6/cookbook/guides/google-gemini-image-generation) | Type: Guide | Summary: Generate and edit images with Google Gemini 2.5 Flash Image using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with GPT-5](/v6/cookbook/guides/gpt-5) | Type: Guide | Summary: Get started with GPT-5 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with Llama 3.1](/v6/cookbook/guides/llama-3_1) | Type: Guide | Summary: Get started with Llama 3.1 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Multi-Modal Agent](/v6/cookbook/guides/multi-modal-chatbot) | Type: Guide | Summary: Learn how to build a multi-modal agent that can process images and PDFs with the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Natural Language Postgres](/v6/cookbook/guides/natural-language-postgres) | Type: Guide | Summary: Learn how to build a Next.js app that lets you talk to a PostgreSQL database in natural language. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with OpenAI o1](/v6/cookbook/guides/o1) | Type: Guide | Summary: Get started with OpenAI o1 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with OpenAI o3-mini](/v6/cookbook/guides/o3) | Type: Guide | Summary: Get started with OpenAI o3-mini using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [OpenAI Responses API](/v6/cookbook/guides/openai-responses) | Type: Guide | Summary: Get started with the OpenAI Responses API using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with DeepSeek R1](/v6/cookbook/guides/r1) | Type: Guide | Summary: Get started with DeepSeek R1 using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [RAG Agent](/v6/cookbook/guides/rag-chatbot) | Type: Guide | Summary: Learn how to build a RAG Agent with the AI SDK and Next.js | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Slackbot Agent Guide](/v6/cookbook/guides/slackbot) | Type: Guide | Summary: Learn how to use the AI SDK to build an AI Agent in Slack. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

    - [Get started with Claude 3.7 Sonnet](/v6/cookbook/guides/sonnet-3-7) | Type: Guide | Summary: Get started with Claude 3.7 Sonnet using the AI SDK. | Prerequisites: /v6/cookbook/guides | Topics: v6, cookbook, guides

- [Caching Middleware](/v6/cookbook/next/caching-middleware) | Type: Conceptual | Summary: Learn how to create a caching middleware with Next.js and KV. | Topics: v6, cookbook, next

- [Call Tools](/v6/cookbook/next/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Call Tools in Multiple Steps](/v6/cookbook/next/call-tools-multiple-steps) | Type: Conceptual | Summary: Learn how to call tools in multiple steps using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Chat with PDFs](/v6/cookbook/next/chat-with-pdf) | Type: Conceptual | Summary: Learn how to build a chatbot that can understand PDFs using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Streaming with Custom Format](/v6/cookbook/next/custom-stream-format) | Type: Conceptual | Summary: Build a custom format to stream LLM responses | Topics: v6, cookbook, next

- [Generate Image with Chat Prompt](/v6/cookbook/next/generate-image-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate an image with a chat prompt using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Generate Object](/v6/cookbook/next/generate-object) | Type: Conceptual | Summary: Learn how to generate object using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Generate Object with File Prompt through Form Submission](/v6/cookbook/next/generate-object-with-file-prompt) | Type: Conceptual | Summary: Learn how to generate object with file prompt through form submission using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Generate Text](/v6/cookbook/next/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Next.js. | Topics: v6, cookbook, next

- [Generate Text with Chat Prompt](/v6/cookbook/next/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Human-in-the-Loop with Next.js](/v6/cookbook/next/human-in-the-loop) | Type: Conceptual | Summary: Add a human approval step to your agentic system with Next.js and the AI SDK | Topics: v6, cookbook, next

- [Markdown Chatbot with Memoization](/v6/cookbook/next/markdown-chatbot-with-memoization) | Type: Conceptual | Summary: Build a chatbot that renders and memoizes Markdown responses with Next.js and the AI SDK. | Topics: v6, cookbook, next

- [Model Context Protocol (MCP) Tools](/v6/cookbook/next/mcp-tools) | Type: Conceptual | Summary: Learn how to use MCP tools with the AI SDK and Next.js | Topics: v6, cookbook, next

- [Render Visual Interface in Chat](/v6/cookbook/next/render-visual-interface-in-chat) | Type: Conceptual | Summary: Learn how to render visual interfaces in chat using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Send Custom Body from useChat](/v6/cookbook/next/send-custom-body-from-use-chat) | Type: Conceptual | Summary: Learn how to send a custom body from the useChat hook using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Stream Object](/v6/cookbook/next/stream-object) | Type: Conceptual | Summary: Learn how to stream object using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Stream Text](/v6/cookbook/next/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and Next.js | Topics: v6, cookbook, next

- [streamText Multi-Step Cookbook](/v6/cookbook/next/stream-text-multistep) | Type: Conceptual | Summary: Learn how to create several streamText steps with different settings | Topics: v6, cookbook, next

- [Stream Text with Chat Prompt](/v6/cookbook/next/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Stream Text with Image Prompt](/v6/cookbook/next/stream-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream text with an image prompt using the AI SDK and Next.js | Topics: v6, cookbook, next

- [Track Agent Token Usage](/v6/cookbook/next/track-agent-token-usage) | Type: Conceptual | Summary: Learn how to track the active context window with ToolLoopAgent. | Topics: v6, cookbook, next

- [Share useChat State Across Components](/v6/cookbook/next/use-shared-chat-context) | Type: Conceptual | Summary: Learn how to share a chat instance across multiple components with useChat and easily reset the chat. | Topics: v6, cookbook, next

- [Call Tools](/v6/cookbook/node/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and Node | Topics: v6, cookbook, node

- [Call Tools in Parallel](/v6/cookbook/node/call-tools-in-parallel) | Type: Conceptual | Summary: Learn how to call tools in parallel using the AI SDK in Node.js | Topics: v6, cookbook, node

- [Call Tools in Multiple Steps](/v6/cookbook/node/call-tools-multiple-steps) | Type: Conceptual | Summary: Learn how to call tools with multiple steps using the AI SDK and Node | Topics: v6, cookbook, node

- [Call Tools with Image Prompt](/v6/cookbook/node/call-tools-with-image-prompt) | Type: Conceptual | Summary: Learn how to call tools with image prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Dynamic Prompt Caching](/v6/cookbook/node/dynamic-prompt-caching) | Type: Conceptual | Summary: Learn how to reduce API costs by implementing dynamic prompt caching for Anthropic models using cache control directives. | Topics: v6, cookbook, node

- [Embed Text](/v6/cookbook/node/embed-text) | Type: Conceptual | Summary: Learn how to embed text using the AI SDK and Node | Topics: v6, cookbook, node

- [Embed Text in Batch](/v6/cookbook/node/embed-text-batch) | Type: Conceptual | Summary: Learn how to embed multiple text using the AI SDK and Node | Topics: v6, cookbook, node

- [Generate Object](/v6/cookbook/node/generate-object) | Type: Conceptual | Summary: Learn how to generate structured data using the AI SDK and Node | Topics: v6, cookbook, node

- [Generate Object with a Reasoning Model](/v6/cookbook/node/generate-object-reasoning) | Type: Conceptual | Summary: Learn how to generate structured data with a reasoning model using the AI SDK and Node | Topics: v6, cookbook, node

- [Generate Text](/v6/cookbook/node/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Node | Topics: v6, cookbook, node

- [Generate Text with Chat Prompt](/v6/cookbook/node/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Generate Text with Image Prompt](/v6/cookbook/node/generate-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to generate text with image prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Intercepting Fetch Requests](/v6/cookbook/node/intercept-fetch-requests) | Type: Conceptual | Summary: Learn how to intercept fetch requests using the AI SDK and Node | Topics: v6, cookbook, node

- [Knowledge Base Agent](/v6/cookbook/node/knowledge-base-agent) | Type: Conceptual | Summary: Build an AI agent that can read from and write to a knowledge base using Upstash Search and the AI SDK | Topics: v6, cookbook, node

- [Local Caching Middleware](/v6/cookbook/node/local-caching-middleware) | Type: Conceptual | Summary: Learn how to create a caching middleware for local development. | Topics: v6, cookbook, node

- [Manual Agent Loop](/v6/cookbook/node/manual-agent-loop) | Type: Conceptual | Summary: Learn how to create your own agentic loop with full control over tool execution | Topics: v6, cookbook, node

- [Model Context Protocol (MCP) Elicitation](/v6/cookbook/node/mcp-elicitation) | Type: Conceptual | Summary: Learn how to handle elicitation requests from MCP servers with the AI SDK | Topics: v6, cookbook, node

- [Model Context Protocol (MCP) Tools](/v6/cookbook/node/mcp-tools) | Type: Conceptual | Summary: Learn how to use MCP tools with the AI SDK and Node | Topics: v6, cookbook, node

- [Repair Malformed JSON with jsonrepair](/v6/cookbook/node/repair-json-with-jsonrepair) | Type: Conceptual | Summary: Learn how to use the jsonrepair library to automatically fix truncated or malformed JSON output from language models. | Topics: v6, cookbook, node

- [Retrieval Augmented Generation](/v6/cookbook/node/retrieval-augmented-generation) | Type: Conceptual | Summary: Learn how to use retrieval augmented generation using the AI SDK and Node | Topics: v6, cookbook, node

- [Stream Object](/v6/cookbook/node/stream-object) | Type: Conceptual | Summary: Learn how to stream structured data using the AI SDK and Node | Topics: v6, cookbook, node

- [Record Final Object after Streaming Object](/v6/cookbook/node/stream-object-record-final-object) | Type: Conceptual | Summary: Learn how to record the final object after streaming an object using the AI SDK and Node | Topics: v6, cookbook, node

- [Record Token Usage After Streaming Object](/v6/cookbook/node/stream-object-record-token-usage) | Type: Conceptual | Summary: Learn how to record token usage when streaming structured data using the AI SDK and Node | Topics: v6, cookbook, node

- [Stream Object with Image Prompt](/v6/cookbook/node/stream-object-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream structured data with an image prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Stream Text](/v6/cookbook/node/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and Node | Topics: v6, cookbook, node

- [Stream Text with Chat Prompt](/v6/cookbook/node/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to stream text with chat prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Stream Text with File Prompt](/v6/cookbook/node/stream-text-with-file-prompt) | Type: Conceptual | Summary: Learn how to stream text with file prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Stream Text with Image Prompt](/v6/cookbook/node/stream-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream text with image prompt using the AI SDK and Node | Topics: v6, cookbook, node

- [Web Search Agent](/v6/cookbook/node/web-search-agent) | Type: Conceptual | Summary: Learn how to build an agent that has access to web with the AI SDK and Node | Topics: v6, cookbook, node

- [Call Tools](/v6/cookbook/rsc/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Call Tools in Parallel](/v6/cookbook/rsc/call-tools-in-parallel) | Type: Conceptual | Summary: Learn how to tools in parallel text using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Generate Object](/v6/cookbook/rsc/generate-object) | Type: Conceptual | Summary: Learn how to generate object using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Generate Text](/v6/cookbook/rsc/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Generate Text with Chat Prompt](/v6/cookbook/rsc/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Render Visual Interface in Chat](/v6/cookbook/rsc/render-visual-interface-in-chat) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Restore Messages From Database](/v6/cookbook/rsc/restore-messages-from-database) | Type: Conceptual | Summary: Learn how to restore messages from an external database using the AI SDK and React Server Components | Topics: v6, cookbook, rsc

- [Save Messages To Database](/v6/cookbook/rsc/save-messages-to-database) | Type: Conceptual | Summary: Learn how to save messages to an external database using the AI SDK and React Server Components | Topics: v6, cookbook, rsc

- [Stream Object](/v6/cookbook/rsc/stream-object) | Type: Conceptual | Summary: Learn how to stream object using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Stream Text](/v6/cookbook/rsc/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Stream Text with Chat Prompt](/v6/cookbook/rsc/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to stream text with chat prompt using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc

- [Record Token Usage after Streaming User Interfaces](/v6/cookbook/rsc/stream-ui-record-token-usage) | Type: Conceptual | Summary: Learn how to record token usage after streaming user interfaces using the AI SDK and React Server Components | Topics: v6, cookbook, rsc

- [Stream Updates to Visual Interfaces](/v6/cookbook/rsc/stream-updates-to-visual-interfaces) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: v6, cookbook, rsc