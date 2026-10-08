---
title: Providers and Models
description: Learn about the providers and models available in the AI SDK.
url: "https://ai-sdk.dev/v6/docs/foundations/providers-and-models"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Companies such as OpenAI and Anthropic (providers) offer access to a range of large language models (LLMs) with differing strengths and capabilities through their own APIs.

Each provider typically has its own unique method for interfacing with their models, complicating the process of switching providers and increasing the risk of vendor lock-in.

To solve these challenges, AI SDK Core offers a standardized approach to interacting with LLMs through a [language model specification](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v3) that abstracts differences between providers. This unified interface allows you to switch between providers with ease while using the same API for all providers.

Here is an overview of the AI SDK Provider Architecture:

![](/images/ai-sdk-diagram.png)

## AI SDK Providers

The AI SDK comes with a wide range of providers that you can use to interact with different language models:

- [xAI Grok Provider](/v6/providers/ai-sdk-providers/xai) (`@ai-sdk/xai`)
- [OpenAI Provider](/v6/providers/ai-sdk-providers/openai) (`@ai-sdk/openai`)
- [Azure OpenAI Provider](/v6/providers/ai-sdk-providers/azure) (`@ai-sdk/azure`)
- [Anthropic Provider](/v6/providers/ai-sdk-providers/anthropic) (`@ai-sdk/anthropic`)
- [Amazon Bedrock Provider](/v6/providers/ai-sdk-providers/amazon-bedrock) (`@ai-sdk/amazon-bedrock`)
- [Google Generative AI Provider](/v6/providers/ai-sdk-providers/google-generative-ai) (`@ai-sdk/google`)
- [Google Vertex Provider](/v6/providers/ai-sdk-providers/google-vertex) (`@ai-sdk/google-vertex`)
- [Mistral Provider](/v6/providers/ai-sdk-providers/mistral) (`@ai-sdk/mistral`)
- [Together.ai Provider](/v6/providers/ai-sdk-providers/togetherai) (`@ai-sdk/togetherai`)
- [Cohere Provider](/v6/providers/ai-sdk-providers/cohere) (`@ai-sdk/cohere`)
- [Fireworks Provider](/v6/providers/ai-sdk-providers/fireworks) (`@ai-sdk/fireworks`)
- [DeepInfra Provider](/v6/providers/ai-sdk-providers/deepinfra) (`@ai-sdk/deepinfra`)
- [DeepSeek Provider](/v6/providers/ai-sdk-providers/deepseek) (`@ai-sdk/deepseek`)
- [Cerebras Provider](/v6/providers/ai-sdk-providers/cerebras) (`@ai-sdk/cerebras`)
- [Groq Provider](/v6/providers/ai-sdk-providers/groq) (`@ai-sdk/groq`)
- [Perplexity Provider](/v6/providers/ai-sdk-providers/perplexity) (`@ai-sdk/perplexity`)
- [ElevenLabs Provider](/v6/providers/ai-sdk-providers/elevenlabs) (`@ai-sdk/elevenlabs`)
- [Hume Provider](/v6/providers/ai-sdk-providers/hume) (`@ai-sdk/hume`)
- [Rev.ai Provider](/v6/providers/ai-sdk-providers/revai) (`@ai-sdk/revai`)
- [Deepgram Provider](/v6/providers/ai-sdk-providers/deepgram) (`@ai-sdk/deepgram`)
- [Gladia Provider](/v6/providers/ai-sdk-providers/gladia) (`@ai-sdk/gladia`)
- [AssemblyAI Provider](/v6/providers/ai-sdk-providers/assemblyai) (`@ai-sdk/assemblyai`)
- [Baseten Provider](/v6/providers/ai-sdk-providers/baseten) (`@ai-sdk/baseten`)

You can also use the [OpenAI Compatible provider](/v6/providers/openai-compatible-providers) with OpenAI-compatible APIs:

- [LM Studio](/v6/providers/openai-compatible-providers/lmstudio)
- [Heroku](/v6/providers/openai-compatible-providers/heroku)

Our [language model specification](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v3) is published as an open-source package, which you can use to create [custom providers](/v6/providers/community-providers/custom-providers).

The open-source community has created the following providers:

- [Ollama Provider](/v6/providers/community-providers/ollama) (`ollama-ai-provider`)
- [FriendliAI Provider](/v6/providers/community-providers/friendliai) (`@friendliai/ai-provider`)
- [Portkey Provider](/v6/providers/community-providers/portkey) (`@portkey-ai/vercel-provider`)
- [Cloudflare Workers AI Provider](/v6/providers/community-providers/cloudflare-workers-ai) (`workers-ai-provider`)
- [OpenRouter Provider](/v6/providers/community-providers/openrouter) (`@openrouter/ai-sdk-provider`)
- [Apertis Provider](/v6/providers/community-providers/apertis) (`@apertis/ai-sdk-provider`)
- [Aihubmix Provider](/v6/providers/community-providers/aihubmix) (`@aihubmix/ai-sdk-provider`)
- [Requesty Provider](/v6/providers/community-providers/requesty) (`@requesty/ai-sdk`)
- [Crosshatch Provider](/v6/providers/community-providers/crosshatch) (`@crosshatch/ai-provider`)
- [Mixedbread Provider](/v6/providers/community-providers/mixedbread) (`mixedbread-ai-provider`)
- [Voyage AI Provider](/v6/providers/community-providers/voyage-ai) (`voyage-ai-provider`)
- [Mem0 Provider](/v6/providers/community-providers/mem0) (`@mem0/vercel-ai-provider`)
- [Letta Provider](/v6/providers/community-providers/letta) (`@letta-ai/vercel-ai-sdk-provider`)
- [Hindsight Provider](/v6/providers/community-providers/hindsight) (`@vectorize-io/hindsight-ai-sdk`)
- [Supermemory Provider](/v6/providers/community-providers/supermemory) (`@supermemory/tools`)
- [Spark Provider](/v6/providers/community-providers/spark) (`spark-ai-provider`)
- [AnthropicVertex Provider](/v6/providers/community-providers/anthropic-vertex-ai) (`anthropic-vertex-ai`)
- [LangDB Provider](/v6/providers/community-providers/langdb) (`@langdb/vercel-provider`)
- [Dify Provider](/v6/providers/community-providers/dify) (`dify-ai-provider`)
- [Sarvam Provider](/v6/providers/community-providers/sarvam) (`sarvam-ai-provider`)
- [Claude Code Provider](/v6/providers/community-providers/claude-code) (`ai-sdk-provider-claude-code`)
- [Browser AI Provider](/v6/providers/community-providers/browser-ai) (`browser-ai`)
- [Gemini CLI Provider](/v6/providers/community-providers/gemini-cli) (`ai-sdk-provider-gemini-cli`)
- [A2A Provider](/v6/providers/community-providers/a2a) (`a2a-ai-provider`)
- [SAP AI Core Provider](/v6/providers/community-providers/sap-ai) (`@jerome-benoit/sap-ai-provider`)
- [AI/ML API Provider](/v6/providers/community-providers/aimlapi) (`@ai-ml.api/aimlapi-vercel-ai`)
- [MCP Sampling Provider](/v6/providers/community-providers/mcp-sampling) (`@mcpc-tech/mcp-sampling-ai-provider`)
- [ACP Provider](/v6/providers/community-providers/acp) (`@mcpc-tech/acp-ai-provider`)
- [OpenCode Provider](/v6/providers/community-providers/opencode-sdk) (`ai-sdk-provider-opencode-sdk`)
- [Codex CLI Provider](/v6/providers/community-providers/codex-cli) (`ai-sdk-provider-codex-cli`)
- [Soniox Provider](/v6/providers/community-providers/soniox) (`@soniox/vercel-ai-sdk-provider`)
- [Zhipu (Z.AI) Provider](/v6/providers/community-providers/zhipu) (`zhipu-ai-provider`)
- [OLLM Provider](/v6/providers/community-providers/ollm) (`@ofoundation/ollm`)
- [ZeroEntropy Provider](/v6/providers/community-providers/zeroentropy) (`zeroentropy-ai-provider`)
- [Neon AI Gateway Provider](/v6/providers/community-providers/neon-ai-gateway) (`@neon/ai-sdk-provider`)

## Self-Hosted Models

You can access self-hosted models with the following providers:

- [Ollama Provider](/v6/providers/community-providers/ollama)
- [LM Studio](/v6/providers/openai-compatible-providers/lmstudio)
- [Baseten](/v6/providers/ai-sdk-providers/baseten)
- [Browser AI](/v6/providers/community-providers/browser-ai)

Additionally, any self-hosted provider that supports the OpenAI specification can be used with the [OpenAI Compatible Provider](/v6/providers/openai-compatible-providers).

## Model Capabilities

The AI providers support different language models with various capabilities.
Here are the capabilities of popular models:

| Provider                                                                 | Model                                       | Image Input | Object Generation | Tool Usage | Tool Streaming |
| ------------------------------------------------------------------------ | ------------------------------------------- | ----------- | ----------------- | ---------- | -------------- |
| [xAI Grok](/v6/providers/ai-sdk-providers/xai)                              | `grok-4.6`                                  | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v6/providers/ai-sdk-providers/xai)                              | `grok-4.5`                                  | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v6/providers/ai-sdk-providers/xai)                              | `grok-4`                                    | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v6/providers/ai-sdk-providers/xai)                              | `grok-3`                                    | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v6/providers/ai-sdk-providers/xai)                              | `grok-3-mini`                               | ✗           | ✓                 | ✓          | ✓              |
| [Vercel](/v6/providers/ai-sdk-providers/vercel)                             | `v0-1.0-md`                                 | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-6-astra`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.6`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.6-luna`                              | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.6-sol`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.6-terra`                             | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.5`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.4-pro`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.4`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.4-mini`                              | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.4-nano`                              | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.3-chat-latest`                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.2-pro`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.2-chat-latest`                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.2`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5`                                     | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5-mini`                                | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5-nano`                                | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.1-chat-latest`                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.1-codex-mini`                        | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.1-codex`                             | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5.1`                                   | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5-codex`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v6/providers/ai-sdk-providers/openai)                             | `gpt-5-chat-latest`                         | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-fable-5-1`                          | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-5-5`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-5`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-fable-5`                            | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-8`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-7`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-6`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-4-6`                         | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-5`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-1`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-0`                           | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v6/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-4-0`                         | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v6/providers/ai-sdk-providers/google-generative-ai) | `gemini-3.8-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v6/providers/ai-sdk-providers/google-generative-ai) | `gemini-3.1-pro-preview`                    | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v6/providers/ai-sdk-providers/google-generative-ai) | `gemini-3-pro-preview`                      | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v6/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.5-pro`                            | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v6/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.5-flash`                          | ✓           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `pixtral-large-latest`                      | ✓           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `mistral-large-latest`                      | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `mistral-medium-latest`                     | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `mistral-medium-3`                          | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `mistral-medium-2505`                       | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `mistral-medium-3.5`                        | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `mistral-small-latest`                      | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v6/providers/ai-sdk-providers/mistral)                           | `pixtral-12b-2409`                          | ✓           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v6/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-flash`                         | ✗           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v6/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-pro`                           | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v6/providers/ai-sdk-providers/cerebras)                         | `llama3.1-8b`                               | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v6/providers/ai-sdk-providers/cerebras)                         | `llama3.1-70b`                              | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v6/providers/ai-sdk-providers/cerebras)                         | `llama3.3-70b`                              | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v6/providers/ai-sdk-providers/groq)                                 | `meta-llama/llama-4-scout-17b-16e-instruct` | ✓           | ✓                 | ✓          | ✓              |
| [Groq](/v6/providers/ai-sdk-providers/groq)                                 | `llama-3.3-70b-versatile`                   | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v6/providers/ai-sdk-providers/groq)                                 | `llama-3.1-8b-instant`                      | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v6/providers/ai-sdk-providers/groq)                                 | `mixtral-8x7b-32768`                        | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v6/providers/ai-sdk-providers/groq)                                 | `gemma2-9b-it`                              | ✗           | ✓                 | ✓          | ✓              |

This table is not exhaustive. Additional models can be found in the provider
documentation pages and on the provider websites.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)