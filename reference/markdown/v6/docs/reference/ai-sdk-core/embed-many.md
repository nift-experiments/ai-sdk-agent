---
title: embedMany
description: API Reference for embedMany.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/embed-many"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Embed several values using an embedding model.

`embedMany` automatically splits large requests into smaller chunks when the
model has a limit on either the number of embeddings or the UTF-8 input bytes
that can be processed in a single call. Providers can use a conservative byte
budget to keep requests below aggregate token limits without adding a tokenizer
to the AI SDK core package. An individual value larger than the byte budget is
sent in its own call because splitting it would change the resulting embedding.

```ts
import { embedMany } from 'ai';

const { embeddings } = await embedMany({
  model: 'openai/text-embedding-3-small',
  values: [
    'sunny day at the beach',
    'rainy afternoon in the city',
    'snowy night in the mountains',
  ],
});
```

## Import

```
import { embedMany } from "ai"
```

## API Signature

### Parameters

- `model` (`EmbeddingModel`): The embedding model to use. Example: openai.embeddingModel('text-embedding-3-small')
- `values` (`Array<string>`): The values to embed.
- `maxRetries?` (`number`): Maximum number of retries. Set to 0 to disable retries. Default: 2.
- `abortSignal?` (`AbortSignal`): An optional abort signal that can be used to cancel the call.
- `headers?` (`Record<string, string>`): Additional HTTP headers to be sent with the request. Only applicable for HTTP-based providers.
- `providerOptions?` (`ProviderOptions`): Provider-specific options that are passed through to the provider.
- `maxParallelCalls?` (`number`): Maximum number of concurrent requests to the provider. Default: Infinity.
- `experimental_telemetry?` (`TelemetrySettings`): Telemetry configuration. Experimental feature.
  - `TelemetrySettings`
    - `isEnabled?` (`boolean`): Enable or disable telemetry. Disabled by default while experimental.
    - `recordInputs?` (`boolean`): Enable or disable input recording. Enabled by default.
    - `recordOutputs?` (`boolean`): Enable or disable output recording. Enabled by default.
    - `functionId?` (`string`): Identifier for this function. Used to group telemetry data by function.
    - `metadata?` (`Record<string, string | number | boolean | Array<null | undefined | string> | Array<null | undefined | number> | Array<null | undefined | boolean>>`): Additional information to include in the telemetry data.
    - `tracer?` (`Tracer`): A custom tracer to use for the telemetry data.

### Returns

- `values` (`Array<string>`): The values that were embedded.
- `embeddings` (`number[][]`): The embeddings. They are in the same order as the values.
- `usage` (`EmbeddingModelUsage`): The token usage for generating the embeddings.
  - `EmbeddingModelUsage`
    - `tokens` (`number`): The total number of input tokens.
- `warnings` (`Warning[]`): Warnings from the model provider (e.g. unsupported settings).
- `providerMetadata?` (`ProviderMetadata | undefined`): Optional metadata from the provider. The outer key is the provider name. The inner values are the metadata. Details depend on the provider.
- `responses?` (`Array<{ headers?: Record<string, string>; body?: unknown } | undefined>`): Optional raw response data from each chunk request. There may be multiple responses if the request was split into multiple chunks.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)