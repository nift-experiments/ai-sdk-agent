---
title: Stream Object with Image Prompt
description: Learn how to stream structured data with an image prompt using the AI SDK and Node
url: "https://ai-sdk.dev/v5/cookbook/node/stream-object-with-image-prompt"
docs_index: /llms.txt
tags:
  - node
  - streaming
  - structured data
  - multimodal
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Some language models that support vision capabilities accept images as part of the prompt. Here are some of the different [formats](/v5/docs/reference/ai-sdk-core/generate-text#content-image) you can use to include images as input.

## URL

```ts title='index.ts'
import { streamObject } from 'ai';
import dotenv from 'dotenv';
import { z } from 'zod';

dotenv.config();

async function main() {
  const { partialObjectStream } = streamObject({
    model: 'openai/gpt-4.1',
    maxOutputTokens: 512,
    schema: z.object({
      stamps: z.array(
        z.object({
          country: z.string(),
          date: z.string(),
        }),
      ),
    }),
    messages: [
      {
        role: 'user',
        content: [
          {
            type: 'text',
            text: 'list all the stamps in these passport pages?',
          },
          {
            type: 'image',
            image: new URL(
              'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/WW2_Spanish_official_passport.jpg/1498px-WW2_Spanish_official_passport.jpg',
            ),
          },
        ],
      },
    ],
  });

  for await (const partialObject of partialObjectStream) {
    console.clear();
    console.log(partialObject);
  }
}

main();
```

## File Buffer

```ts title='index.ts'
import { streamObject } from 'ai';
import dotenv from 'dotenv';
import { z } from 'zod';
import fs from 'fs';

dotenv.config();

async function main() {
  const { partialObjectStream } = streamObject({
    model: 'openai/gpt-4.1',
    maxOutputTokens: 512,
    schema: z.object({
      stamps: z.array(
        z.object({
          country: z.string(),
          date: z.string(),
        }),
      ),
    }),
    messages: [
      {
        role: 'user',
        content: [
          {
            type: 'text',
            text: 'list all the stamps in these passport pages?',
          },
          {
            type: 'image',
            image: fs.readFileSync('./data/passport.png', {
              encoding: 'base64',
            }),
          },
        ],
      },
    ],
  });

  for await (const partialObject of partialObjectStream) {
    console.clear();
    console.log(partialObject);
  }
}

main();
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)