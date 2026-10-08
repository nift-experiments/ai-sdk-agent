---
title: streamToResponse
description: Learn to use streamToResponse helper function in your application.
url: "https://ai-sdk.dev/v5/docs/reference/stream-helpers/stream-to-response"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

`streamToResponse` has been removed in AI SDK 4.0. Use
`pipeDataStreamToResponse` from
[streamText](/v5/docs/reference/ai-sdk-core/stream-text) instead.

`streamToResponse` pipes a data stream to a Node.js `ServerResponse` object and sets the status code and headers.

This is useful to create data stream responses in environments that use `ServerResponse` objects, such as Node.js HTTP servers.

The status code and headers can be configured using the `options` parameter.
By default, the status code is set to 200 and the Content-Type header is set to `text/plain; charset=utf-8`.

## Import

```
import { streamToResponse } from "ai"
```

## Example

You can e.g. use `streamToResponse` to pipe a data stream to a Node.js HTTP server response:

```ts
import { StreamData, streamText, streamToResponse } from 'ai';
import { createServer } from 'http';

createServer(async (req, res) => {
  const result = streamText({
    model: "anthropic/claude-sonnet-5.5",
    prompt: 'What is the weather in San Francisco?',
  });

  // use stream data
  const data = new StreamData();

  data.append('initialized call');

  streamToResponse(
    result.toAIStream({
      onFinal() {
        data.append('call completed');
        data.close();
      },
    }),
    res,
    {},
    data,
  );
}).listen(8080);
```

## API Signature

### Parameters

- `stream` (`ReadableStream`): The Web Stream to pipe to the response. It can be the return value of OpenAIStream, HuggingFaceStream, AnthropicStream, or an AIStream instance.
- `response` (`ServerResponse`): The Node.js ServerResponse object to pipe the stream to. This is usually the second argument of a Node.js HTTP request handler.
- `options` (`Options`): Configure the response
  - `Options`
    - `status` (`number`): The status code to set on the response. Defaults to \`200\`.
    - `headers` (`Record<string, string>`): Additional headers to set on the response. Defaults to \`\{ 'Content-Type': 'text/plain; charset=utf-8' }\`.
- `data` (`StreamData`): StreamData object for forwarding additional data to the client.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)