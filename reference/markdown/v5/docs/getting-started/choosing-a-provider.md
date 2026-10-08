---
title: Choosing a Provider
description: Learn how to configure and authenticate with AI providers in the AI SDK.
url: "https://ai-sdk.dev/v5/docs/getting-started/choosing-a-provider"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The AI SDK supports dozens of model providers through [first-party](/v5/providers/ai-sdk-providers), [OpenAI-compatible](/v5/providers/openai-compatible-providers), and [community](/v5/providers/community-providers) packages.

```ts
import { generateText } from 'ai';

const { text } = await generateText({
  model: "anthropic/claude-sonnet-5.5",
  prompt: 'What is love?',
});
```

## AI Gateway

The [Vercel AI Gateway](/v5/providers/ai-sdk-providers/ai-gateway) is the fastest way to get started with the AI SDK. Access models from OpenAI, Anthropic, Google, and other providers. Authenticate with [OIDC](https://ai-sdk.dev/v5/providers/ai-sdk-providers/ai-gateway#oidc-authentication-vercel-deployments) or an AI Gateway API key

<div className="max-w-[40%] mx-auto">
  [Get an API Key](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai%3Futm_source%3Dgateway-models-page\&title=Get+Started+with+Vercel+AI+Gateway)
</div>

Add your API key to your environment:

```dotenv title=".env.local"
AI_GATEWAY_API_KEY=your_api_key_here
```

The AI Gateway is the default [global provider](/v5/docs/ai-sdk-core/provider-management#global-provider-configuration), so you can access models using a simple string:

```ts
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'What is love?',
});
```

You can also explicitly import and use the gateway provider:

```ts
// Option 1: Import from 'ai' package (included by default)
import { gateway } from 'ai';
model: gateway('anthropic/claude-sonnet-4.5');

// Option 2: Install and import from '@ai-sdk/gateway' package
import { gateway } from '@ai-sdk/gateway';
model: gateway('anthropic/claude-sonnet-4.5');
```

## Using Dedicated Providers

You can also use [first-party](/v5/providers/ai-sdk-providers), [OpenAI-compatible](/v5/providers/openai-compatible-providers), and [community](/v5/providers/community-providers) provider packages directly. Install the package and create a provider instance. For example, to use Anthropic:

<div className="my-4">
  #### pnpm

  ```
  pnpm add @ai-sdk/anthropic
  ```

  #### npm

  ```
  npm install @ai-sdk/anthropic
  ```

  #### yarn

  ```
  yarn add @ai-sdk/anthropic
  ```

  #### bun

  ```
  bun add @ai-sdk/anthropic
  ```
</div>

```ts
import { anthropic } from '@ai-sdk/anthropic';

model: anthropic('claude-sonnet-4-5');
```

You can change the default global provider so string model references use your preferred provider everywhere in your application. Learn more about [provider management](/v5/docs/ai-sdk-core/provider-management#global-provider-configuration).

See [available providers](/v5/providers/ai-sdk-providers) for setup instructions for each provider.

## Custom Providers

You can build your own provider to integrate any service with the AI SDK. The AI SDK provides a [Language Model Specification](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v3) that ensures compatibility across providers.

```ts
import { generateText } from 'ai';
import { yourProvider } from 'your-custom-provider';

const { text } = await generateText({
  model: yourProvider('your-model-id'),
  prompt: 'What is love?',
});
```

See [Writing a Custom Provider](/v5/providers/community-providers/custom-providers) for a complete guide.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)