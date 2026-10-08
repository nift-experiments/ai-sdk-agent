---
title: AI SDK Providers
description: Learn how to use AI SDK providers.
url: "https://ai-sdk.dev/v5/providers/ai-sdk-providers"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The AI SDK comes with several providers that you can use to interact with different language models:

There are also [community providers](./community-providers) that have been created using the [Language Model Specification](./community-providers/custom-providers).

## Provider support

Not all providers support all AI SDK features. Here's a quick comparison of the capabilities of popular models:

| Provider                                                                 | Model                                               | Image Input | Object Generation | Tool Usage | Tool Streaming |
| ------------------------------------------------------------------------ | --------------------------------------------------- | ----------- | ----------------- | ---------- | -------------- |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-4.6`                                          | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-4.5`                                          | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-4`                                            | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3`                                            | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3-fast`                                       | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3-mini`                                       | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-3-mini-fast`                                  | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-2-1212`                                       | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-2-vision-1212`                                | ✓           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-beta`                                         | ✗           | ✓                 | ✓          | ✓              |
| [xAI Grok](/v5/providers/ai-sdk-providers/xai)                              | `grok-vision-beta`                                  | ✓           | ✗                 | ✗          | ✗              |
| [Vercel](/v5/providers/ai-sdk-providers/vercel)                             | `v0-1.0-md`                                         | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-6-astra`                                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-6-luna`                                        | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-6-sol`                                         | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6`                                           | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6-luna`                                      | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6-sol`                                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.6-terra`                                     | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5`                                             | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-mini`                                        | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-nano`                                        | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-codex`                                       | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5-chat-latest`                                 | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1-chat-latest`                               | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1`                                           | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1-codex-mini`                                | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-5.1-codex`                                     | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-4.1`                                           | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-4.1-mini`                                      | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-4o`                                            | ✓           | ✓                 | ✓          | ✓              |
| [OpenAI](/v5/providers/ai-sdk-providers/openai)                             | `gpt-4o-mini`                                       | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-fable-5-1`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-5-5`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-5`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-fable-5`                                    | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-8`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-7`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-6`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-4-6`                                 | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-5`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-1`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-opus-4-0`                                   | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-sonnet-4-0`                                 | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-3-7-sonnet-latest`                          | ✓           | ✓                 | ✓          | ✓              |
| [Anthropic](/v5/providers/ai-sdk-providers/anthropic)                       | `claude-3-5-haiku-latest`                           | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-3.8-flash`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-3.1-pro-preview`                            | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-3-pro-preview`                              | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.5-pro`                                    | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.5-flash`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-3.8-flash`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-3.1-pro-preview`                            | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-3-pro-preview`                              | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-2.5-pro`                                    | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-2.5-flash`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `pixtral-large-latest`                              | ✓           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-large-latest`                              | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `magistral-medium-2506`                             | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `magistral-small-2506`                              | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-small-latest`                              | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `ministral-8b-latest`                               | ✗           | ✓                 | ✓          | ✓              |
| [Cohere](/v5/providers/ai-sdk-providers/cohere)                             | `command-a-03-2025`                                 | ✗           | ✓                 | ✓          | ✓              |
| [Cohere](/v5/providers/ai-sdk-providers/cohere)                             | `command-a-reasoning-08-2025`                       | ✗           | ✓                 | ✓          | ✓              |
| [Cohere](/v5/providers/ai-sdk-providers/cohere)                             | `command-r-plus`                                    | ✗           | ✓                 | ✓          | ✓              |
| [Cohere](/v5/providers/ai-sdk-providers/cohere)                             | `command-r`                                         | ✗           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v5/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-flash-vision-exp`                      | ✓           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v5/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-flash`                                 | ✗           | ✓                 | ✓          | ✓              |
| [DeepSeek](/v5/providers/ai-sdk-providers/deepseek)                         | `deepseek-v4-pro`                                   | ✗           | ✓                 | ✓          | ✓              |
| [Moonshot AI](/v5/providers/ai-sdk-providers/moonshotai)                    | `kimi-k3`                                           | ✓           | ✓                 | ✓          | ✓              |
| [Moonshot AI](/v5/providers/ai-sdk-providers/moonshotai)                    | `kimi-k2.7-code`                                    | ✓           | ✓                 | ✓          | ✓              |
| [Moonshot AI](/v5/providers/ai-sdk-providers/moonshotai)                    | `kimi-k2.6`                                         | ✓           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `meta-llama/llama-4-scout-17b-16e-instruct`         | ✓           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `deepseek-r1-distill-llama-70b`                     | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `llama-3.3-70b-versatile`                           | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `llama-3.1-8b-instant`                              | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `qwen-qwq-32b`                                      | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `mixtral-8x7b-32768`                                | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `gemma2-9b-it`                                      | ✗           | ✓                 | ✓          | ✓              |
| [Groq](/v5/providers/ai-sdk-providers/groq)                                 | `moonshotai/kimi-k2-instruct-0905`                  | ✗           | ✓                 | ✓          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | ✓           | ✗                 | ✗          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `meta-llama/Llama-4-Scout-17B-16E-Instruct`         | ✓           | ✗                 | ✗          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`       | ✗           | ✓                 | ✓          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `meta-llama/Llama-3.3-70B-Instruct`                 | ✗           | ✓                 | ✓          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `deepseek-ai/DeepSeek-V3`                           | ✗           | ✗                 | ✗          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `deepseek-ai/DeepSeek-R1`                           | ✗           | ✗                 | ✗          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`         | ✗           | ✗                 | ✗          | ✗              |
| [DeepInfra](/v5/providers/ai-sdk-providers/deepinfra)                       | `deepseek-ai/DeepSeek-R1-Turbo`                     | ✗           | ✗                 | ✗          | ✗              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-medium-latest`                             | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `mistral-medium-2505`                               | ✗           | ✓                 | ✓          | ✓              |
| [Mistral](/v5/providers/ai-sdk-providers/mistral)                           | `pixtral-12b-2409`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-2.0-flash-exp`                              | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-1.5-flash`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Google Generative AI](/v5/providers/ai-sdk-providers/google-generative-ai) | `gemini-1.5-pro`                                    | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-2.0-flash-exp`                              | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-1.5-flash`                                  | ✓           | ✓                 | ✓          | ✓              |
| [Google Vertex](/v5/providers/ai-sdk-providers/google-vertex)               | `gemini-1.5-pro`                                    | ✓           | ✓                 | ✓          | ✓              |
| [Cerebras](/v5/providers/ai-sdk-providers/cerebras)                         | `llama3.1-8b`                                       | ✗           | ✓                 | ✓          | ✓              |
| [Cerebras](/v5/providers/ai-sdk-providers/cerebras)                         | `llama3.3-70b`                                      | ✗           | ✓                 | ✓          | ✓              |
| [Fireworks](/v5/providers/ai-sdk-providers/fireworks)                       | `kimi-k2-instruct`                                  | ✗           | ✓                 | ✓          | ✗              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `openai/gpt-oss-120b`                               | ✗           | ✓                 | ✓          | ✓              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `Qwen/Qwen3-235B-A22B-Instruct-2507`                | ✗           | ✓                 | ✓          | ✓              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `Qwen/Qwen3-Coder-480B-A35B-Instruct`               | ✗           | ✓                 | ✓          | ✓              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `moonshotai/Kimi-K2-Instruct-0905`                  | ✗           | ✓                 | ✓          | ✓              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `deepseek-ai/DeepSeek-V3.1`                         | ✗           | ✓                 | ✓          | ✓              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `deepseek-ai/DeepSeek-R1-0528`                      | ✗           | ✓                 | ✓          | ✓              |
| [Baseten](/v5/providers/ai-sdk-providers/baseten)                           | `deepseek-ai/DeepSeek-V3-0324`                      | ✗           | ✓                 | ✓          | ✓              |
| [Alibaba](/v5/providers/ai-sdk-providers/alibaba)                           | `qwen-plus`                                         | ✗           | ✓                 | ✓          | ✓              |

This table is not exhaustive. Additional models can be found in the provider
documentation pages and on the provider websites.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)