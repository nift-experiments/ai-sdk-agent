---
title: "useChat \"An error occurred\""
description: "Troubleshooting errors related to the \"An error occurred\" error in useChat."
url: "https://ai-sdk.dev/v5/docs/troubleshooting/use-chat-an-error-occurred"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

## Issue

I am using [`useChat`](/v5/docs/reference/ai-sdk-ui/use-chat) and I get the error "An error occurred".

## Background

Error messages from `streamText` are masked by default when using `toDataStreamResponse` for security reasons (secure-by-default).
This prevents leaking sensitive information to the client.

## Solution

To forward error details to the client or to log errors, use the `getErrorMessage` function when calling `toDataStreamResponse`.

```tsx
export function errorHandler(error: unknown) {
  if (error == null) {
    return 'unknown error';
  }

  if (typeof error === 'string') {
    return error;
  }

  if (error instanceof Error) {
    return error.message;
  }

  return JSON.stringify(error);
}
```

```tsx
const result = streamText({
  // ...
});

return result.toUIMessageStreamResponse({
  getErrorMessage: errorHandler,
});
```

In case you are using `createDataStreamResponse`, you can use the `onError` function when calling `toDataStreamResponse`:

```tsx
const response = createDataStreamResponse({
  // ...
  async execute(dataStream) {
    // ...
  },
  onError: errorHandler,
});
```

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)