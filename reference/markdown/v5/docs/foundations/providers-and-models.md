---
title: Providers and Models
description: Learn about the providers and models available in the AI SDK.
url: "https://ai-sdk.dev/v5/docs/foundations/providers-and-models"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Companies such as OpenAI and Anthropic (providers) offer access to a range of large language models (LLMs) with differing strengths and capabilities through their own APIs.

Each provider typically has its own unique method for interfacing with their models, complicating the process of switching providers and increasing the risk of vendor lock-in.

To solve these challenges, AI SDK Core offers a standardized approach to interacting with LLMs through a [language model specification](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v2) that abstracts differences between providers. This unified interface allows you to switch between providers with ease while using the same API for all providers.

Here is an overview of the AI SDK Provider Architecture:

![](/images/ai-sdk-diagram.png)

## AI SDK Providers

The AI SDK comes with a wide range of providers that you can use to interact with different language models:

- [xAI Grok Provider](/v5/providers/ai-sdk-providers/xai) (`@ai-sdk/xai`)
- [OpenAI Provider](/v5/providers/ai-sdk-providers/openai) (`@ai-sdk/openai`)
- [Azure OpenAI Provider](/v5/providers/ai-sdk-providers/azure) (`@ai-sdk/azure`)
- [Anthropic Provider](/v5/providers/ai-sdk-providers/anthropic) (`@ai-sdk/anthropic`)
- [Amazon Bedrock Provider](/v5/providers/ai-sdk-providers/amazon-bedrock) (`@ai-sdk/amazon-bedrock`)
- [Google Generative AI Provider](/v5/providers/ai-sdk-providers/google-generative-ai) (`@ai-sdk/google`)
- [Google Vertex Provider](/v5/providers/ai-sdk-providers/google-vertex) (`@ai-sdk/google-vertex`)
- [Mistral Provider](/v5/providers/ai-sdk-providers/mistral) (`@ai-sdk/mistral`)
- [Together.ai Provider](/v5/providers/ai-sdk-providers/togetherai) (`@ai-sdk/togetherai`)
- [Cohere Provider](/v5/providers/ai-sdk-providers/cohere) (`@ai-sdk/cohere`)
- [Fireworks Provider](/v5/providers/ai-sdk-providers/fireworks) (`@ai-sdk/fireworks`)
- [DeepInfra Provider](/v5/providers/ai-sdk-providers/deepinfra) (`@ai-sdk/deepinfra`)
- [DeepSeek Provider](/v5/providers/ai-sdk-providers/deepseek) (`@ai-sdk/deepseek`)
- [Cerebras Provider](/v5/providers/ai-sdk-providers/cerebras) (`@ai-sdk/cerebras`)
- [Groq Provider](/v5/providers/ai-sdk-providers/groq) (`@ai-sdk/groq`)
- [Perplexity Provider](/v5/providers/ai-sdk-providers/perplexity) (`@ai-sdk/perplexity`)
- [ElevenLabs Provider](/v5/providers/ai-sdk-providers/elevenlabs) (`@ai-sdk/elevenlabs`)
- [Hume Provider](/v5/providers/ai-sdk-providers/hume) (`@ai-sdk/hume`)
- [Rev.ai Provider](/v5/providers/ai-sdk-providers/revai) (`@ai-sdk/revai`)
- [Deepgram Provider](/v5/providers/ai-sdk-providers/deepgram) (`@ai-sdk/deepgram`)
- [Gladia Provider](/v5/providers/ai-sdk-providers/gladia) (`@ai-sdk/gladia`)
- [AssemblyAI Provider](/v5/providers/ai-sdk-providers/assemblyai) (`@ai-sdk/assemblyai`)
- [Baseten](/v5/providers/ai-sdk-providers/baseten)

You can also use the [OpenAI Compatible provider](/v5/providers/openai-compatible-providers) with OpenAI-compatible APIs:

- [LM Studio](/v5/providers/openai-compatible-providers/lmstudio)
- [Heroku](/v5/providers/openai-compatible-providers/heroku)

Our [language model specification](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v2) is published as an open-source package, which you can use to create [custom providers](/v5/providers/community-providers/custom-providers).

The open-source community has created the following providers:

- [Ollama Provider](/v5/providers/community-providers/ollama) (`ollama-ai-provider`)
- [FriendliAI Provider](/v5/providers/community-providers/friendliai) (`@friendliai/ai-provider`)
- [Portkey Provider](/v5/providers/community-providers/portkey) (`@portkey-ai/vercel-provider`)
- [Cloudflare Workers AI Provider](/v5/providers/community-providers/cloudflare-workers-ai) (`workers-ai-provider`)
- [OpenRouter Provider](/v5/providers/community-providers/openrouter) (`@openrouter/ai-sdk-provider`)
- [Aihubmix Provider](/v5/providers/community-providers/aihubmix) (`@aihubmix/ai-sdk-provider`)
- [Requesty Provider](/v5/providers/community-providers/requesty) (`@requesty/ai-sdk`)
- [Crosshatch Provider](/v5/providers/community-providers/crosshatch) (`@crosshatch/ai-provider`)
- [Mixedbread Provider](/v5/providers/community-providers/mixedbread) (`mixedbread-ai-provider`)
- [Voyage AI Provider](/v5/providers/community-providers/voyage-ai) (`voyage-ai-provider`)
- [Mem0 Provider](/v5/providers/community-providers/mem0)(`@mem0/vercel-ai-provider`)
- [Letta Provider](/v5/providers/community-providers/letta)(`@letta-ai/vercel-ai-sdk-provider`)
- [Supermemory Provider](/v5/providers/community-providers/supermemory)(`@supermemory/tools`)
- [Spark Provider](/v5/providers/community-providers/spark) (`spark-ai-provider`)
- [AnthropicVertex Provider](/v5/providers/community-providers/anthropic-vertex-ai) (`anthropic-vertex-ai`)
- [LangDB Provider](/v5/providers/community-providers/langdb) (`@langdb/vercel-provider`)
- [Dify Provider](/v5/providers/community-providers/dify) (`dify-ai-provider`)
- [Sarvam Provider](/v5/providers/community-providers/sarvam) (`sarvam-ai-provider`)
- [Claude Code Provider](/v5/providers/community-providers/claude-code) (`ai-sdk-provider-claude-code`)
- [Built-in AI Provider](/v5/providers/community-providers/built-in-ai) (`built-in-ai`)
- [Gemini CLI Provider](/v5/providers/community-providers/gemini-cli) (`ai-sdk-provider-gemini-cli`)
- [A2A Provider](/v5/providers/community-providers/a2a) (`a2a-ai-provider`)
- [SAP-AI Provider](/v5/providers/community-providers/sap-ai) (`@mymediset/sap-ai-provider`)
- [AI/ML API Provider](/v5/providers/community-providers/aimlapi) (`@ai-ml.api/aimlapi-vercel-ai`)
- [MCP Sampling Provider](/v5/providers/community-providers/mcp-sampling) (`@mcpc-tech/mcp-sampling-ai-provider`)
- [ACP Provider](/v5/providers/community-providers/acp) (`@mcpc-tech/acp-ai-provider`)

## Self-Hosted Models

You can access self-hosted models with the following providers:

- [Ollama Provider](/v5/providers/community-providers/ollama)
- [LM Studio](/v5/providers/openai-compatible-providers/lmstudio)
- [Baseten](/v5/providers/ai-sdk-providers/baseten)
- [Built-in AI](/v5/providers/community-providers/built-in-ai)

Additionally, any self-hosted provider that supports the OpenAI specification can be used with the [OpenAI Compatible Provider](/v5/providers/openai-compatible-providers).

## Model Capabilities

The AI providers support different language models with various capabilities.
Here are the capabilities of popular models:

| Provider                                                                 | Model                                       | Image Input | Object Generation | Tool Usage | Tool Streaming |
| ------------------------------------------------------------------------ | ------------------------------------------- | ----------- | ----------------- | ---------- | -------------- |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-4.6`                                  | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-4.5`                                  | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-4`                                    | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3`                                    | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3-fast`                               | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3-mini`                               | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3-mini-fast`                          | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-2-1212`                               | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-2-vision-1212`                        | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-beta`                                 | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-vision-beta`                          | ✓           | ✗                 | ✗          | ✗              |
| [Vercel](/v5/providers/ai-sdk-providers/vercel)                             | `v0-1.0-md`                                 | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-6-astra`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6-luna`                              | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6-sol`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6-terra`                             | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.4-pro`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.4`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.3-chat-latest`                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.2-pro`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.2-chat-latest`                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.2`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5`                                     | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-mini`                                | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-nano`                                | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1-chat-latest`                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1-codex-mini`                        | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1-codex`                             | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-codex`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-chat-latest`                         | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-fable-5-1`                          | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-5-5`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-5`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-fable-5`                            | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-8`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-7`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-6`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-4-6`                         | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-5`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-1`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-0`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-4-0`                         | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-3-7-sonnet-latest`                  | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-3-5-haiku-latest`                   | ✓           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `pixtral-large-latest`                      | ✓           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-large-latest`                      | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-medium-latest`                     | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-medium-2505`                       | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-small-latest`                      | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `pixtral-12b-2409`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-3.8-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-3.1-pro-preview`                    | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-3-pro-preview`                      | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.5-pro`                            | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.5-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.0-flash-exp`                      | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-1.5-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-1.5-pro`                            | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-3.8-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-3.1-pro-preview`                    | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-3-pro-preview`                      | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-2.5-pro`                            | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-2.5-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-2.0-flash-exp`                      | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-1.5-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-1.5-pro`                            | ✓           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v5/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-flash`                         | ✗           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v5/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-pro`                           | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v5/providers/ai-sdk-providers/cerebras)                         | `llama3.1-8b`                               | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v5/providers/ai-sdk-providers/cerebras)                         | `llama3.1-70b`                              | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v5/providers/ai-sdk-providers/cerebras)                         | `llama3.3-70b`                              | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `meta-llama/llama-4-scout-17b-16e-instruct` | ✓           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `llama-3.3-70b-versatile`                   | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `llama-3.1-8b-instant`                      | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `mixtral-8x7b-32768`                        | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `gemma2-9b-it`                              | ✗           | ✓                 | ✓          | ✓              |

This table is not exhaustive. Additional models can be found in the provider
documentation pages and on the provider websites.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)