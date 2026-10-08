---
title: embedMany
description: API Reference for embedMany.
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-core/embed-many"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Embed several values using an embedding model. The type of the value is defined
by the embedding model.

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

- `model` (`EmbeddingModel`): The embedding model to use. Example: openai.textEmbeddingModel('text-embedding-3-small')
- `values` (`Array<VALUE>`): The values to embed. The type depends on the model.
- `maxRetries?` (`number`): Maximum number of retries. Set to 0 to disable retries. Default: 2.
- `abortSignal?` (`AbortSignal`): An optional abort signal that can be used to cancel the call.
- `headers?` (`Record<string, string>`): Additional HTTP headers to be sent with the request. Only applicable for HTTP-based providers.
- `experimental_telemetry?` (`TelemetrySettings`): Telemetry configuration. Experimental feature.
  - `TelemetrySettings`
    - `isEnabled?` (`boolean`): Enable or disable telemetry. Disabled by default while experimental.
    - `recordInputs?` (`boolean`): Enable or disable input recording. Enabled by default.
    - `recordOutputs?` (`boolean`): Enable or disable output recording. Enabled by default.
    - `functionId?` (`string`): Identifier for this function. Used to group telemetry data by function.
    - `metadata?` (`Record<string, string | number | boolean | Array<null | undefined | string> | Array<null | undefined | number> | Array<null | undefined | boolean>>`): Additional information to include in the telemetry data.
    - `tracer?` (`Tracer`): A custom tracer to use for the telemetry data.

### Returns

- `values` (`Array<VALUE>`): The values that were embedded.
- `embeddings` (`number[][]`): The embeddings. They are in the same order as the values.
- `usage` (`EmbeddingModelUsage`): The token usage for generating the embeddings.
  - `EmbeddingModelUsage`
    - `tokens` (`number`): The total number of input tokens.
    - `body?` (`unknown`): The response body.
- `providerMetadata?` (`ProviderMetadata | undefined`): Optional metadata from the provider. The outer key is the provider name. The inner values are the metadata. Details depend on the provider.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)