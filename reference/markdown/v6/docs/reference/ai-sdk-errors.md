---
title: AI SDK Errors
description: Reference for AI SDK error classes and typed error handling.
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-errors"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

The AI SDK exposes typed errors so applications can handle expected failure
modes without matching error message strings.

## Importing Errors

The application package is named `ai`, not `@ai-sdk/ai`. It re-exports common
provider-level errors from `@ai-sdk/provider` together with the higher-level
errors raised by AI SDK Core:

```typescript
import { APICallError, NoObjectGeneratedError } from 'ai';
```

Provider implementations that depend directly on `@ai-sdk/provider` can import
its provider-level errors from that package instead:

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
the class provides it. The static guard also works when multiple AI SDK package
versions are loaded.

## Common Failure Modes

| Failure mode                                                                           | Error to check                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A provider request fails because of a network error or non-success response            | [`APICallError`](/v6/docs/reference/ai-sdk-errors/ai-api-call-error)                                                                                                                                                                                                                           |
| Automatic retries fail after multiple attempts                                         | [`RetryError`](/v6/docs/reference/ai-sdk-errors/ai-retry-error)                                                                                                                                                                                                                                |
| A structured output cannot be parsed or validated                                      | [`NoObjectGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-object-generated-error); inspect its `cause` for [`JSONParseError`](/v6/docs/reference/ai-sdk-errors/ai-json-parse-error) or [`TypeValidationError`](/v6/docs/reference/ai-sdk-errors/ai-type-validation-error)                    |
| A generation call returns no usable output                                             | [`NoOutputGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-output-generated-error) or the modality-specific `No*GeneratedError`                                                                                                                                                         |
| A model calls a missing tool or supplies invalid tool input                            | [`NoSuchToolError`](/v6/docs/reference/ai-sdk-errors/ai-no-such-tool-error) or [`InvalidToolInputError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error)                                                                                                                            |
| Tool-call repair fails                                                                 | [`ToolCallRepairError`](/v6/docs/reference/ai-sdk-errors/ai-tool-call-repair-error)                                                                                                                                                                                                            |
| A response violates an enforced `toolChoice`                                           | [`ToolChoiceViolationError`](/v6/docs/reference/ai-sdk-errors/ai-tool-choice-violation-error)                                                                                                                                                                                                  |
| Message history contains unresolved tool calls or invalid approvals                    | [`MissingToolResultsError`](/v6/docs/troubleshooting/missing-tool-results-error), [`InvalidToolApprovalError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-error), or [`InvalidToolApprovalSignatureError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-signature-error) |
| A provider or model cannot be resolved                                                 | [`NoSuchProviderError`](/v6/docs/reference/ai-sdk-errors/ai-no-such-provider-error) or [`NoSuchModelError`](/v6/docs/reference/ai-sdk-errors/ai-no-such-model-error)                                                                                                                              |
| A provider response is empty, malformed, or invalid                                    | [`EmptyResponseBodyError`](/v6/docs/reference/ai-sdk-errors/ai-empty-response-body-error), [`JSONParseError`](/v6/docs/reference/ai-sdk-errors/ai-json-parse-error), or [`InvalidResponseDataError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-response-data-error)                                |
| The requested model or provider does not support a capability or specification version | [`UnsupportedFunctionalityError`](/v6/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error) or [`UnsupportedModelVersionError`](/v6/docs/troubleshooting/unsupported-model-version)                                                                                                    |
| UI messages cannot be converted or a UI message stream is invalid                      | [`MessageConversionError`](/v6/docs/reference/ai-sdk-errors/ai-message-conversion-error) or [`UIMessageStreamError`](/v6/docs/reference/ai-sdk-errors/ai-ui-message-stream-error)                                                                                                                 |

## Error Reference

### Base Error

- `AISDKError`: Base class and broad type guard for AI SDK errors.

### Provider Requests and Responses

- [`APICallError`](/v6/docs/reference/ai-sdk-errors/ai-api-call-error)
- [`DownloadError`](/v6/docs/reference/ai-sdk-errors/ai-download-error)
- [`EmptyResponseBodyError`](/v6/docs/reference/ai-sdk-errors/ai-empty-response-body-error)
- [`InvalidPromptError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-prompt-error)
- [`InvalidResponseDataError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-response-data-error)
- [`JSONParseError`](/v6/docs/reference/ai-sdk-errors/ai-json-parse-error)
- [`LoadAPIKeyError`](/v6/docs/reference/ai-sdk-errors/ai-load-api-key-error)
- [`LoadSettingError`](/v6/docs/reference/ai-sdk-errors/ai-load-setting-error)
- [`NoContentGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-content-generated-error)
- [`NoSuchModelError`](/v6/docs/reference/ai-sdk-errors/ai-no-such-model-error)
- [`RetryError`](/v6/docs/reference/ai-sdk-errors/ai-retry-error)
- [`TooManyEmbeddingValuesForCallError`](/v6/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error)
- [`TypeValidationError`](/v6/docs/reference/ai-sdk-errors/ai-type-validation-error)
- [`UnsupportedFunctionalityError`](/v6/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error)

### Inputs and Message Streams

- [`InvalidArgumentError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-argument-error)
- [`InvalidDataContentError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-data-content-error)
- [`InvalidMessageRoleError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-message-role-error)
- `InvalidStreamPartError`
- [`MessageConversionError`](/v6/docs/reference/ai-sdk-errors/ai-message-conversion-error)
- [`UIMessageStreamError`](/v6/docs/reference/ai-sdk-errors/ai-ui-message-stream-error)

### Generated Output

- [`NoImageGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-image-generated-error)
- [`NoObjectGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-object-generated-error)
- [`NoOutputGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-output-generated-error)
- [`NoSpeechGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-speech-generated-error)
- [`NoTranscriptGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-transcript-generated-error)
- [`NoVideoGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-video-generated-error)

### Providers and Model Compatibility

- [`NoSuchProviderError`](/v6/docs/reference/ai-sdk-errors/ai-no-such-provider-error)
- [`UnsupportedModelVersionError`](/v6/docs/troubleshooting/unsupported-model-version)

### Tools and Approvals

- [`InvalidToolApprovalError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-error)
- [`InvalidToolApprovalSignatureError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-approval-signature-error)
- [`InvalidToolInputError`](/v6/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error)
- [`MissingToolResultsError`](/v6/docs/troubleshooting/missing-tool-results-error)
- [`NoSuchToolError`](/v6/docs/reference/ai-sdk-errors/ai-no-such-tool-error)
- [`ToolCallNotFoundForApprovalError`](/v6/docs/reference/ai-sdk-errors/ai-tool-call-not-found-for-approval-error)
- [`ToolCallRepairError`](/v6/docs/reference/ai-sdk-errors/ai-tool-call-repair-error)
- [`ToolChoiceViolationError`](/v6/docs/reference/ai-sdk-errors/ai-tool-choice-violation-error)

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)