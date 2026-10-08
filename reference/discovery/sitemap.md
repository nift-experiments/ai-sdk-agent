# AI SDK documentation

## Purpose

This file is a high-level semantic index of the documentation.
It is intended for:

- LLM-assisted navigation (ChatGPT, Claude, etc.)
- Quick orientation for contributors
- Identifying relevant documentation areas during development

It is not intended to replace individual docs.

---

## Documentation

- [Advanced](/docs/advanced) | Type: Conceptual | Summary: Learn how to use advanced functionality within the AI SDK and RSC API. | Topics: advanced

    - [Backpressure](/docs/advanced/backpressure) | Type: Conceptual | Summary: How to handle backpressure and cancellation when working with the AI SDK | Prerequisites: /docs/advanced | Topics: advanced, backpressure

    - [Caching](/docs/advanced/caching) | Type: Conceptual | Summary: How to handle caching when working with the AI SDK | Prerequisites: /docs/advanced | Topics: advanced, caching

    - [Language Models as Routers](/docs/advanced/model-as-router) | Type: Conceptual | Summary: Generative User Interfaces and Language Models as Routers | Prerequisites: /docs/advanced | Topics: advanced, model-as-router

    - [Multiple Streamables](/docs/advanced/multiple-streamables) | Type: Conceptual | Summary: Learn to handle multiple streamables in your application. | Prerequisites: /docs/advanced | Topics: advanced, multiple-streamables

    - [Multistep Interfaces](/docs/advanced/multistep-interfaces) | Type: Conceptual | Summary: Concepts behind building multistep interfaces | Prerequisites: /docs/advanced | Topics: advanced, multistep-interfaces

    - [Prompt Engineering](/docs/advanced/prompt-engineering) | Type: Conceptual | Summary: Learn how to engineer prompts for LLMs with the AI SDK | Prerequisites: /docs/advanced | Topics: advanced, prompt-engineering

    - [Rate Limiting](/docs/advanced/rate-limiting) | Type: Conceptual | Summary: Learn how to rate limit your application. | Prerequisites: /docs/advanced | Topics: advanced, rate-limiting

    - [Rendering UI with Language Models](/docs/advanced/rendering-ui-with-language-models) | Type: Conceptual | Summary: Rendering UI with Language Models | Prerequisites: /docs/advanced | Topics: advanced, rendering-ui-with-language-models

    - [Secure URL Fetching](/docs/advanced/secure-url-fetching) | Type: Conceptual | Summary: How the AI SDK protects server-side fetches of URLs returned by model providers, and how to harden your deployment further. | Prerequisites: /docs/advanced | Topics: advanced, secure-url-fetching

    - [Sequential Generations](/docs/advanced/sequential-generations) | Type: Conceptual | Summary: Learn how to implement sequential generations ("chains") with the AI SDK | Prerequisites: /docs/advanced | Topics: advanced, sequential-generations

    - [Stopping Streams](/docs/advanced/stopping-streams) | Type: Conceptual | Summary: Learn how to cancel streams with the AI SDK | Prerequisites: /docs/advanced | Topics: advanced, stopping-streams

    - [Vercel Deployment Guide](/docs/advanced/vercel-deployment-guide) | Type: Conceptual | Summary: Learn how to deploy an AI application to production on Vercel | Prerequisites: /docs/advanced | Topics: advanced, vercel-deployment-guide

- [Building Agents](/docs/agents/building-agents) | Type: Conceptual | Summary: Complete guide to creating agents with the ToolLoopAgent. | Topics: agents, building-agents

- [Configuring Call Options](/docs/agents/configuring-call-options) | Type: Conceptual | Summary: Pass type-safe runtime inputs to dynamically configure agent behavior. | Topics: agents, configuring-call-options

- [Loop Control](/docs/agents/loop-control) | Type: Conceptual | Summary: Control agent execution with built-in loop management using stopWhen and prepareStep | Topics: agents, loop-control

- [Memory](/docs/agents/memory) | Type: Conceptual | Summary: Add persistent memory to your agent using provider-defined tools, memory providers, or a custom tool. | Topics: agents, memory

- [Overview](/docs/agents/overview) | Type: Conceptual | Summary: Learn how to build agents with the AI SDK. | Topics: agents, overview

- [Policy-Based Tool Approvals](/docs/agents/policy-tool-approvals) | Type: Conceptual | Summary: Author tool authorization rules as code with @ai-sdk/policy-opa and Open Policy Agent. | Topics: agents, policy-tool-approvals

- [Subagents](/docs/agents/subagents) | Type: Conceptual | Summary: Delegate context-heavy tasks to specialized subagents while keeping the main agent focused. | Topics: agents, subagents

- [Terminal UI](/docs/agents/terminal-ui) | Type: Conceptual | Summary: Run AI SDK agents in an interactive terminal UI. | Topics: agents, terminal-ui

- [Tool Approvals](/docs/agents/tool-approvals) | Type: Conceptual | Summary: Add manual and automatic approval flows to ToolLoopAgent tools. | Topics: agents, tool-approvals

- [WorkflowAgent](/docs/agents/workflow-agent) | Type: Conceptual | Summary: Build durable, resumable agents with the WorkflowAgent from @ai-sdk/workflow. | Topics: agents, workflow-agent

- [Workflow Patterns](/docs/agents/workflows) | Type: Conceptual | Summary: Learn workflow patterns for building reliable agents with the AI SDK. | Topics: agents, workflows

- [Batch](/docs/ai-sdk-core/batch) | Type: Conceptual | Summary: Learn how to process asynchronous batches with the AI SDK. | Topics: ai-sdk-core, batch

- [Code Mode](/docs/ai-sdk-core/code-mode) | Type: Conceptual | Summary: Let models orchestrate AI SDK tools with sandboxed JavaScript and TypeScript. | Topics: ai-sdk-core, code-mode

- [Decisions](/docs/ai-sdk-core/decisions) | Type: Conceptual | Summary: Decide answers to Choice, Score, and Boolean questions against shared state. | Topics: ai-sdk-core, decisions

- [DevTools](/docs/ai-sdk-core/devtools) | Type: Conceptual | Summary: Debug and inspect AI SDK applications with DevTools | Topics: ai-sdk-core, devtools

- [Embeddings](/docs/ai-sdk-core/embeddings) | Type: Conceptual | Summary: Learn how to embed values with the AI SDK. | Topics: ai-sdk-core, embeddings

- [Error Handling](/docs/ai-sdk-core/error-handling) | Type: Conceptual | Summary: Learn how to handle errors in the AI SDK Core | Topics: ai-sdk-core, error-handling

- [File Uploads](/docs/ai-sdk-core/file-uploads) | Type: Conceptual | Summary: Learn how to upload files and use provider references with the AI SDK. | Topics: ai-sdk-core, file-uploads

- [Generating Structured Data](/docs/ai-sdk-core/generating-structured-data) | Type: Conceptual | Summary: Learn how to generate structured data with the AI SDK. | Topics: ai-sdk-core, generating-structured-data

- [Generating Text](/docs/ai-sdk-core/generating-text) | Type: Conceptual | Summary: Learn how to generate text with the AI SDK. | Topics: ai-sdk-core, generating-text

- [Image Generation](/docs/ai-sdk-core/image-generation) | Type: Conceptual | Summary: Learn how to generate images with the AI SDK. | Topics: ai-sdk-core, image-generation

- [Lifecycle Callbacks](/docs/ai-sdk-core/lifecycle-callbacks) | Type: Conceptual | Summary: Observe AI SDK lifecycle events in generateText, streamText, embed, embedMany, rerank, and experimental_decide calls | Topics: ai-sdk-core, lifecycle-callbacks

- [MCP Apps](/docs/ai-sdk-core/mcp-apps) | Type: Conceptual | Summary: Learn how to connect to MCP Apps and render interactive tool UIs with the AI SDK. | Topics: ai-sdk-core, mcp-apps

- [MCP Events](/docs/ai-sdk-core/mcp-events) | Type: Conceptual | Summary: Understand the MCP webhook events contract and the AI SDK APIs for subscribing, verifying, and receiving events. | Topics: ai-sdk-core, mcp-events

- [Model Context Protocol (MCP)](/docs/ai-sdk-core/mcp-tools) | Type: Conceptual | Summary: Learn how to connect to Model Context Protocol (MCP) servers and use their tools with AI SDK Core. | Topics: ai-sdk-core, mcp-tools

- [Language Model Middleware](/docs/ai-sdk-core/middleware) | Type: Conceptual | Summary: Learn how to use middleware to enhance the behavior of language models | Topics: ai-sdk-core, middleware

- [Overview](/docs/ai-sdk-core/overview) | Type: Conceptual | Summary: An overview of AI SDK Core. | Topics: ai-sdk-core, overview

- [Prompt Engineering](/docs/ai-sdk-core/prompt-engineering) | Type: Conceptual | Summary: Learn how to develop prompts with AI SDK Core. | Topics: ai-sdk-core, prompt-engineering

- [Provider & Model Management](/docs/ai-sdk-core/provider-management) | Type: Conceptual | Summary: Learn how to work with multiple providers and models | Topics: ai-sdk-core, provider-management

- [Realtime](/docs/ai-sdk-core/realtime) | Type: Conceptual | Summary: Learn how to build realtime voice conversations with the AI SDK. | Topics: ai-sdk-core, realtime

- [Reasoning](/docs/ai-sdk-core/reasoning) | Type: Conceptual | Summary: Learn how to control reasoning across providers with the top-level reasoning parameter. | Topics: ai-sdk-core, reasoning

- [Reranking](/docs/ai-sdk-core/reranking) | Type: Conceptual | Summary: Learn how to rerank documents with the AI SDK. | Topics: ai-sdk-core, reranking

- [Runtime and Tool Context](/docs/ai-sdk-core/runtime-and-tool-context) | Type: Conceptual | Summary: Learn how runtime context, tool context, and telemetry context filtering work together. | Topics: ai-sdk-core, runtime-and-tool-context

- [Settings](/docs/ai-sdk-core/settings) | Type: Conceptual | Summary: Learn how to configure the AI SDK. | Topics: ai-sdk-core, settings

- [Skill Uploads](/docs/ai-sdk-core/skill-uploads) | Type: Conceptual | Summary: Learn how to upload skills and use provider references with the AI SDK. | Topics: ai-sdk-core, skill-uploads

- [Speech](/docs/ai-sdk-core/speech) | Type: Conceptual | Summary: Learn how to generate speech from text with the AI SDK. | Topics: ai-sdk-core, speech

- [Telemetry](/docs/ai-sdk-core/telemetry) | Type: Conceptual | Summary: Using OpenTelemetry with AI SDK Core | Topics: ai-sdk-core, telemetry

- [Testing](/docs/ai-sdk-core/testing) | Type: Conceptual | Summary: Learn how to use AI SDK Core mock providers for testing. | Topics: ai-sdk-core, testing

- [Tool Search](/docs/ai-sdk-core/tool-search) | Type: Conceptual | Summary: Let models discover tools on demand, with direct calling or cache-preserving code mode. | Topics: ai-sdk-core, tool-search

- [Tool Calling](/docs/ai-sdk-core/tools-and-tool-calling) | Type: Conceptual | Summary: Learn about tool calling and multi-step calls (using stopWhen) with AI SDK Core. | Topics: ai-sdk-core, tools-and-tool-calling

- [Transcription](/docs/ai-sdk-core/transcription) | Type: Conceptual | Summary: Learn how to transcribe audio with the AI SDK. | Topics: ai-sdk-core, transcription

- [Translation](/docs/ai-sdk-core/translation) | Type: Conceptual | Summary: Learn how to translate speech with the AI SDK. | Topics: ai-sdk-core, translation

- [Video Generation](/docs/ai-sdk-core/video-generation) | Type: Conceptual | Summary: Learn how to generate videos with the AI SDK. | Topics: ai-sdk-core, video-generation

- [Harness Adapters](/docs/ai-sdk-harnesses/harness-adapters) | Type: Conceptual | Summary: Learn about the available AI SDK harness adapters. | Topics: ai-sdk-harnesses, harness-adapters

- [HarnessAgent](/docs/ai-sdk-harnesses/harness-agent) | Type: Conceptual | Summary: Create and run AI SDK HarnessAgent sessions. | Topics: ai-sdk-harnesses, harness-agent

- [Overview](/docs/ai-sdk-harnesses/overview) | Type: Conceptual | Summary: Learn what AI SDK harnesses are and how they fit into the AI SDK. | Topics: ai-sdk-harnesses, overview

- [Skills](/docs/ai-sdk-harnesses/skills) | Type: Conceptual | Summary: Use skills with AI SDK harnesses. | Topics: ai-sdk-harnesses, skills

- [Terminal UI](/docs/ai-sdk-harnesses/terminal-ui) | Type: Conceptual | Summary: Use @ai-sdk/tui with HarnessAgent. | Topics: ai-sdk-harnesses, terminal-ui

- [Tools](/docs/ai-sdk-harnesses/tools) | Type: Conceptual | Summary: Use tools with AI SDK harnesses. | Topics: ai-sdk-harnesses, tools

- [UI](/docs/ai-sdk-harnesses/ui) | Type: Conceptual | Summary: Use AI SDK harnesses with useChat. | Topics: ai-sdk-harnesses, ui

- [Workflow Utilities](/docs/ai-sdk-harnesses/workflow-utilities) | Type: Conceptual | Summary: Run HarnessAgent turns as durable Workflow DevKit workflows. | Topics: ai-sdk-harnesses, workflow-utilities

- [Handling Authentication](/docs/ai-sdk-rsc/authentication) | Type: Conceptual | Summary: Learn how to authenticate with the AI SDK. | Topics: ai-sdk-rsc, authentication

- [Error Handling](/docs/ai-sdk-rsc/error-handling) | Type: Conceptual | Summary: Learn how to handle errors with the AI SDK. | Topics: ai-sdk-rsc, error-handling

- [Managing Generative UI State](/docs/ai-sdk-rsc/generative-ui-state) | Type: Conceptual | Summary: Overview of the AI and UI states | Topics: ai-sdk-rsc, generative-ui-state

- [Handling Loading State](/docs/ai-sdk-rsc/loading-state) | Type: Conceptual | Summary: Overview of handling loading state with AI SDK RSC | Topics: ai-sdk-rsc, loading-state

- [Migrating from RSC to UI](/docs/ai-sdk-rsc/migrating-to-ui) | Type: Conceptual | Summary: Learn how to migrate from AI SDK RSC to AI SDK UI. | Topics: ai-sdk-rsc, migrating-to-ui

- [Multistep Interfaces](/docs/ai-sdk-rsc/multistep-interfaces) | Type: Conceptual | Summary: Overview of Building Multistep Interfaces with AI SDK RSC | Topics: ai-sdk-rsc, multistep-interfaces

- [Overview](/docs/ai-sdk-rsc/overview) | Type: Conceptual | Summary: An overview of AI SDK RSC. | Topics: ai-sdk-rsc, overview

- [Saving and Restoring States](/docs/ai-sdk-rsc/saving-and-restoring-states) | Type: Conceptual | Summary: Saving and restoring AI and UI states with onGetUIState and onSetAIState | Topics: ai-sdk-rsc, saving-and-restoring-states

- [Streaming React Components](/docs/ai-sdk-rsc/streaming-react-components) | Type: Conceptual | Summary: Overview of streaming RSCs | Topics: ai-sdk-rsc, streaming-react-components

- [Streaming Values](/docs/ai-sdk-rsc/streaming-values) | Type: Conceptual | Summary: Overview of streaming RSCs | Topics: ai-sdk-rsc, streaming-values

- [Chatbot](/docs/ai-sdk-ui/chatbot) | Type: Conceptual | Summary: Learn how to use the useChat hook. | Topics: ai-sdk-ui, chatbot

- [Chatbot Message Persistence](/docs/ai-sdk-ui/chatbot-message-persistence) | Type: Conceptual | Summary: Learn how to store and load chat messages in a chatbot. | Topics: ai-sdk-ui, chatbot-message-persistence

- [Chatbot Resume Streams](/docs/ai-sdk-ui/chatbot-resume-streams) | Type: Conceptual | Summary: Learn how to resume chatbot streams after client disconnects. | Topics: ai-sdk-ui, chatbot-resume-streams

- [Chatbot Tool Usage](/docs/ai-sdk-ui/chatbot-tool-usage) | Type: Conceptual | Summary: Learn how to use tools with the useChat hook. | Topics: ai-sdk-ui, chatbot-tool-usage

- [Completion](/docs/ai-sdk-ui/completion) | Type: Conceptual | Summary: Learn how to use the useCompletion hook. | Topics: ai-sdk-ui, completion

- [Error Handling](/docs/ai-sdk-ui/error-handling) | Type: Conceptual | Summary: Learn how to handle errors in the AI SDK UI | Topics: ai-sdk-ui, error-handling

- [Generative User Interfaces](/docs/ai-sdk-ui/generative-user-interfaces) | Type: Conceptual | Summary: Learn how to build Generative UI with AI SDK UI. | Topics: ai-sdk-ui, generative-user-interfaces

- [Message Metadata](/docs/ai-sdk-ui/message-metadata) | Type: Conceptual | Summary: Learn how to attach and use metadata with messages in AI SDK UI | Topics: ai-sdk-ui, message-metadata

- [Object Generation](/docs/ai-sdk-ui/object-generation) | Type: Conceptual | Summary: Learn how to use the useObject hook. | Topics: ai-sdk-ui, object-generation

- [Overview](/docs/ai-sdk-ui/overview) | Type: Conceptual | Summary: An overview of AI SDK UI. | Topics: ai-sdk-ui, overview

- [Reading UIMessage Streams](/docs/ai-sdk-ui/reading-ui-message-streams) | Type: Conceptual | Summary: Learn how to read UIMessage streams. | Topics: ai-sdk-ui, reading-ui-message-streams

- [Stream Protocols](/docs/ai-sdk-ui/stream-protocol) | Type: Conceptual | Summary: Learn more about the supported stream protocols in the AI SDK. | Topics: ai-sdk-ui, stream-protocol

- [Streaming Custom Data](/docs/ai-sdk-ui/streaming-data) | Type: Conceptual | Summary: Learn how to stream custom data from the server to the client. | Topics: ai-sdk-ui, streaming-data

- [Transport](/docs/ai-sdk-ui/transport) | Type: Conceptual | Summary: Learn how to use custom transports with useChat. | Topics: ai-sdk-ui, transport

- [Overview](/docs/foundations/overview) | Type: Conceptual | Summary: An overview of foundational concepts critical to understanding the AI SDK | Topics: foundations, overview

- [Prompts](/docs/foundations/prompts) | Type: Conceptual | Summary: Learn about the Prompt structure used in the AI SDK. | Topics: foundations, prompts

- [Provider Options](/docs/foundations/provider-options) | Type: Conceptual | Summary: Learn how to use provider-specific options to control reasoning, caching, and other advanced features. | Topics: foundations, provider-options

- [Providers and Models](/docs/foundations/providers-and-models) | Type: Conceptual | Summary: Learn about the providers and models available in the AI SDK. | Topics: foundations, providers-and-models

- [Streaming](/docs/foundations/streaming) | Type: Conceptual | Summary: Why use streaming for AI applications? | Topics: foundations, streaming

- [Tools](/docs/foundations/tools) | Type: Conceptual | Summary: Learn about tools with the AI SDK. | Topics: foundations, tools

- [Getting Started](/docs/getting-started) | Type: Guide | Summary: Welcome to the AI SDK documentation! | Topics: getting-started

    - [Choosing a Provider](/docs/getting-started/choosing-a-provider) | Type: Guide | Summary: Learn how to configure and authenticate with AI providers in the AI SDK. | Prerequisites: /docs/getting-started | Topics: getting-started, choosing-a-provider

    - [Coding Agents](/docs/getting-started/coding-agents) | Type: Guide | Summary: Learn how to set up the AI SDK for use with coding agents, including installing skills, accessing bundled docs, and using DevTools. | Prerequisites: /docs/getting-started | Topics: getting-started, coding-agents

    - [Expo](/docs/getting-started/expo) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Expo. | Prerequisites: /docs/getting-started | Topics: getting-started, expo

    - [Navigating the Library](/docs/getting-started/navigating-the-library) | Type: Guide | Summary: Learn how to navigate the AI SDK. | Prerequisites: /docs/getting-started | Topics: getting-started, navigating-the-library

    - [Next.js App Router](/docs/getting-started/nextjs-app-router) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Next.js App Router. | Prerequisites: /docs/getting-started | Topics: getting-started, nextjs-app-router

    - [Next.js Pages Router](/docs/getting-started/nextjs-pages-router) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Next.js Pages Router. | Prerequisites: /docs/getting-started | Topics: getting-started, nextjs-pages-router

    - [Node.js](/docs/getting-started/nodejs) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Node.js. | Prerequisites: /docs/getting-started | Topics: getting-started, nodejs

    - [Vue.js (Nuxt)](/docs/getting-started/nuxt) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Vue.js (Nuxt). | Prerequisites: /docs/getting-started | Topics: getting-started, nuxt

    - [Svelte](/docs/getting-started/svelte) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and Svelte. | Prerequisites: /docs/getting-started | Topics: getting-started, svelte

    - [TanStack Start](/docs/getting-started/tanstack-start) | Type: Guide | Summary: Learn how to build your first agent with the AI SDK and TanStack Start. | Prerequisites: /docs/getting-started | Topics: getting-started, tanstack-start

- [AI SDK by Vercel](/docs/introduction) | Type: Conceptual | Summary: The AI SDK is the TypeScript toolkit for building AI applications and agents with React, Next.js, Vue, Svelte, Node.js, and more. | Topics: introduction

- [Migration Guides](/docs/migration-guides) | Type: Conceptual | Summary: Learn how to upgrade between Vercel AI versions. | Topics: migration-guides

    - [Migrate AI SDK 3.0 to 3.1](/docs/migration-guides/migration-guide-3-1) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.0 to 3.1. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-3-1

    - [Migrate AI SDK 3.1 to 3.2](/docs/migration-guides/migration-guide-3-2) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.1 to 3.2. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-3-2

    - [Migrate AI SDK 3.2 to 3.3](/docs/migration-guides/migration-guide-3-3) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.2 to 3.3. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-3-3

    - [Migrate AI SDK 3.3 to 3.4](/docs/migration-guides/migration-guide-3-4) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.3 to 3.4. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-3-4

    - [Migrate AI SDK 3.4 to 4.0](/docs/migration-guides/migration-guide-4-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 3.4 to 4.0. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-4-0

    - [Migrate AI SDK 4.0 to 4.1](/docs/migration-guides/migration-guide-4-1) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.0 to 4.1. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-4-1

    - [Migrate AI SDK 4.1 to 4.2](/docs/migration-guides/migration-guide-4-2) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.1 to 4.2. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-4-2

    - [Migrate AI SDK 4.x to 5.0](/docs/migration-guides/migration-guide-5-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 4.x to 5.0. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-5-0

    - [Migrate Your Data to AI SDK 5.0](/docs/migration-guides/migration-guide-5-0-data) | Type: Conceptual | Summary: Learn how to migrate your persisted messages and chat data from AI SDK 4.x to 5.0. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-5-0-data

    - [Migrate AI SDK 5.x to 6.0](/docs/migration-guides/migration-guide-6-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 5.x to 6.0. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-6-0

    - [Migrate AI SDK 6.x to 7.0](/docs/migration-guides/migration-guide-7-0) | Type: Conceptual | Summary: Learn how to upgrade AI SDK 6.x to 7.0. | Prerequisites: /docs/migration-guides | Topics: migration-guides, migration-guide-7-0

    - [Versioning](/docs/migration-guides/versioning) | Type: Conceptual | Summary: Understand how the AI SDK approaches versioning. | Prerequisites: /docs/migration-guides | Topics: migration-guides, versioning

- [Reference](/docs/reference) | Type: Reference | Summary: Reference documentation for the AI SDK | Topics: reference

    - [AI SDK Core](/docs/reference/ai-sdk-core) | Type: Reference | Summary: Reference documentation for the AI SDK Core | Prerequisites: /docs/reference | Topics: reference, ai-sdk-core

        - [addToolInputExamplesMiddleware](/docs/reference/ai-sdk-core/add-tool-input-examples-middleware) | Type: Reference | Summary: Middleware that appends tool input examples to tool descriptions. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, add-tool-input-examples-middleware

        - [Agent (Interface)](/docs/reference/ai-sdk-core/agent) | Type: Reference | Summary: API Reference for the Agent interface. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, agent

        - [experimental_cancelBatch](/docs/reference/ai-sdk-core/cancel-batch) | Type: Reference | Summary: API Reference for experimental_cancelBatch. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, cancel-batch

        - [cosineSimilarity](/docs/reference/ai-sdk-core/cosine-similarity) | Type: Reference | Summary: Calculate the cosine similarity between two vectors (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, cosine-similarity

        - [createAgentUIStream](/docs/reference/ai-sdk-core/create-agent-ui-stream) | Type: Reference | Summary: API Reference for the createAgentUIStream utility. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, create-agent-ui-stream

        - [createAgentUIStreamResponse](/docs/reference/ai-sdk-core/create-agent-ui-stream-response) | Type: Reference | Summary: API Reference for the createAgentUIStreamResponse utility. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, create-agent-ui-stream-response

        - [createIdGenerator](/docs/reference/ai-sdk-core/create-id-generator) | Type: Reference | Summary: Create a customizable unique identifier generator (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, create-id-generator

        - [createMCPClient](/docs/reference/ai-sdk-core/create-mcp-client) | Type: Reference | Summary: Create a client for connecting to MCP servers | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, create-mcp-client

        - [customProvider](/docs/reference/ai-sdk-core/custom-provider) | Type: Reference | Summary: Custom provider that uses models from a different provider (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, custom-provider

        - [experimental_decide](/docs/reference/ai-sdk-core/decide) | Type: Reference | Summary: Decide answers to typed questions against shared state with a decision model. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, decide

        - [DefaultGeneratedFile](/docs/reference/ai-sdk-core/default-generated-file) | Type: Reference | Summary: API Reference for DefaultGeneratedFile. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, default-generated-file

        - [defaultInstructionsMiddleware](/docs/reference/ai-sdk-core/default-instructions-middleware) | Type: Reference | Summary: Middleware that applies default instructions to language model calls | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, default-instructions-middleware

        - [defaultSettingsMiddleware](/docs/reference/ai-sdk-core/default-settings-middleware) | Type: Reference | Summary: Middleware that applies default settings for language models | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, default-settings-middleware

        - [dynamicTool](/docs/reference/ai-sdk-core/dynamic-tool) | Type: Reference | Summary: Helper function for creating dynamic tools with unknown types | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, dynamic-tool

        - [embed](/docs/reference/ai-sdk-core/embed) | Type: Reference | Summary: API Reference for embed. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, embed

        - [embedMany](/docs/reference/ai-sdk-core/embed-many) | Type: Reference | Summary: API Reference for embedMany. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, embed-many

        - [extractJsonMiddleware](/docs/reference/ai-sdk-core/extract-json-middleware) | Type: Reference | Summary: Middleware that extracts JSON from text content by stripping markdown code fences | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, extract-json-middleware

        - [extractReasoningMiddleware](/docs/reference/ai-sdk-core/extract-reasoning-middleware) | Type: Reference | Summary: Middleware that extracts reasoning sections from generated text using configurable delimiters | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, extract-reasoning-middleware

        - [filterActiveTools](/docs/reference/ai-sdk-core/filter-active-tools) | Type: Reference | Summary: Filter a tool set to the currently active tools (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, filter-active-tools

        - [generateId](/docs/reference/ai-sdk-core/generate-id) | Type: Reference | Summary: Generate a unique identifier (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, generate-id

        - [generateImage](/docs/reference/ai-sdk-core/generate-image) | Type: Reference | Summary: API Reference for generateImage. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, generate-image

        - [generateSpeech](/docs/reference/ai-sdk-core/generate-speech) | Type: Reference | Summary: API Reference for generateSpeech. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, generate-speech

        - [generateText](/docs/reference/ai-sdk-core/generate-text) | Type: Reference | Summary: API Reference for generateText. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, generate-text

        - [experimental_generateVideo](/docs/reference/ai-sdk-core/generate-video) | Type: Reference | Summary: API Reference for experimental_generateVideo. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, generate-video

        - [experimental_getBatchResults](/docs/reference/ai-sdk-core/get-batch-results) | Type: Reference | Summary: API Reference for experimental_getBatchResults. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, get-batch-results

        - [experimental_getBatchStatus](/docs/reference/ai-sdk-core/get-batch-status) | Type: Reference | Summary: API Reference for experimental_getBatchStatus. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, get-batch-status

        - [experimental_getRealtimeToolDefinitions](/docs/reference/ai-sdk-core/get-realtime-tool-definitions) | Type: Reference | Summary: API reference for experimental_getRealtimeToolDefinitions. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, get-realtime-tool-definitions

        - [hasToolCall](/docs/reference/ai-sdk-core/has-tool-call) | Type: Reference | Summary: API Reference for hasToolCall. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, has-tool-call

        - [isStepCount](/docs/reference/ai-sdk-core/is-step-count) | Type: Reference | Summary: API Reference for isStepCount. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, is-step-count

        - [jsonSchema](/docs/reference/ai-sdk-core/json-schema) | Type: Reference | Summary: Helper function for creating JSON schemas | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, json-schema

        - [LanguageModelV4Middleware](/docs/reference/ai-sdk-core/language-model-v2-middleware) | Type: Reference | Summary: Middleware for enhancing language model behavior (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, language-model-v2-middleware

        - [experimental_listBatches](/docs/reference/ai-sdk-core/list-batches) | Type: Reference | Summary: API Reference for experimental_listBatches. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, list-batches

        - [isLoopFinished](/docs/reference/ai-sdk-core/loop-finished) | Type: Reference | Summary: API Reference for isLoopFinished. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, loop-finished

        - [MCP Apps](/docs/reference/ai-sdk-core/mcp-apps) | Type: Reference | Summary: API reference for MCP Apps helpers in @ai-sdk/mcp. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, mcp-apps

        - [MCP Events](/docs/reference/ai-sdk-core/mcp-events) | Type: Reference | Summary: Reference for experimental MCP event methods, the webhook handler, and subscription and storage types. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, mcp-events

        - [Experimental_StdioMCPTransport](/docs/reference/ai-sdk-core/mcp-stdio-transport) | Type: Reference | Summary: Create a transport for Model Context Protocol (MCP) clients to communicate with MCP servers using standard input and output streams | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, mcp-stdio-transport

        - [ModelMessage](/docs/reference/ai-sdk-core/model-message) | Type: Reference | Summary: Message types for AI SDK Core (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, model-message

        - [Output](/docs/reference/ai-sdk-core/output) | Type: Reference | Summary: API Reference for Output. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, output

        - [pipeAgentUIStreamToResponse](/docs/reference/ai-sdk-core/pipe-agent-ui-stream-to-response) | Type: Reference | Summary: API Reference for the pipeAgentUIStreamToResponse utility. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, pipe-agent-ui-stream-to-response

        - [createProviderRegistry](/docs/reference/ai-sdk-core/provider-registry) | Type: Reference | Summary: Registry for managing multiple providers and models (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, provider-registry

        - [rerank](/docs/reference/ai-sdk-core/rerank) | Type: Reference | Summary: API Reference for rerank. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, rerank

        - [safeValidateUIMessages](/docs/reference/ai-sdk-core/safe-validate-ui-messages) | Type: Reference | Summary: API Reference for safeValidateUIMessages | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, safe-validate-ui-messages

        - [Experimental_SandboxSession](/docs/reference/ai-sdk-core/sandbox) | Type: Reference | Summary: API Reference for the Experimental_SandboxSession interface. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, sandbox

        - [simulateReadableStream](/docs/reference/ai-sdk-core/simulate-readable-stream) | Type: Reference | Summary: Create a ReadableStream that emits values with configurable delays | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, simulate-readable-stream

        - [simulateStreamingMiddleware](/docs/reference/ai-sdk-core/simulate-streaming-middleware) | Type: Reference | Summary: Middleware that simulates streaming for non-streaming language models | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, simulate-streaming-middleware

        - [smoothStream](/docs/reference/ai-sdk-core/smooth-stream) | Type: Reference | Summary: Stream transformer for smoothing text and reasoning output | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, smooth-stream

        - [experimental_startBatch](/docs/reference/ai-sdk-core/start-batch) | Type: Reference | Summary: API Reference for experimental_startBatch. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, start-batch

        - [streamText](/docs/reference/ai-sdk-core/stream-text) | Type: Reference | Summary: API Reference for streamText. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, stream-text

        - [experimental_streamTranscribe](/docs/reference/ai-sdk-core/stream-transcribe) | Type: Reference | Summary: API Reference for experimental_streamTranscribe. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, stream-transcribe

        - [experimental_streamTranslate](/docs/reference/ai-sdk-core/stream-translate) | Type: Reference | Summary: API Reference for experimental_streamTranslate. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, stream-translate

        - [tool](/docs/reference/ai-sdk-core/tool) | Type: Reference | Summary: Helper function for tool type inference | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, tool

        - [ToolLoopAgent](/docs/reference/ai-sdk-core/tool-loop-agent) | Type: Reference | Summary: API Reference for the ToolLoopAgent class. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, tool-loop-agent

        - [toolSearch](/docs/reference/ai-sdk-core/tool-search) | Type: Reference | Summary: Search deferred tools and load their definitions on demand for direct calling or code mode. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, tool-search

        - [transcribe](/docs/reference/ai-sdk-core/transcribe) | Type: Reference | Summary: API Reference for transcribe. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, transcribe

        - [UIMessage](/docs/reference/ai-sdk-core/ui-message) | Type: Reference | Summary: API Reference for UIMessage | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, ui-message

        - [uploadFile](/docs/reference/ai-sdk-core/upload-file) | Type: Reference | Summary: API Reference for uploadFile. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, upload-file

        - [uploadSkill](/docs/reference/ai-sdk-core/upload-skill) | Type: Reference | Summary: API Reference for uploadSkill. | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, upload-skill

        - [valibotSchema](/docs/reference/ai-sdk-core/valibot-schema) | Type: Reference | Summary: Helper function for creating Valibot schemas | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, valibot-schema

        - [validateUIMessages](/docs/reference/ai-sdk-core/validate-ui-messages) | Type: Reference | Summary: API Reference for validateUIMessages | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, validate-ui-messages

        - [wrapImageModel](/docs/reference/ai-sdk-core/wrap-image-model) | Type: Reference | Summary: Function for wrapping an image model with middleware (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, wrap-image-model

        - [wrapLanguageModel](/docs/reference/ai-sdk-core/wrap-language-model) | Type: Reference | Summary: Function for wrapping a language model with middleware (API Reference) | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, wrap-language-model

        - [zodSchema](/docs/reference/ai-sdk-core/zod-schema) | Type: Reference | Summary: Helper function for creating Zod schemas | Prerequisites: /docs/reference/ai-sdk-core | Topics: reference, ai-sdk-core, zod-schema

    - [AI SDK Errors](/docs/reference/ai-sdk-errors) | Type: Reference | Summary: Reference for AI SDK error classes and typed error handling. | Prerequisites: /docs/reference | Topics: reference, ai-sdk-errors

        - [AI_APICallError](/docs/reference/ai-sdk-errors/ai-api-call-error) | Type: Reference | Summary: Learn how to fix AI_APICallError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-api-call-error

        - [AI_DecisionRefusalError](/docs/reference/ai-sdk-errors/ai-decision-refusal-error) | Type: Reference | Summary: Identify decision questions that a model declined to answer. | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-decision-refusal-error

        - [AI_DecisionUnsupportedQuestionTypeError](/docs/reference/ai-sdk-errors/ai-decision-unsupported-question-type-error) | Type: Reference | Summary: Identify a decision question type that a model does not support. | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-decision-unsupported-question-type-error

        - [AI_DownloadError](/docs/reference/ai-sdk-errors/ai-download-error) | Type: Reference | Summary: Learn how to fix AI_DownloadError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-download-error

        - [AI_EmptyResponseBodyError](/docs/reference/ai-sdk-errors/ai-empty-response-body-error) | Type: Reference | Summary: Learn how to fix AI_EmptyResponseBodyError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-empty-response-body-error

        - [AI_InvalidArgumentError](/docs/reference/ai-sdk-errors/ai-invalid-argument-error) | Type: Reference | Summary: Learn how to fix AI_InvalidArgumentError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-argument-error

        - [AI_InvalidDataContentError](/docs/reference/ai-sdk-errors/ai-invalid-data-content-error) | Type: Reference | Summary: How to fix AI_InvalidDataContentError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-data-content-error

        - [AI_InvalidMessageRoleError](/docs/reference/ai-sdk-errors/ai-invalid-message-role-error) | Type: Reference | Summary: Learn how to fix AI_InvalidMessageRoleError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-message-role-error

        - [AI_InvalidPromptError](/docs/reference/ai-sdk-errors/ai-invalid-prompt-error) | Type: Reference | Summary: Learn how to fix AI_InvalidPromptError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-prompt-error

        - [AI_InvalidResponseDataError](/docs/reference/ai-sdk-errors/ai-invalid-response-data-error) | Type: Reference | Summary: Learn how to fix AI_InvalidResponseDataError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-response-data-error

        - [AI_InvalidToolApprovalError](/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolApprovalError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-tool-approval-error

        - [AI_InvalidToolApprovalSignatureError](/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-signature-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolApprovalSignatureError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-tool-approval-signature-error

        - [AI_InvalidToolInputError](/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error) | Type: Reference | Summary: Learn how to fix AI_InvalidToolInputError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-invalid-tool-input-error

        - [AI_JSONParseError](/docs/reference/ai-sdk-errors/ai-json-parse-error) | Type: Reference | Summary: Learn how to fix AI_JSONParseError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-json-parse-error

        - [AI_LoadAPIKeyError](/docs/reference/ai-sdk-errors/ai-load-api-key-error) | Type: Reference | Summary: Learn how to fix AI_LoadAPIKeyError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-load-api-key-error

        - [AI_LoadSettingError](/docs/reference/ai-sdk-errors/ai-load-setting-error) | Type: Reference | Summary: Learn how to fix AI_LoadSettingError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-load-setting-error

        - [AI_MessageConversionError](/docs/reference/ai-sdk-errors/ai-message-conversion-error) | Type: Reference | Summary: Learn how to fix AI_MessageConversionError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-message-conversion-error

        - [AI_NoContentGeneratedError](/docs/reference/ai-sdk-errors/ai-no-content-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoContentGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-content-generated-error

        - [AI_NoImageGeneratedError](/docs/reference/ai-sdk-errors/ai-no-image-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoImageGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-image-generated-error

        - [AI_NoObjectGeneratedError](/docs/reference/ai-sdk-errors/ai-no-object-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoObjectGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-object-generated-error

        - [AI_NoOutputGeneratedError](/docs/reference/ai-sdk-errors/ai-no-output-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoOutputGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-output-generated-error

        - [AI_NoSpeechGeneratedError](/docs/reference/ai-sdk-errors/ai-no-speech-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoSpeechGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-speech-generated-error

        - [AI_NoSuchModelError](/docs/reference/ai-sdk-errors/ai-no-such-model-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchModelError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-such-model-error

        - [AI_NoSuchProviderError](/docs/reference/ai-sdk-errors/ai-no-such-provider-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchProviderError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-such-provider-error

        - [AI_NoSuchProviderReferenceError](/docs/reference/ai-sdk-errors/ai-no-such-provider-reference-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchProviderReferenceError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-such-provider-reference-error

        - [AI_NoSuchToolError](/docs/reference/ai-sdk-errors/ai-no-such-tool-error) | Type: Reference | Summary: Learn how to fix AI_NoSuchToolError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-such-tool-error

        - [AI_NoTranscriptGeneratedError](/docs/reference/ai-sdk-errors/ai-no-transcript-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoTranscriptGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-transcript-generated-error

        - [AI_NoTranslationGeneratedError](/docs/reference/ai-sdk-errors/ai-no-translation-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoTranslationGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-translation-generated-error

        - [AI_NoVideoGeneratedError](/docs/reference/ai-sdk-errors/ai-no-video-generated-error) | Type: Reference | Summary: Learn how to fix AI_NoVideoGeneratedError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-no-video-generated-error

        - [AI_RetryError](/docs/reference/ai-sdk-errors/ai-retry-error) | Type: Reference | Summary: Learn how to fix AI_RetryError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-retry-error

        - [AI_StreamProviderError](/docs/reference/ai-sdk-errors/ai-stream-provider-error) | Type: Reference | Summary: Learn how to handle AI_StreamProviderError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-stream-provider-error

        - [AI_TooManyEmbeddingValuesForCallError](/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error) | Type: Reference | Summary: Learn how to fix AI_TooManyEmbeddingValuesForCallError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-too-many-embedding-values-for-call-error

        - [AI_ToolCallNotFoundForApprovalError](/docs/reference/ai-sdk-errors/ai-tool-call-not-found-for-approval-error) | Type: Reference | Summary: Learn how to fix AI_ToolCallNotFoundForApprovalError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-tool-call-not-found-for-approval-error

        - [ToolCallRepairError](/docs/reference/ai-sdk-errors/ai-tool-call-repair-error) | Type: Reference | Summary: Learn how to fix AI SDK ToolCallRepairError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-tool-call-repair-error

        - [ToolChoiceViolationError](/docs/reference/ai-sdk-errors/ai-tool-choice-violation-error) | Type: Reference | Summary: Learn how to fix AI SDK ToolChoiceViolationError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-tool-choice-violation-error

        - [AI_TypeValidationError](/docs/reference/ai-sdk-errors/ai-type-validation-error) | Type: Reference | Summary: Learn how to fix AI_TypeValidationError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-type-validation-error

        - [AI_UIMessageStreamError](/docs/reference/ai-sdk-errors/ai-ui-message-stream-error) | Type: Reference | Summary: Learn how to fix AI_UIMessageStreamError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-ui-message-stream-error

        - [AI_UnsupportedFunctionalityError](/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error) | Type: Reference | Summary: Learn how to fix AI_UnsupportedFunctionalityError | Prerequisites: /docs/reference/ai-sdk-errors | Topics: reference, ai-sdk-errors, ai-unsupported-functionality-error

    - [AI SDK RSC](/docs/reference/ai-sdk-rsc) | Type: Reference | Summary: Reference documentation for the AI SDK RSC | Prerequisites: /docs/reference | Topics: reference, ai-sdk-rsc

        - [createAI](/docs/reference/ai-sdk-rsc/create-ai) | Type: Reference | Summary: Reference for the createAI function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, create-ai

        - [createStreamableUI](/docs/reference/ai-sdk-rsc/create-streamable-ui) | Type: Reference | Summary: Reference for the createStreamableUI function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, create-streamable-ui

        - [createStreamableValue](/docs/reference/ai-sdk-rsc/create-streamable-value) | Type: Reference | Summary: Reference for the createStreamableValue function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, create-streamable-value

        - [getAIState](/docs/reference/ai-sdk-rsc/get-ai-state) | Type: Reference | Summary: Reference for the getAIState function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, get-ai-state

        - [getMutableAIState](/docs/reference/ai-sdk-rsc/get-mutable-ai-state) | Type: Reference | Summary: Reference for the getMutableAIState function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, get-mutable-ai-state

        - [readStreamableValue](/docs/reference/ai-sdk-rsc/read-streamable-value) | Type: Reference | Summary: Reference for the readStreamableValue function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, read-streamable-value

        - [render (Removed)](/docs/reference/ai-sdk-rsc/render) | Type: Reference | Summary: Reference for the render function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, render

        - [streamUI](/docs/reference/ai-sdk-rsc/stream-ui) | Type: Reference | Summary: Reference for the streamUI function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, stream-ui

        - [useActions](/docs/reference/ai-sdk-rsc/use-actions) | Type: Reference | Summary: Reference for the useActions function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, use-actions

        - [useAIState](/docs/reference/ai-sdk-rsc/use-ai-state) | Type: Reference | Summary: Reference for the useAIState function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, use-ai-state

        - [useStreamableValue](/docs/reference/ai-sdk-rsc/use-streamable-value) | Type: Reference | Summary: Reference for the useStreamableValue function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, use-streamable-value

        - [useUIState](/docs/reference/ai-sdk-rsc/use-ui-state) | Type: Reference | Summary: Reference for the useUIState function from the AI SDK RSC | Prerequisites: /docs/reference/ai-sdk-rsc | Topics: reference, ai-sdk-rsc, use-ui-state

    - [AI SDK TUI](/docs/reference/ai-sdk-tui) | Type: Reference | Summary: Reference documentation for @ai-sdk/tui | Prerequisites: /docs/reference | Topics: reference, ai-sdk-tui

        - [runAgentTUI](/docs/reference/ai-sdk-tui/run-agent-tui) | Type: Reference | Summary: API Reference for the runAgentTUI function. | Prerequisites: /docs/reference/ai-sdk-tui | Topics: reference, ai-sdk-tui, run-agent-tui

    - [AI SDK UI](/docs/reference/ai-sdk-ui) | Type: Reference | Summary: Reference documentation for the AI SDK UI | Prerequisites: /docs/reference | Topics: reference, ai-sdk-ui

        - [convertToModelMessages](/docs/reference/ai-sdk-ui/convert-to-model-messages) | Type: Reference | Summary: Convert useChat messages to ModelMessages for AI functions (API Reference) | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, convert-to-model-messages

        - [createUIMessageStream](/docs/reference/ai-sdk-ui/create-ui-message-stream) | Type: Reference | Summary: API Reference for createUIMessageStream. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, create-ui-message-stream

        - [createUIMessageStreamResponse](/docs/reference/ai-sdk-ui/create-ui-message-stream-response) | Type: Reference | Summary: API Reference for createUIMessageStreamResponse. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, create-ui-message-stream-response

        - [DirectChatTransport](/docs/reference/ai-sdk-ui/direct-chat-transport) | Type: Reference | Summary: API Reference for the DirectChatTransport class. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, direct-chat-transport

        - [InferUITool](/docs/reference/ai-sdk-ui/infer-ui-tool) | Type: Reference | Summary: API Reference for InferUITool. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, infer-ui-tool

        - [InferUITools](/docs/reference/ai-sdk-ui/infer-ui-tools) | Type: Reference | Summary: API Reference for InferUITools. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, infer-ui-tools

        - [experimental_MCPAppRenderer](/docs/reference/ai-sdk-ui/mcp-app-renderer) | Type: Reference | Summary: API reference for rendering MCP Apps with @ai-sdk/react. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, mcp-app-renderer

        - [pipeUIMessageStreamToResponse](/docs/reference/ai-sdk-ui/pipe-ui-message-stream-to-response) | Type: Reference | Summary: Learn to use pipeUIMessageStreamToResponse helper function to pipe streaming data to a ServerResponse object. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, pipe-ui-message-stream-to-response

        - [pruneMessages](/docs/reference/ai-sdk-ui/prune-messages) | Type: Reference | Summary: API Reference for pruneMessages. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, prune-messages

        - [readUIMessageStream](/docs/reference/ai-sdk-ui/read-ui-message-stream) | Type: Reference | Summary: API Reference for readUIMessageStream. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, read-ui-message-stream

        - [useChat](/docs/reference/ai-sdk-ui/use-chat) | Type: Reference | Summary: API reference for the useChat hook. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, use-chat

        - [useCompletion](/docs/reference/ai-sdk-ui/use-completion) | Type: Reference | Summary: API reference for the useCompletion hook. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, use-completion

        - [useObject](/docs/reference/ai-sdk-ui/use-object) | Type: Reference | Summary: API reference for the useObject hook. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, use-object

        - [experimental_useRealtime](/docs/reference/ai-sdk-ui/use-realtime) | Type: Reference | Summary: API reference for the experimental_useRealtime hook. | Prerequisites: /docs/reference/ai-sdk-ui | Topics: reference, ai-sdk-ui, use-realtime

    - [AI SDK Workflow](/docs/reference/ai-sdk-workflow) | Type: Reference | Summary: Reference documentation for @ai-sdk/workflow | Prerequisites: /docs/reference | Topics: reference, ai-sdk-workflow

        - [generateVideo](/docs/reference/ai-sdk-workflow/generate-video) | Type: Reference | Summary: API Reference for durable video generation in workflows. | Prerequisites: /docs/reference/ai-sdk-workflow | Topics: reference, ai-sdk-workflow, generate-video

        - [WorkflowAgent](/docs/reference/ai-sdk-workflow/workflow-agent) | Type: Reference | Summary: API Reference for the WorkflowAgent class. | Prerequisites: /docs/reference/ai-sdk-workflow | Topics: reference, ai-sdk-workflow, workflow-agent

        - [WorkflowChatTransport](/docs/reference/ai-sdk-workflow/workflow-chat-transport) | Type: Reference | Summary: API Reference for the WorkflowChatTransport class. | Prerequisites: /docs/reference/ai-sdk-workflow | Topics: reference, ai-sdk-workflow, workflow-chat-transport

- [Troubleshooting](/docs/troubleshooting) | Type: Conceptual | Summary: Troubleshooting information for common issues encountered with the AI SDK. | Topics: troubleshooting

    - [Abort and resumable streams](/docs/troubleshooting/abort-breaks-resumable-streams) | Type: Conceptual | Summary: Troubleshooting abort and stop behavior with resumable streams | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, abort-breaks-resumable-streams

    - [Azure OpenAI Slow to Stream](/docs/troubleshooting/azure-stream-slow) | Type: Conceptual | Summary: Learn to troubleshoot Azure OpenAI slow to stream issues. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, azure-stream-slow

    - [Server Action Plain Objects Error](/docs/troubleshooting/client-stream-error) | Type: Conceptual | Summary: Troubleshooting errors related to using AI SDK Core functions with Server Actions. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, client-stream-error

    - [High memory usage when processing many images](/docs/troubleshooting/high-memory-usage-with-images) | Type: Conceptual | Summary: Troubleshooting high memory usage when using generateText or streamText with many images | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, high-memory-usage-with-images

    - [Jest: cannot find module '@ai-sdk/rsc'](/docs/troubleshooting/jest-cannot-find-module-ai-rsc) | Type: Conceptual | Summary: Troubleshooting AI SDK errors related to the Jest: cannot find module '@ai-sdk/rsc' error | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, jest-cannot-find-module-ai-rsc

    - [Missing Tool Results Error](/docs/troubleshooting/missing-tool-results-error) | Type: Conceptual | Summary: How to fix the "Tool results are missing for tool calls" error when using the AI SDK. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, missing-tool-results-error

    - [Model is not assignable to type "LanguageModelV1"](/docs/troubleshooting/model-is-not-assignable-to-type) | Type: Conceptual | Summary: Troubleshooting errors related to incompatible models. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, model-is-not-assignable-to-type

    - [Object generation failed with OpenAI](/docs/troubleshooting/no-object-generated-content-filter) | Type: Conceptual | Summary: Troubleshooting NoObjectGeneratedError with finish-reason content-filter caused by incompatible Zod schema types when using OpenAI structured outputs | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, no-object-generated-content-filter

    - [Type Error with onToolCall](/docs/troubleshooting/ontoolcall-type-narrowing) | Type: Conceptual | Summary: How to handle TypeScript type errors when using the onToolCall callback | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, ontoolcall-type-narrowing

    - [React error "Maximum update depth exceeded"](/docs/troubleshooting/react-maximum-update-depth-exceeded) | Type: Conceptual | Summary: Troubleshooting errors related to the "Maximum update depth exceeded" error. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, react-maximum-update-depth-exceeded

    - [Repeated assistant messages in useChat](/docs/troubleshooting/repeated-assistant-messages) | Type: Conceptual | Summary: Troubleshooting duplicate assistant messages when using useChat with streamText | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, repeated-assistant-messages

    - [Server Actions in Client Components](/docs/troubleshooting/server-actions-in-client-components) | Type: Conceptual | Summary: Troubleshooting errors related to server actions in client components. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, server-actions-in-client-components

    - [useChat/useCompletion stream output contains 0:... instead of text](/docs/troubleshooting/strange-stream-output) | Type: Conceptual | Summary: How to fix strange stream output in the UI | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, strange-stream-output

    - [onEnd not called when stream is aborted](/docs/troubleshooting/stream-abort-handling) | Type: Conceptual | Summary: Troubleshooting onEnd callback not executing when streams are aborted with toUIMessageStream | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, stream-abort-handling

    - [streamText fails silently](/docs/troubleshooting/stream-text-not-working) | Type: Conceptual | Summary: Troubleshooting errors related to the streamText function not working. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, stream-text-not-working

    - [Streamable UI Errors](/docs/troubleshooting/streamable-ui-errors) | Type: Conceptual | Summary: Troubleshooting errors related to streamable UI. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, streamable-ui-errors

    - [Streaming Not Working When Deployed](/docs/troubleshooting/streaming-not-working-when-deployed) | Type: Conceptual | Summary: Troubleshooting streaming issues in deployed apps. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, streaming-not-working-when-deployed

    - [Streaming Not Working When Proxied](/docs/troubleshooting/streaming-not-working-when-proxied) | Type: Conceptual | Summary: Troubleshooting streaming issues in proxied apps. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, streaming-not-working-when-proxied

    - [Streaming Status Shows But No Text Appears](/docs/troubleshooting/streaming-status-delay) | Type: Conceptual | Summary: Why useChat shows "streaming" status without any visible content | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, streaming-status-delay

    - [Getting Timeouts When Deploying on Vercel](/docs/troubleshooting/timeout-on-vercel) | Type: Conceptual | Summary: Learn how to fix timeouts and cut off responses when deploying to Vercel. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, timeout-on-vercel

    - [Tool calling with structured outputs](/docs/troubleshooting/tool-calling-with-structured-outputs) | Type: Conceptual | Summary: Troubleshooting tool calling when combined with structured output generation | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, tool-calling-with-structured-outputs

    - [Tool Invocation Missing Result Error](/docs/troubleshooting/tool-invocation-missing-result) | Type: Conceptual | Summary: How to fix the "ToolInvocation must have a result" error when using tools without execute functions | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, tool-invocation-missing-result

    - [TypeScript error "Cannot find namespace 'JSX'"](/docs/troubleshooting/typescript-cannot-find-namespace-jsx) | Type: Conceptual | Summary: Troubleshooting errors related to TypeScript and JSX. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, typescript-cannot-find-namespace-jsx

    - [TypeScript performance issues with Zod and AI SDK 5](/docs/troubleshooting/typescript-performance-zod) | Type: Conceptual | Summary: Troubleshooting TypeScript server crashes and slow performance when using Zod with AI SDK 5 | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, typescript-performance-zod

    - [Unclosed Streams](/docs/troubleshooting/unclosed-streams) | Type: Conceptual | Summary: Troubleshooting errors related to unclosed streams. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, unclosed-streams

    - [Unsupported model version error](/docs/troubleshooting/unsupported-model-version) | Type: Conceptual | Summary: Troubleshooting the AI_UnsupportedModelVersionError when migrating to AI SDK 5 | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, unsupported-model-version

    - [useChat "An error occurred"](/docs/troubleshooting/use-chat-an-error-occurred) | Type: Conceptual | Summary: Troubleshooting errors related to the "An error occurred" error in useChat. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, use-chat-an-error-occurred

    - [Custom headers, body, and credentials not working with useChat](/docs/troubleshooting/use-chat-custom-request-options) | Type: Conceptual | Summary: Troubleshooting errors related to custom request configuration in useChat hook | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, use-chat-custom-request-options

    - [useChat Failed to Parse Stream](/docs/troubleshooting/use-chat-failed-to-parse-stream) | Type: Conceptual | Summary: Troubleshooting errors related to the Use Chat Failed to Parse Stream error. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, use-chat-failed-to-parse-stream

    - [Stale body values with useChat](/docs/troubleshooting/use-chat-stale-body-data) | Type: Conceptual | Summary: Troubleshooting stale values when passing information via the body parameter of useChat | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, use-chat-stale-body-data

    - [useChat No Response](/docs/troubleshooting/use-chat-tools-no-response) | Type: Conceptual | Summary: Troubleshooting errors related to the Use Chat Failed to Parse Stream error. | Prerequisites: /docs/troubleshooting | Topics: troubleshooting, use-chat-tools-no-response

## Providers

- [Adapters](/providers/adapters) | Type: Conceptual | Summary: Learn how to use AI SDK Adapters. | Topics: providers, adapters

    - [LangChain](/providers/adapters/langchain) | Type: Conceptual | Summary: Learn how to use LangChain with the AI SDK. | Prerequisites: /providers/adapters | Topics: providers, adapters, langchain

    - [LlamaIndex](/providers/adapters/llamaindex) | Type: Conceptual | Summary: Learn how to use LlamaIndex with the AI SDK. | Prerequisites: /providers/adapters | Topics: providers, adapters, llamaindex

- [AI SDK Harnesses](/providers/ai-sdk-harnesses) | Type: Conceptual | Summary: Learn how to use AI SDK harness adapters. | Topics: providers, ai-sdk-harnesses

    - [Agent Client Protocol](/providers/ai-sdk-harnesses/acp) | Type: Conceptual | Summary: Learn how to use Agent Client Protocol implementations through the AI SDK harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, acp

    - [Claude Code](/providers/ai-sdk-harnesses/claude-code) | Type: Conceptual | Summary: Learn how to use the Claude Code harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, claude-code

    - [Cline](/providers/ai-sdk-harnesses/cline) | Type: Conceptual | Summary: Learn how to use the Cline harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, cline

    - [Codex](/providers/ai-sdk-harnesses/codex) | Type: Conceptual | Summary: Learn how to use the Codex harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, codex

    - [Cursor](/providers/ai-sdk-harnesses/cursor) | Type: Conceptual | Summary: Learn how to use the Cursor harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, cursor

    - [Deep Agents](/providers/ai-sdk-harnesses/deepagents) | Type: Conceptual | Summary: Learn how to use the Deep Agents harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, deepagents

    - [fx](/providers/ai-sdk-harnesses/fx) | Type: Conceptual | Summary: Learn how to use the fx harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, fx

    - [GitHub Copilot](/providers/ai-sdk-harnesses/github-copilot) | Type: Conceptual | Summary: Learn how to use the GitHub Copilot harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, github-copilot

    - [Grok Build](/providers/ai-sdk-harnesses/grok-build) | Type: Conceptual | Summary: Learn how to use the Grok Build harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, grok-build

    - [OpenCode](/providers/ai-sdk-harnesses/opencode) | Type: Conceptual | Summary: Learn how to use the OpenCode harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, opencode

    - [Pi](/providers/ai-sdk-harnesses/pi) | Type: Conceptual | Summary: Learn how to use the Pi harness adapter. | Prerequisites: /providers/ai-sdk-harnesses | Topics: providers, ai-sdk-harnesses, pi

- [AI SDK Providers](/providers/ai-sdk-providers) | Type: Conceptual | Summary: Learn how to use AI SDK providers. | Topics: providers, ai-sdk-providers

    - [AI Gateway](/providers/ai-sdk-providers/ai-gateway) | Type: Conceptual | Summary: Learn how to use the AI Gateway provider with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, ai-gateway

    - [Alibaba](/providers/ai-sdk-providers/alibaba) | Type: Conceptual | Summary: Learn how to use Alibaba Cloud Model Studio (Qwen) models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, alibaba

    - [Amazon Bedrock](/providers/ai-sdk-providers/amazon-bedrock) | Type: Conceptual | Summary: Learn how to use the Amazon Bedrock provider. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, amazon-bedrock

    - [Anthropic](/providers/ai-sdk-providers/anthropic) | Type: Conceptual | Summary: Learn how to use the Anthropic provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, anthropic

    - [Claude Platform on AWS](/providers/ai-sdk-providers/anthropic-aws) | Type: Conceptual | Summary: Learn how to use the Claude Platform on AWS provider. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, anthropic-aws

    - [AssemblyAI](/providers/ai-sdk-providers/assemblyai) | Type: Conceptual | Summary: Learn how to use the AssemblyAI provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, assemblyai

    - [Azure OpenAI](/providers/ai-sdk-providers/azure) | Type: Conceptual | Summary: Learn how to use the Azure OpenAI provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, azure

    - [Baseten](/providers/ai-sdk-providers/baseten) | Type: Conceptual | Summary: Learn how to use Baseten models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, baseten

    - [Black Forest Labs](/providers/ai-sdk-providers/black-forest-labs) | Type: Conceptual | Summary: Learn how to use Black Forest Labs models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, black-forest-labs

    - [ByteDance](/providers/ai-sdk-providers/bytedance) | Type: Conceptual | Summary: Learn how to use ByteDance Seedance video and Seedream image models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, bytedance

    - [Cartesia](/providers/ai-sdk-providers/cartesia) | Type: Conceptual | Summary: Learn how to use the Cartesia provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, cartesia

    - [Cerebras](/providers/ai-sdk-providers/cerebras) | Type: Conceptual | Summary: Learn how to use Cerebras's models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, cerebras

    - [Cohere](/providers/ai-sdk-providers/cohere) | Type: Conceptual | Summary: Learn how to use the Cohere provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, cohere

    - [Deepgram](/providers/ai-sdk-providers/deepgram) | Type: Conceptual | Summary: Learn how to use the Deepgram provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, deepgram

    - [DeepInfra](/providers/ai-sdk-providers/deepinfra) | Type: Conceptual | Summary: Learn how to use DeepInfra's models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, deepinfra

    - [DeepSeek](/providers/ai-sdk-providers/deepseek) | Type: Conceptual | Summary: Learn how to use DeepSeek's models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, deepseek

    - [ElevenLabs](/providers/ai-sdk-providers/elevenlabs) | Type: Conceptual | Summary: Learn how to use the ElevenLabs provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, elevenlabs

    - [Fal](/providers/ai-sdk-providers/fal) | Type: Conceptual | Summary: Learn how to use Fal AI models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, fal

    - [Fireworks](/providers/ai-sdk-providers/fireworks) | Type: Conceptual | Summary: Learn how to use Fireworks models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, fireworks

    - [Fish Audio](/providers/ai-sdk-providers/fish-audio) | Type: Conceptual | Summary: Learn how to use the Fish Audio provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, fish-audio

    - [Gladia](/providers/ai-sdk-providers/gladia) | Type: Conceptual | Summary: Learn how to use the Gladia provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, gladia

    - [GMI Cloud](/providers/ai-sdk-providers/gmicloud) | Type: Conceptual | Summary: Learn how to use GMI Cloud's models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, gmicloud

    - [Google](/providers/ai-sdk-providers/google) | Type: Conceptual | Summary: Learn how to use Google Provider. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, google

    - [Google Vertex AI](/providers/ai-sdk-providers/google-vertex) | Type: Conceptual | Summary: Learn how to use the Google Vertex AI provider. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, google-vertex

    - [Groq](/providers/ai-sdk-providers/groq) | Type: Conceptual | Summary: Learn how to use Groq. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, groq

    - [Hugging Face](/providers/ai-sdk-providers/huggingface) | Type: Conceptual | Summary: Learn how to use Hugging Face Provider. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, huggingface

    - [Hume](/providers/ai-sdk-providers/hume) | Type: Conceptual | Summary: Learn how to use the Hume provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, hume

    - [Kling AI](/providers/ai-sdk-providers/klingai) | Type: Conceptual | Summary: Learn how to use the Kling AI provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, klingai

    - [Luma](/providers/ai-sdk-providers/luma) | Type: Conceptual | Summary: Learn how to use Luma AI models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, luma

    - [MiniMax](/providers/ai-sdk-providers/minimax) | Type: Conceptual | Summary: Learn how to use MiniMax models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, minimax

    - [Mistral AI](/providers/ai-sdk-providers/mistral) | Type: Conceptual | Summary: Learn how to use Mistral. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, mistral

    - [Moonshot AI](/providers/ai-sdk-providers/moonshotai) | Type: Conceptual | Summary: Learn how to use Moonshot AI models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, moonshotai

    - [Open Responses](/providers/ai-sdk-providers/open-responses) | Type: Conceptual | Summary: Learn how to use the Open Responses provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, open-responses

    - [OpenAI](/providers/ai-sdk-providers/openai) | Type: Conceptual | Summary: Learn how to use the OpenAI provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, openai

    - [Perplexity](/providers/ai-sdk-providers/perplexity) | Type: Conceptual | Summary: Learn how to use Perplexity's Agent API with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, perplexity

    - [Prodia](/providers/ai-sdk-providers/prodia) | Type: Conceptual | Summary: Learn how to use Prodia models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, prodia

    - [QuiverAI](/providers/ai-sdk-providers/quiverai) | Type: Conceptual | Summary: Learn how to use QuiverAI models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, quiverai

    - [Replicate](/providers/ai-sdk-providers/replicate) | Type: Conceptual | Summary: Learn how to use Replicate models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, replicate

    - [Rev.ai](/providers/ai-sdk-providers/revai) | Type: Conceptual | Summary: Learn how to use the Rev.ai provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, revai

    - [Together.ai](/providers/ai-sdk-providers/togetherai) | Type: Conceptual | Summary: Learn how to use Together.ai's models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, togetherai

    - [Topaz Labs](/providers/ai-sdk-providers/topaz) | Type: Conceptual | Summary: Learn how to use the Topaz Labs provider for the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, topaz

    - [TypeSafe](/providers/ai-sdk-providers/typesafe-ai) | Type: Conceptual | Summary: Use TypeSafe System One models for typed decisions with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, typesafe-ai

    - [Voyage AI](/providers/ai-sdk-providers/voyage) | Type: Conceptual | Summary: Learn how to use the Voyage AI provider for embedding and reranking with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, voyage

    - [xAI Grok](/providers/ai-sdk-providers/xai) | Type: Conceptual | Summary: Learn how to use xAI Grok and Imagine. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, xai

    - [Z.AI](/providers/ai-sdk-providers/zai) | Type: Conceptual | Summary: Learn how to use Z.AI's GLM models with the AI SDK. | Prerequisites: /providers/ai-sdk-providers | Topics: providers, ai-sdk-providers, zai

- [Community Providers](/providers/community-providers) | Type: Conceptual | Summary: Learn how to use Language Model Specification. | Topics: providers, community-providers

    - [A2A](/providers/community-providers/a2a) | Type: Conceptual | Summary: A2A Protocol Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, a2a

    - [ACP (Agent Client Protocol)](/providers/community-providers/acp) | Type: Conceptual | Summary: ACP Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, acp

    - [Aihubmix](/providers/community-providers/aihubmix) | Type: Conceptual | Summary: Learn how to use Aihubmix with the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, aihubmix

    - [AI/ML API](/providers/community-providers/aimlapi) | Type: Conceptual | Summary: Learn how to use the AI/ML API provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, aimlapi

    - [Anthropic Vertex](/providers/community-providers/anthropic-vertex-ai) | Type: Conceptual | Summary: Learn how to use the Anthropic Vertex provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, anthropic-vertex-ai

    - [Apertis](/providers/community-providers/apertis) | Type: Conceptual | Summary: Apertis AI Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, apertis

    - [Automatic1111](/providers/community-providers/automatic1111) | Type: Conceptual | Summary: Automatic1111 Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, automatic1111

    - [Azure AI](/providers/community-providers/azure-ai) | Type: Conceptual | Summary: Learn how to use the @quail-ai/azure-ai-provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, azure-ai

    - [Browser AI](/providers/community-providers/browser-ai) | Type: Conceptual | Summary: Learn how to use browser AI model providers for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, browser-ai

    - [Cencori](/providers/community-providers/cencori) | Type: Conceptual | Summary: Cencori Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, cencori

    - [Claude Code](/providers/community-providers/claude-code) | Type: Conceptual | Summary: Learn how to use the Claude Code provider to access Claude models through the Claude Agent SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, claude-code

    - [Cloudflare AI Gateway](/providers/community-providers/cloudflare-ai-gateway) | Type: Conceptual | Summary: Learn how to use the Cloudflare AI Gateway provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, cloudflare-ai-gateway

    - [Cloudflare Workers AI](/providers/community-providers/cloudflare-workers-ai) | Type: Conceptual | Summary: Learn how to use the Cloudflare Workers AI provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, cloudflare-workers-ai

    - [Codex CLI (App Server)](/providers/community-providers/codex-app-server) | Type: Conceptual | Summary: Learn how to use the Codex CLI App Server provider for mid-execution message injection and persistent threads. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, codex-app-server

    - [Codex CLI](/providers/community-providers/codex-cli) | Type: Conceptual | Summary: Learn how to use the Codex CLI provider to access OpenAI GPT-5 models through the Codex CLI. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, codex-cli

    - [Crosshatch](/providers/community-providers/crosshatch) | Type: Conceptual | Summary: Learn how to use the Crosshatch provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, crosshatch

    - [Crusoe](/providers/community-providers/crusoe) | Type: Conceptual | Summary: Learn how to use the Crusoe provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, crusoe

    - [Writing a Custom Provider](/providers/community-providers/custom-providers) | Type: Conceptual | Summary: Learn how to write a custom provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, custom-providers

    - [Dify](/providers/community-providers/dify) | Type: Conceptual | Summary: Learn how to use the Dify provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, dify

    - [Firemoon](/providers/community-providers/firemoon) | Type: Conceptual | Summary: Firemoon provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, firemoon

    - [Flowise](/providers/community-providers/flowise) | Type: Conceptual | Summary: Learn how to use the Flowise provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, flowise

    - [FriendliAI](/providers/community-providers/friendliai) | Type: Conceptual | Summary: Learn how to use the FriendliAI Provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, friendliai

    - [Gemini CLI](/providers/community-providers/gemini-cli) | Type: Conceptual | Summary: Learn how to use the Gemini CLI provider to access Google's Gemini models. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, gemini-cli

    - [Helicone](/providers/community-providers/helicone) | Type: Conceptual | Summary: Helicone Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, helicone

    - [Hindsight](/providers/community-providers/hindsight) | Type: Conceptual | Summary: Learn how to use Hindsight persistent memory with the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, hindsight

    - [Inflection AI](/providers/community-providers/inflection-ai) | Type: Conceptual | Summary: Learn how to use the unofficial Inflection AI provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, inflection-ai

    - [Interfaze](/providers/community-providers/interfaze) | Type: Conceptual | Summary: Interfaze Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, interfaze

    - [Jina AI](/providers/community-providers/jina-ai) | Type: Conceptual | Summary: Learn how to use the Jina AI provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, jina-ai

    - [LangDB](/providers/community-providers/langdb) | Type: Conceptual | Summary: Learn how to use LangDB with the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, langdb

    - [Letta](/providers/community-providers/letta) | Type: Conceptual | Summary: Learn how to use the Letta provider with the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, letta

    - [llama.cpp](/providers/community-providers/llama-cpp) | Type: Conceptual | Summary: Learn how to use the llama.cpp provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, llama-cpp

    - [LlamaGate](/providers/community-providers/llamagate) | Type: Conceptual | Summary: LlamaGate Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, llamagate

    - [MCP Sampling AI Provider](/providers/community-providers/mcp-sampling) | Type: Conceptual | Summary: Learn how to use the MCP Sampling AI Provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, mcp-sampling

    - [Mem0](/providers/community-providers/mem0) | Type: Conceptual | Summary: Learn how to use the Mem0 AI SDK provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, mem0

    - [MiniMax](/providers/community-providers/minimax) | Type: Conceptual | Summary: Learn how to use MiniMax provider with the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, minimax

    - [Mixedbread](/providers/community-providers/mixedbread) | Type: Conceptual | Summary: Learn how to use the Mixedbread provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, mixedbread

    - [Neon AI Gateway](/providers/community-providers/neon-ai-gateway) | Type: Conceptual | Summary: Learn how to use the Neon AI Gateway provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, neon-ai-gateway

    - [Nia](/providers/community-providers/nia) | Type: Conceptual | Summary: Learn how to use Nia with the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, nia

    - [Ollama](/providers/community-providers/ollama) | Type: Conceptual | Summary: Learn how to use the Ollama provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, ollama

    - [OLLM](/providers/community-providers/ollm) | Type: Conceptual | Summary: OLLM Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, ollm

    - [OpenCode](/providers/community-providers/opencode-sdk) | Type: Conceptual | Summary: Learn how to use the OpenCode provider to access multiple AI models through a unified interface. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, opencode-sdk

    - [OpenRouter](/providers/community-providers/openrouter) | Type: Conceptual | Summary: OpenRouter Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, openrouter

    - [Portkey](/providers/community-providers/portkey) | Type: Conceptual | Summary: Learn how to use the Portkey provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, portkey

    - [QVAC](/providers/community-providers/qvac) | Type: Conceptual | Summary: Learn how to use the QVAC provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, qvac

    - [Qwen](/providers/community-providers/qwen) | Type: Conceptual | Summary: Learn how to use the Qwen provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, qwen

    - [React Native Apple](/providers/community-providers/react-native-apple) | Type: Conceptual | Summary: Learn how to use the Apple provider for on-device AI. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, react-native-apple

    - [Requesty](/providers/community-providers/requesty) | Type: Conceptual | Summary: Requesty Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, requesty

    - [Runpod](/providers/community-providers/runpod) | Type: Conceptual | Summary: Runpod Provider for the AI SDK | Prerequisites: /providers/community-providers | Topics: providers, community-providers, runpod

    - [SambaNova](/providers/community-providers/sambanova) | Type: Conceptual | Summary: Learn how to use the SambaNova provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, sambanova

    - [SAP AI Core](/providers/community-providers/sap-ai) | Type: Conceptual | Summary: Learn how to use the SAP AI Core provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, sap-ai

    - [Sarvam](/providers/community-providers/sarvam) | Type: Conceptual | Summary: Learn how to use the Sarvam AI provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, sarvam

    - [Soniox](/providers/community-providers/soniox) | Type: Conceptual | Summary: Learn how to use the Soniox provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, soniox

    - [Spark](/providers/community-providers/spark) | Type: Conceptual | Summary: Learn how to use the Spark provider for the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, spark

    - [Supermemory](/providers/community-providers/supermemory) | Type: Conceptual | Summary: Learn how to use the Supermemory AI SDK provider for the Vercel AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, supermemory

    - [Telnyx](/providers/community-providers/telnyx) | Type: Conceptual | Summary: Telnyx provider for AI SDK 7 | Prerequisites: /providers/community-providers | Topics: providers, community-providers, telnyx

    - [vectorstores](/providers/community-providers/vectorstores) | Type: Conceptual | Summary: Learn how to use vector databases with the AI SDK. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, vectorstores

    - [Voyage AI](/providers/community-providers/voyage-ai) | Type: Conceptual | Summary: Learn how to use the Voyage AI provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, voyage-ai

    - [ZeroEntropy](/providers/community-providers/zeroentropy) | Type: Conceptual | Summary: Learn how to use the ZeroEntropy community provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, zeroentropy

    - [Zhipu AI (Z.AI)](/providers/community-providers/zhipu) | Type: Conceptual | Summary: Learn how to use the Zhipu (Z.AI) provider. | Prerequisites: /providers/community-providers | Topics: providers, community-providers, zhipu

- [Observability Integrations](/providers/observability) | Type: Conceptual | Summary: AI SDK Integration for monitoring and tracing LLM applications | Topics: providers, observability

    - [Arize AX](/providers/observability/arize-ax) | Type: Conceptual | Summary: Trace, monitor, and evaluate LLM applications with Arize AX | Prerequisites: /providers/observability | Topics: providers, observability, arize-ax

    - [Axiom](/providers/observability/axiom) | Type: Conceptual | Summary: Measure, observe, and improve your AI SDK application with Axiom | Prerequisites: /providers/observability | Topics: providers, observability, axiom

    - [Braintrust](/providers/observability/braintrust) | Type: Conceptual | Summary: Monitoring and tracing LLM applications with Braintrust | Prerequisites: /providers/observability | Topics: providers, observability, braintrust

    - [Confident AI](/providers/observability/confident-ai) | Type: Conceptual | Summary: Trace and monitor your AI SDK applications with Confident AI | Prerequisites: /providers/observability | Topics: providers, observability, confident-ai

    - [Datadog Agent Observability](/providers/observability/datadog) | Type: Conceptual | Summary: Trace and monitor AI SDK applications with Datadog Agent Observability | Prerequisites: /providers/observability | Topics: providers, observability, datadog

    - [Helicone](/providers/observability/helicone) | Type: Conceptual | Summary: Monitor and optimize your AI SDK applications with minimal configuration using Helicone | Prerequisites: /providers/observability | Topics: providers, observability, helicone

    - [Laminar](/providers/observability/laminar) | Type: Conceptual | Summary: Monitor your AI SDK applications with Laminar | Prerequisites: /providers/observability | Topics: providers, observability, laminar

    - [Langfuse](/providers/observability/langfuse) | Type: Conceptual | Summary: Monitor, evaluate and debug your AI SDK application with Langfuse | Prerequisites: /providers/observability | Topics: providers, observability, langfuse

    - [LangSmith](/providers/observability/langsmith) | Type: Conceptual | Summary: Monitor and evaluate your AI SDK application with LangSmith | Prerequisites: /providers/observability | Topics: providers, observability, langsmith

    - [LangWatch](/providers/observability/langwatch) | Type: Conceptual | Summary: Track, monitor, guardrail and evaluate your AI SDK applications with LangWatch. | Prerequisites: /providers/observability | Topics: providers, observability, langwatch

    - [Latitude](/providers/observability/latitude) | Type: Conceptual | Summary: Monitor and debug your AI SDK application with Latitude | Prerequisites: /providers/observability | Topics: providers, observability, latitude

    - [Maxim](/providers/observability/maxim) | Type: Conceptual | Summary: Evaluate & Observe LLM applications with Maxim | Prerequisites: /providers/observability | Topics: providers, observability, maxim

    - [MLflow](/providers/observability/mlflow) | Type: Conceptual | Summary: Track, visualize, and debug Vercel AI SDK traces with MLflow Tracing | Prerequisites: /providers/observability | Topics: providers, observability, mlflow

    - [Patronus](/providers/observability/patronus) | Type: Conceptual | Summary: Monitor, evaluate and debug your AI SDK application with Patronus | Prerequisites: /providers/observability | Topics: providers, observability, patronus

    - [PostHog](/providers/observability/posthog) | Type: Conceptual | Summary: Monitor and analyze LLM usage with PostHog | Prerequisites: /providers/observability | Topics: providers, observability, posthog

    - [Raindrop](/providers/observability/raindrop) | Type: Conceptual | Summary: Monitor AI SDK calls and agent traces with Raindrop | Prerequisites: /providers/observability | Topics: providers, observability, raindrop

    - [Respan](/providers/observability/respan) | Type: Conceptual | Summary: Trace and monitor your AI SDK application with Respan | Prerequisites: /providers/observability | Topics: providers, observability, respan

    - [Scorecard](/providers/observability/scorecard) | Type: Conceptual | Summary: Monitoring and evaluating LLM applications with Scorecard | Prerequisites: /providers/observability | Topics: providers, observability, scorecard

    - [Sentry](/providers/observability/sentry) | Type: Conceptual | Summary: Monitor AI SDK calls and agent traces with Sentry | Prerequisites: /providers/observability | Topics: providers, observability, sentry

    - [SigNoz](/providers/observability/signoz) | Type: Conceptual | Summary: Monitor, observe and debug your AI SDK application with SigNoz | Prerequisites: /providers/observability | Topics: providers, observability, signoz

    - [Traceloop](/providers/observability/traceloop) | Type: Conceptual | Summary: Monitoring and evaluating LLM applications with Traceloop | Prerequisites: /providers/observability | Topics: providers, observability, traceloop

    - [Weave](/providers/observability/weave) | Type: Conceptual | Summary: Monitor and evaluate LLM applications with Weave. | Prerequisites: /providers/observability | Topics: providers, observability, weave

- [OpenAI Compatible Providers](/providers/openai-compatible-providers) | Type: Conceptual | Summary: Use OpenAI compatible providers with the AI SDK. | Topics: providers, openai-compatible-providers

    - [Cheaper Inference](/providers/openai-compatible-providers/cheaper-inference) | Type: Conceptual | Summary: Use the Cheaper Inference OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, cheaper-inference

    - [Clarifai](/providers/openai-compatible-providers/clarifai) | Type: Conceptual | Summary: Use Clarifai OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, clarifai

    - [Writing a Custom Provider](/providers/openai-compatible-providers/custom-providers) | Type: Conceptual | Summary: Create a custom provider package for an OpenAI-compatible provider leveraging the AI SDK OpenAI Compatible package. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, custom-providers

    - [Heroku](/providers/openai-compatible-providers/heroku) | Type: Conceptual | Summary: Use a Heroku OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, heroku

    - [LM Studio](/providers/openai-compatible-providers/lmstudio) | Type: Conceptual | Summary: Use the LM Studio OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, lmstudio

    - [ModelRush](/providers/openai-compatible-providers/modelrush) | Type: Conceptual | Summary: Use the ModelRush OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, modelrush

    - [NEAR AI Cloud](/providers/openai-compatible-providers/nearai) | Type: Conceptual | Summary: Use the NEAR AI Cloud OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, nearai

    - [NVIDIA NIM](/providers/openai-compatible-providers/nim) | Type: Conceptual | Summary: Use NVIDIA NIM OpenAI compatible API with the AI SDK. | Prerequisites: /providers/openai-compatible-providers | Topics: providers, openai-compatible-providers, nim

## Cookbook

- [Express](/cookbook/api-servers/express) | Type: Conceptual | Summary: Learn how to use the AI SDK in an Express server | Topics: cookbook, api-servers, express

- [Fastify](/cookbook/api-servers/fastify) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Fastify server | Topics: cookbook, api-servers, fastify

- [Hono](/cookbook/api-servers/hono) | Type: Conceptual | Summary: Example of using the AI SDK in a Hono server. | Topics: cookbook, api-servers, hono

- [Nest.js](/cookbook/api-servers/nest) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Nest.js server | Topics: cookbook, api-servers, nest

- [Node.js HTTP Server](/cookbook/api-servers/node-http-server) | Type: Conceptual | Summary: Learn how to use the AI SDK in a Node.js HTTP server | Topics: cookbook, api-servers, node-http-server

- [Guides](/cookbook/guides) | Type: Conceptual | Summary: Learn how to build AI applications with the AI SDK | Topics: cookbook, guides

    - [Compact Agent Context](/cookbook/guides/agent-context-compaction) | Type: Guide | Summary: Learn how to compact agent context by mutating message state between steps with prepareStep. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, agent-context-compaction

    - [Add Skills to Your Agent](/cookbook/guides/agent-skills) | Type: Guide | Summary: Learn how to extend your agent with specialized capabilities loaded at runtime with Agent Skills. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, agent-skills

    - [Get started with Claude 4](/cookbook/guides/claude-4) | Type: Guide | Summary: Get started with Claude 4 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, claude-4

    - [Get started with Computer Use](/cookbook/guides/computer-use) | Type: Guide | Summary: Get started with Claude's Computer Use capabilities with the AI SDK | Prerequisites: /cookbook/guides | Topics: cookbook, guides, computer-use

    - [Build a Custom Memory Tool](/cookbook/guides/custom-memory-tool) | Type: Guide | Summary: Build an agent that persists memories using a filesystem-backed memory tool. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, custom-memory-tool

    - [Get started with DeepSeek V3.2](/cookbook/guides/deepseek-v3-2) | Type: Guide | Summary: Get started with DeepSeek V3.2 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, deepseek-v3-2

    - [Get started with Gemini 3](/cookbook/guides/gemini) | Type: Guide | Summary: Get started with Gemini 3 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, gemini

    - [Google Gemini Image Generation](/cookbook/guides/google-gemini-image-generation) | Type: Guide | Summary: Generate and edit images with Google Gemini 3.1 Flash Image using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, google-gemini-image-generation

    - [Get started with GPT-5](/cookbook/guides/gpt-5) | Type: Guide | Summary: Get started with GPT-5 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, gpt-5

    - [Get started with Llama 3.1](/cookbook/guides/llama-3_1) | Type: Guide | Summary: Get started with Llama 3.1 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, llama-3_1

    - [Multi-Modal Agent](/cookbook/guides/multi-modal-chatbot) | Type: Guide | Summary: Learn how to build a multi-modal agent that can process images and PDFs with the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, multi-modal-chatbot

    - [Natural Language Postgres](/cookbook/guides/natural-language-postgres) | Type: Guide | Summary: Learn how to build a Next.js app that lets you talk to a PostgreSQL database in natural language. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, natural-language-postgres

    - [Get started with OpenAI o1](/cookbook/guides/o1) | Type: Guide | Summary: Get started with OpenAI o1 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, o1

    - [Get started with OpenAI o3-mini](/cookbook/guides/o3) | Type: Guide | Summary: Get started with OpenAI o3-mini using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, o3

    - [OpenAI Responses API](/cookbook/guides/openai-responses) | Type: Guide | Summary: Get started with the OpenAI Responses API using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, openai-responses

    - [Get started with DeepSeek R1](/cookbook/guides/r1) | Type: Guide | Summary: Get started with DeepSeek R1 using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, r1

    - [RAG Agent](/cookbook/guides/rag-chatbot) | Type: Guide | Summary: Learn how to build a RAG Agent with the AI SDK and Next.js | Prerequisites: /cookbook/guides | Topics: cookbook, guides, rag-chatbot

    - [Slackbot Agent Guide](/cookbook/guides/slackbot) | Type: Guide | Summary: Learn how to use the AI SDK to build an AI Agent in Slack. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, slackbot

    - [Get started with Claude 3.7 Sonnet](/cookbook/guides/sonnet-3-7) | Type: Guide | Summary: Get started with Claude 3.7 Sonnet using the AI SDK. | Prerequisites: /cookbook/guides | Topics: cookbook, guides, sonnet-3-7

- [Caching Middleware](/cookbook/next/caching-middleware) | Type: Conceptual | Summary: Learn how to create a caching middleware with Next.js and KV. | Topics: cookbook, next, caching-middleware

- [Call Tools](/cookbook/next/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and Next.js | Topics: cookbook, next, call-tools

- [Call Tools in Multiple Steps](/cookbook/next/call-tools-multiple-steps) | Type: Conceptual | Summary: Learn how to call tools in multiple steps using the AI SDK and Next.js | Topics: cookbook, next, call-tools-multiple-steps

- [Chat with PDFs](/cookbook/next/chat-with-pdf) | Type: Conceptual | Summary: Learn how to build a chatbot that can understand PDFs using the AI SDK and Next.js | Topics: cookbook, next, chat-with-pdf

- [Streaming with Custom Format](/cookbook/next/custom-stream-format) | Type: Conceptual | Summary: Build a custom format to stream LLM responses | Topics: cookbook, next, custom-stream-format

- [Generate Image with Chat Prompt](/cookbook/next/generate-image-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate an image with a chat prompt using the AI SDK and Next.js | Topics: cookbook, next, generate-image-with-chat-prompt

- [Generate Object](/cookbook/next/generate-object) | Type: Conceptual | Summary: Learn how to generate object using the AI SDK and Next.js | Topics: cookbook, next, generate-object

- [Generate Object with File Prompt through Form Submission](/cookbook/next/generate-object-with-file-prompt) | Type: Conceptual | Summary: Learn how to generate object with file prompt through form submission using the AI SDK and Next.js | Topics: cookbook, next, generate-object-with-file-prompt

- [Generate Text](/cookbook/next/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Next.js. | Topics: cookbook, next, generate-text

- [Generate Text with Chat Prompt](/cookbook/next/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and Next.js | Topics: cookbook, next, generate-text-with-chat-prompt

- [Human-in-the-Loop with Next.js](/cookbook/next/human-in-the-loop) | Type: Conceptual | Summary: Add a human approval step to your agentic system with Next.js and the AI SDK | Topics: cookbook, next, human-in-the-loop

- [Markdown Chatbot with Streamdown](/cookbook/next/markdown-chatbot-with-memoization) | Type: Conceptual | Summary: Render streaming Markdown responses with Streamdown, Next.js, and the AI SDK. | Topics: cookbook, next, markdown-chatbot-with-memoization

- [Model Context Protocol (MCP) Tools](/cookbook/next/mcp-tools) | Type: Conceptual | Summary: Learn how to use MCP tools with the AI SDK and Next.js | Topics: cookbook, next, mcp-tools

- [Render Visual Interface in Chat](/cookbook/next/render-visual-interface-in-chat) | Type: Conceptual | Summary: Learn how to render visual interfaces in chat using the AI SDK and Next.js | Topics: cookbook, next, render-visual-interface-in-chat

- [Send Custom Body from useChat](/cookbook/next/send-custom-body-from-use-chat) | Type: Conceptual | Summary: Learn how to send a custom body from the useChat hook using the AI SDK and Next.js | Topics: cookbook, next, send-custom-body-from-use-chat

- [Stream Object](/cookbook/next/stream-object) | Type: Conceptual | Summary: Learn how to stream object using the AI SDK and Next.js | Topics: cookbook, next, stream-object

- [Stream Text](/cookbook/next/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and Next.js | Topics: cookbook, next, stream-text

- [streamText Multi-Step Cookbook](/cookbook/next/stream-text-multistep) | Type: Conceptual | Summary: Learn how to create several streamText steps with different settings | Topics: cookbook, next, stream-text-multistep

- [Stream Text with Chat Prompt](/cookbook/next/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Next.js | Topics: cookbook, next, stream-text-with-chat-prompt

- [Stream Text with Image Prompt](/cookbook/next/stream-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream text with an image prompt using the AI SDK and Next.js | Topics: cookbook, next, stream-text-with-image-prompt

- [Track Agent Token Usage](/cookbook/next/track-agent-token-usage) | Type: Conceptual | Summary: Learn how to track the active context window with ToolLoopAgent. | Topics: cookbook, next, track-agent-token-usage

- [Share useChat State Across Components](/cookbook/next/use-shared-chat-context) | Type: Conceptual | Summary: Learn how to share a chat instance across multiple components with useChat and easily reset the chat. | Topics: cookbook, next, use-shared-chat-context

- [Call Tools](/cookbook/node/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and Node | Topics: cookbook, node, call-tools

- [Call Tools in Parallel](/cookbook/node/call-tools-in-parallel) | Type: Conceptual | Summary: Learn how to call tools in parallel using the AI SDK in Node.js | Topics: cookbook, node, call-tools-in-parallel

- [Call Tools in Multiple Steps](/cookbook/node/call-tools-multiple-steps) | Type: Conceptual | Summary: Learn how to call tools with multiple steps using the AI SDK and Node | Topics: cookbook, node, call-tools-multiple-steps

- [Call Tools with Image Prompt](/cookbook/node/call-tools-with-image-prompt) | Type: Conceptual | Summary: Learn how to call tools with image prompt using the AI SDK and Node | Topics: cookbook, node, call-tools-with-image-prompt

- [Dynamic Prompt Caching](/cookbook/node/dynamic-prompt-caching) | Type: Conceptual | Summary: Learn how to reduce API costs by implementing dynamic prompt caching for Anthropic models using cache control directives. | Topics: cookbook, node, dynamic-prompt-caching

- [Embed Text](/cookbook/node/embed-text) | Type: Conceptual | Summary: Learn how to embed text using the AI SDK and Node | Topics: cookbook, node, embed-text

- [Embed Text in Batch](/cookbook/node/embed-text-batch) | Type: Conceptual | Summary: Learn how to embed multiple text using the AI SDK and Node | Topics: cookbook, node, embed-text-batch

- [Generate Object](/cookbook/node/generate-object) | Type: Conceptual | Summary: Learn how to generate structured data using the AI SDK and Node | Topics: cookbook, node, generate-object

- [Generate Object with a Reasoning Model](/cookbook/node/generate-object-reasoning) | Type: Conceptual | Summary: Learn how to generate structured data with a reasoning model using the AI SDK and Node | Topics: cookbook, node, generate-object-reasoning

- [Generate Text](/cookbook/node/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and Node | Topics: cookbook, node, generate-text

- [Generate Text with Chat Prompt](/cookbook/node/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and Node | Topics: cookbook, node, generate-text-with-chat-prompt

- [Generate Text with Image Prompt](/cookbook/node/generate-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to generate text with image prompt using the AI SDK and Node | Topics: cookbook, node, generate-text-with-image-prompt

- [Intercepting Fetch Requests](/cookbook/node/intercept-fetch-requests) | Type: Conceptual | Summary: Learn how to intercept fetch requests using the AI SDK and Node | Topics: cookbook, node, intercept-fetch-requests

- [Knowledge Base Agent](/cookbook/node/knowledge-base-agent) | Type: Conceptual | Summary: Build an AI agent that can read from and write to a knowledge base using Upstash Search and the AI SDK | Topics: cookbook, node, knowledge-base-agent

- [Local Caching Middleware](/cookbook/node/local-caching-middleware) | Type: Conceptual | Summary: Learn how to create a caching middleware for local development. | Topics: cookbook, node, local-caching-middleware

- [Manual Agent Loop](/cookbook/node/manual-agent-loop) | Type: Conceptual | Summary: Learn how to create your own agentic loop with full control over tool execution | Topics: cookbook, node, manual-agent-loop

- [Model Context Protocol (MCP) Elicitation](/cookbook/node/mcp-elicitation) | Type: Conceptual | Summary: Learn how to handle elicitation requests from MCP servers with the AI SDK | Topics: cookbook, node, mcp-elicitation

- [Model Context Protocol (MCP) Tools](/cookbook/node/mcp-tools) | Type: Conceptual | Summary: Learn how to use MCP tools with the AI SDK and Node | Topics: cookbook, node, mcp-tools

- [Repair Malformed JSON with jsonrepair](/cookbook/node/repair-json-with-jsonrepair) | Type: Conceptual | Summary: Learn how to use the jsonrepair library to automatically fix truncated or malformed JSON output from language models. | Topics: cookbook, node, repair-json-with-jsonrepair

- [Retrieval Augmented Generation](/cookbook/node/retrieval-augmented-generation) | Type: Conceptual | Summary: Learn how to use retrieval augmented generation using the AI SDK and Node | Topics: cookbook, node, retrieval-augmented-generation

- [Stream Object](/cookbook/node/stream-object) | Type: Conceptual | Summary: Learn how to stream structured data using the AI SDK and Node | Topics: cookbook, node, stream-object

- [Record Final Object after Streaming Object](/cookbook/node/stream-object-record-final-object) | Type: Conceptual | Summary: Learn how to record the final object after streaming an object using the AI SDK and Node | Topics: cookbook, node, stream-object-record-final-object

- [Record Token Usage After Streaming Object](/cookbook/node/stream-object-record-token-usage) | Type: Conceptual | Summary: Learn how to record token usage when streaming structured data using the AI SDK and Node | Topics: cookbook, node, stream-object-record-token-usage

- [Stream Object with Image Prompt](/cookbook/node/stream-object-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream structured data with an image prompt using the AI SDK and Node | Topics: cookbook, node, stream-object-with-image-prompt

- [Stream Text](/cookbook/node/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and Node | Topics: cookbook, node, stream-text

- [Stream Text with Chat Prompt](/cookbook/node/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to stream text with chat prompt using the AI SDK and Node | Topics: cookbook, node, stream-text-with-chat-prompt

- [Stream Text with File Prompt](/cookbook/node/stream-text-with-file-prompt) | Type: Conceptual | Summary: Learn how to stream text with file prompt using the AI SDK and Node | Topics: cookbook, node, stream-text-with-file-prompt

- [Stream Text with Image Prompt](/cookbook/node/stream-text-with-image-prompt) | Type: Conceptual | Summary: Learn how to stream text with image prompt using the AI SDK and Node | Topics: cookbook, node, stream-text-with-image-prompt

- [Web Search Agent](/cookbook/node/web-search-agent) | Type: Conceptual | Summary: Learn how to build an agent that has access to web with the AI SDK and Node | Topics: cookbook, node, web-search-agent

- [Call Tools](/cookbook/rsc/call-tools) | Type: Conceptual | Summary: Learn how to call tools using the AI SDK and React Server Components. | Topics: cookbook, rsc, call-tools

- [Call Tools in Parallel](/cookbook/rsc/call-tools-in-parallel) | Type: Conceptual | Summary: Learn how to tools in parallel text using the AI SDK and React Server Components. | Topics: cookbook, rsc, call-tools-in-parallel

- [Generate Object](/cookbook/rsc/generate-object) | Type: Conceptual | Summary: Learn how to generate object using the AI SDK and React Server Components. | Topics: cookbook, rsc, generate-object

- [Generate Text](/cookbook/rsc/generate-text) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: cookbook, rsc, generate-text

- [Generate Text with Chat Prompt](/cookbook/rsc/generate-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to generate text with chat prompt using the AI SDK and React Server Components. | Topics: cookbook, rsc, generate-text-with-chat-prompt

- [Render Visual Interface in Chat](/cookbook/rsc/render-visual-interface-in-chat) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: cookbook, rsc, render-visual-interface-in-chat

- [Restore Messages From Database](/cookbook/rsc/restore-messages-from-database) | Type: Conceptual | Summary: Learn how to restore messages from an external database using the AI SDK and React Server Components | Topics: cookbook, rsc, restore-messages-from-database

- [Save Messages To Database](/cookbook/rsc/save-messages-to-database) | Type: Conceptual | Summary: Learn how to save messages to an external database using the AI SDK and React Server Components | Topics: cookbook, rsc, save-messages-to-database

- [Stream Object](/cookbook/rsc/stream-object) | Type: Conceptual | Summary: Learn how to stream object using the AI SDK and React Server Components. | Topics: cookbook, rsc, stream-object

- [Stream Text](/cookbook/rsc/stream-text) | Type: Conceptual | Summary: Learn how to stream text using the AI SDK and React Server Components. | Topics: cookbook, rsc, stream-text

- [Stream Text with Chat Prompt](/cookbook/rsc/stream-text-with-chat-prompt) | Type: Conceptual | Summary: Learn how to stream text with chat prompt using the AI SDK and React Server Components. | Topics: cookbook, rsc, stream-text-with-chat-prompt

- [Record Token Usage after Streaming User Interfaces](/cookbook/rsc/stream-ui-record-token-usage) | Type: Conceptual | Summary: Learn how to record token usage after streaming user interfaces using the AI SDK and React Server Components | Topics: cookbook, rsc, stream-ui-record-token-usage

- [Stream Updates to Visual Interfaces](/cookbook/rsc/stream-updates-to-visual-interfaces) | Type: Conceptual | Summary: Learn how to generate text using the AI SDK and React Server Components. | Topics: cookbook, rsc, stream-updates-to-visual-interfaces