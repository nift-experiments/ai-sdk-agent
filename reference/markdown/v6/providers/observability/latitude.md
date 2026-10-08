---
title: Latitude
description: Monitor and debug your AI SDK application with Latitude
url: "https://ai-sdk.dev/v6/providers/observability/latitude"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

[Latitude](https://latitude.so) ([GitHub](https://github.com/latitude-dev/latitude-llm)) is an open-source MIT-licensed platform for AI agent observability with semantic trace search and issue tracking. It integrates with the AI SDK to capture:

- Traces of every `generateText`, `streamText`, and tool call
- Token usage and latency per call
- Errors and failure patterns grouped as recurring issues

## Setup

Latitude ships an SDK that wires up OpenTelemetry under the hood. The AI SDK emits spans through its `experimental_telemetry` flag and Latitude collects them.

Install the SDK:

#### pnpm

```
pnpm add @latitude-data/telemetry
```

#### npm

```
npm install @latitude-data/telemetry
```

#### yarn

```
yarn add @latitude-data/telemetry
```

#### bun

```
bun add @latitude-data/telemetry
```

Sign in at [app.latitude.so](https://app.latitude.so) and grab your API key and project slug from the dashboard. Set them in your environment:

```bash title=".env"
LATITUDE_API_KEY="..."
LATITUDE_PROJECT_SLUG="..."
```

Initialize Latitude once at startup and set `experimental_telemetry.isEnabled` to `true` on AI SDK calls:

```ts
import { Latitude, capture } from '@latitude-data/telemetry';
import { generateText } from 'ai';
import { openai } from '@ai-sdk/openai';

const latitude = new Latitude({
  apiKey: process.env.LATITUDE_API_KEY!,
  project: process.env.LATITUDE_PROJECT_SLUG!,
});

await capture('generate-support-reply', async () => {
  const { text } = await generateText({
    model: openai('gpt-4o'),
    prompt: 'Hello',
    experimental_telemetry: {
      isEnabled: true,
    },
  });
  return text;
});

await latitude.shutdown();
```

The `capture()` wrapper groups all AI SDK calls inside the callback under a single named trace. `shutdown()` flushes pending spans before the process exits.

## Resources

- [Latitude Vercel AI SDK guide](https://docs.latitude.so/telemetry/frameworks/vercel-ai-sdk)
- [Latitude documentation](https://docs.latitude.so)
- [GitHub repository](https://github.com/latitude-dev/latitude-llm)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)