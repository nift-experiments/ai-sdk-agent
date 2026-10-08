---
title: AI SDK Errors
description: Reference for AI SDK error classes and typed error handling.
url: "https://ai-sdk.dev/v5/docs/reference/ai-sdk-errors"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

AI SDK errors let you handle expected failure modes without matching error
message strings.

## Importing Errors

The AI SDK Core package is named `ai`, not `@ai-sdk/ai`. It re-exports many
provider-level errors from `@ai-sdk/provider` together with the higher-level
errors raised by AI SDK Core:

```typescript
import { APICallError, NoObjectGeneratedError } from 'ai';
```

Provider implementations that depend directly on `@ai-sdk/provider` can import
provider-level errors from that package instead:

```typescript
import { APICallError, InvalidResponseDataError } from '@ai-sdk/provider';
```

## Migrating to Typed Error Handling

Replace message matching or an unconditionally generic `catch` block with the
most specific static `isInstance` guard available. Check `AISDKError` last when
you need a fallback for any AI SDK error:

```typescript
import { AISDKError, APICallError, generateText } from 'ai';

try {
  await generateText({
    model,
    prompt: 'Write a vegetarian lasagna recipe for 4 people.',
  });
} catch (error) {
  if (APICallError.isInstance(error)) {
    console.error('Provider request failed:', error.statusCode);
    return;
  }

  if (AISDKError.isInstance(error)) {
    console.error('AI SDK error:', error.name);
    return;
  }

  throw error;
}
```

Prefer `ErrorClass.isInstance(error)` over `error instanceof ErrorClass` when
the class provides a class-specific guard. The static guards use shared markers
and therefore work when multiple AI SDK package versions are loaded.

In AI SDK 5, `NoSpeechGeneratedError` and `UnsupportedModelVersionError` do not
provide class-specific guards. Use `instanceof` to distinguish those exact
classes. Their inherited `isInstance` method only checks whether a value is any
`AISDKError`.

The experimental transcription API can throw an
`AI_NoTranscriptGeneratedError`, but AI SDK 5 does not export its class. Handle
it with `AISDKError.isInstance(error)` and check `error.name`.

## Common Failure Modes

| Failure mode                                                                | Error to check                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A provider request fails because of a network error or non-success response | [`APICallError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-api-call-error)                                                                                                                                                                                                                                |
| Automatic retries fail after multiple attempts                              | [`RetryError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-retry-error)                                                                                                                                                                                                                                     |
| A structured object cannot be parsed or validated                           | [`NoObjectGeneratedError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-no-object-generated-error); inspect its `cause` with [`JSONParseError.isInstance`](/v5/docs/reference/ai-sdk-errors/ai-json-parse-error) or [`TypeValidationError.isInstance`](/v5/docs/reference/ai-sdk-errors/ai-type-validation-error)  |
| A text stream finishes without producing an output step                     | `NoOutputGeneratedError.isInstance(error)`                                                                                                                                                                                                                                                                         |
| Image or speech generation returns no output                                | [`NoImageGeneratedError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-no-image-generated-error) or [`error instanceof NoSpeechGeneratedError`](/v5/docs/reference/ai-sdk-errors/ai-no-speech-generated-error)                                                                                                  |
| A model calls a missing tool or supplies invalid tool input                 | [`NoSuchToolError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-no-such-tool-error) or [`InvalidToolInputError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error)                                                                                                               |
| Tool-call repair fails                                                      | [`ToolCallRepairError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-tool-call-repair-error)                                                                                                                                                                                                                 |
| A provider or model cannot be resolved                                      | [`NoSuchProviderError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-no-such-provider-error) or [`NoSuchModelError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-no-such-model-error)                                                                                                                 |
| A provider response is empty, malformed, or invalid                         | [`EmptyResponseBodyError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-empty-response-body-error), [`JSONParseError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-json-parse-error), or [`InvalidResponseDataError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-invalid-response-data-error) |
| The requested capability or model specification version is unsupported      | [`UnsupportedFunctionalityError.isInstance(error)`](/v5/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error) or [`error instanceof UnsupportedModelVersionError`](/v5/docs/troubleshooting/unsupported-model-version)                                                                                        |

## Error Reference

This reference lists the error classes exported by the `ai` package.

### Base Error

- `AISDKError`: base class and broad type guard for AI SDK errors

### Provider Requests and Responses

- [`APICallError`](/v5/docs/reference/ai-sdk-errors/ai-api-call-error)
- [`DownloadError`](/v5/docs/reference/ai-sdk-errors/ai-download-error)
- [`EmptyResponseBodyError`](/v5/docs/reference/ai-sdk-errors/ai-empty-response-body-error)
- [`InvalidPromptError`](/v5/docs/reference/ai-sdk-errors/ai-invalid-prompt-error)
- [`InvalidResponseDataError`](/v5/docs/reference/ai-sdk-errors/ai-invalid-response-data-error)
- [`JSONParseError`](/v5/docs/reference/ai-sdk-errors/ai-json-parse-error)
- [`LoadAPIKeyError`](/v5/docs/reference/ai-sdk-errors/ai-load-api-key-error)
- [`LoadSettingError`](/v5/docs/reference/ai-sdk-errors/ai-load-setting-error)
- [`NoContentGeneratedError`](/v5/docs/reference/ai-sdk-errors/ai-no-content-generated-error)
- [`NoSuchModelError`](/v5/docs/reference/ai-sdk-errors/ai-no-such-model-error)
- [`RetryError`](/v5/docs/reference/ai-sdk-errors/ai-retry-error)
- [`TooManyEmbeddingValuesForCallError`](/v5/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error)
- [`TypeValidationError`](/v5/docs/reference/ai-sdk-errors/ai-type-validation-error)
- [`UnsupportedFunctionalityError`](/v5/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error)

### Inputs and Messages

- [`InvalidArgumentError`](/v5/docs/reference/ai-sdk-errors/ai-invalid-argument-error)
- [`InvalidDataContentError`](/v5/docs/reference/ai-sdk-errors/ai-invalid-data-content-error)
- [`InvalidMessageRoleError`](/v5/docs/reference/ai-sdk-errors/ai-invalid-message-role-error)
- `InvalidStreamPartError`
- [`MessageConversionError`](/v5/docs/reference/ai-sdk-errors/ai-message-conversion-error)

### Generated Output

- [`NoImageGeneratedError`](/v5/docs/reference/ai-sdk-errors/ai-no-image-generated-error)
- [`NoObjectGeneratedError`](/v5/docs/reference/ai-sdk-errors/ai-no-object-generated-error)
- `NoOutputGeneratedError`
- [`NoOutputSpecifiedError`](/v5/docs/reference/ai-sdk-errors/ai-no-output-specified-error)
- [`NoSpeechGeneratedError`](/v5/docs/reference/ai-sdk-errors/ai-no-speech-generated-error)

### Tools

- [`InvalidToolInputError`](/v5/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error)
- [`NoSuchToolError`](/v5/docs/reference/ai-sdk-errors/ai-no-such-tool-error)
- [`ToolCallRepairError`](/v5/docs/reference/ai-sdk-errors/ai-tool-call-repair-error)

### Provider Registry and Compatibility

- [`NoSuchProviderError`](/v5/docs/reference/ai-sdk-errors/ai-no-such-provider-error)
- [`UnsupportedModelVersionError`](/v5/docs/troubleshooting/unsupported-model-version)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)