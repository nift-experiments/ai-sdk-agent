---
title: valibotSchema
description: Helper function for creating Valibot schemas
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-core/valibot-schema"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

`valibotSchema`

is currently experimental.

`valibotSchema` is a helper function that converts a Valibot schema into a JSON schema object that is compatible with the AI SDK.
It takes a Valibot schema as input, and returns a typed schema.

You can use it to [generate structured data](/v5/docs/ai-sdk-core/generating-structured-data) and in [tools](/v5/docs/ai-sdk-core/tools-and-tool-calling).

## Example

```ts
import { valibotSchema } from '@ai-sdk/valibot';
import { object, string, array } from 'valibot';

const recipeSchema = valibotSchema(
  object({
    name: string(),
    ingredients: array(
      object({
        name: string(),
        amount: string(),
      }),
    ),
    steps: array(string()),
  }),
);
```

## Import

```
import { valibotSchema } from "ai"
```

## API Signature

### Parameters

- `valibotSchema` (`GenericSchema<unknown, T>`): The Valibot schema definition.

### Returns

A Schema object that is compatible with the AI SDK, containing both the JSON schema representation and validation functionality.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)