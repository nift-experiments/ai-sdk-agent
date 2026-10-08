---
title: DefaultGeneratedFile
description: API Reference for DefaultGeneratedFile.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/default-generated-file"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

A concrete implementation of the `GeneratedFile` interface that provides lazy conversion between base64 and Uint8Array formats.

```ts
import { DefaultGeneratedFile } from 'ai';

const file = new DefaultGeneratedFile({
  data: uint8ArrayData,
  mediaType: 'image/png',
});

console.log(file.base64); // Automatically converted to base64
console.log(file.uint8Array); // Original Uint8Array
```

## Import

```
import { DefaultGeneratedFile } from "ai"
```

## Constructor

### Parameters

- `data` (`string | Uint8Array`): The file data as either a base64 encoded string or Uint8Array.
- `mediaType` (`string`): The IANA media type of the file.

## Properties

- `base64` (`string`): File as a base64 encoded string. Lazily converted from Uint8Array if needed.
- `uint8Array` (`Uint8Array`): File as a Uint8Array. Lazily converted from base64 if needed.
- `mediaType` (`string`): The IANA media type of the file.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)