---
title: wrapImageModel
description: Function for wrapping an image model with middleware (API Reference)
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/wrap-image-model"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The `wrapImageModel` function provides a way to enhance the behavior of image models
by wrapping them with middleware.

```ts
import { generateImage, wrapImageModel } from 'ai';
import { openai } from '@ai-sdk/openai';

const model = wrapImageModel({
  model: openai.image('gpt-image-2'),
  middleware: yourImageModelMiddleware,
});

const { image } = await generateImage({
  model,
  prompt: 'Santa Claus driving a Cadillac',
});
```

## Import

```
import { wrapImageModel } from "ai"
```

## API Signature

### Parameters

- `model` (`ImageModelV3`): The original ImageModelV3 instance to be wrapped.
- `middleware` (`ImageModelV3Middleware | ImageModelV3Middleware[]`): The middleware to be applied to the image model. When multiple middlewares are provided, the first middleware will transform the input first, and the last middleware will be wrapped directly around the model.
- `modelId` (`string`): Optional custom model ID to override the original model's ID.
- `providerId` (`string`): Optional custom provider ID to override the original model's provider.

### Returns

A new `ImageModelV3` instance with middleware applied.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)