---
title: Speech
description: Learn how to generate speech from text with the AI SDK.
url: "https://ai-sdk.dev/v6/docs/ai-sdk-core/speech"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Speech is an experimental feature.

The AI SDK provides the [`generateSpeech`](/v6/docs/reference/ai-sdk-core/generate-speech)
function to generate speech from text using a speech model.

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';
import { openai } from '@ai-sdk/openai';

const audio = await generateSpeech({
  model: openai.speech('tts-1'),
  text: 'Hello, world!',
  voice: 'alloy',
});
```

To access the generated audio:

```ts
const audioData = result.audio.uint8Array; // audio data as Uint8Array
// or
const audioBase64 = result.audio.base64; // audio data as base64 string
```

## Settings

### Provider-Specific settings

You can set model-specific settings with the `providerOptions` parameter.

```ts {7-11}
import { experimental_generateSpeech as generateSpeech } from 'ai';
import { openai } from '@ai-sdk/openai';

const audio = await generateSpeech({
  model: openai.speech('tts-1'),
  text: 'Hello, world!',
  providerOptions: {
    openai: {
      // ...
    },
  },
});
```

### Abort Signals and Timeouts

`generateSpeech` accepts an optional `abortSignal` parameter of
type [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)
that you can use to abort the speech generation process or set a timeout.

```ts {7}
import { openai } from '@ai-sdk/openai';
import { experimental_generateSpeech as generateSpeech } from 'ai';

const audio = await generateSpeech({
  model: openai.speech('tts-1'),
  text: 'Hello, world!',
  abortSignal: AbortSignal.timeout(1000), // Abort after 1 second
});
```

### Custom Headers

`generateSpeech` accepts an optional `headers` parameter of type `Record<string, string>`
that you can use to add custom headers to the speech generation request.

```ts {7}
import { openai } from '@ai-sdk/openai';
import { experimental_generateSpeech as generateSpeech } from 'ai';

const audio = await generateSpeech({
  model: openai.speech('tts-1'),
  text: 'Hello, world!',
  headers: { 'X-Custom-Header': 'custom-value' },
});
```

### Warnings

Warnings (e.g. unsupported parameters) are available on the `warnings` property.

```ts
import { openai } from '@ai-sdk/openai';
import { experimental_generateSpeech as generateSpeech } from 'ai';

const audio = await generateSpeech({
  model: openai.speech('tts-1'),
  text: 'Hello, world!',
});

const warnings = audio.warnings;
```

### Error Handling

When `generateSpeech` cannot generate a valid audio, it throws a [`AI_NoSpeechGeneratedError`](/v6/docs/reference/ai-sdk-errors/ai-no-speech-generated-error).

This error can arise for any of the following reasons:

- The model failed to generate a response
- The model generated a response that could not be parsed

The error preserves the following information to help you log the issue:

- `responses`: Metadata about the speech model responses, including timestamp, model, and headers.
- `cause`: The cause of the error. You can use this for more detailed error handling.

```ts
import {
  experimental_generateSpeech as generateSpeech,
  NoSpeechGeneratedError,
} from 'ai';
import { openai } from '@ai-sdk/openai';

try {
  await generateSpeech({
    model: openai.speech('tts-1'),
    text: 'Hello, world!',
  });
} catch (error) {
  if (NoSpeechGeneratedError.isInstance(error)) {
    console.log('AI_NoSpeechGeneratedError');
    console.log('Cause:', error.cause);
    console.log('Responses:', error.responses);
  }
}
```

## Speech Models

| Provider                                                           | Model                    |
| ------------------------------------------------------------------ | ------------------------ |
| [OpenAI](/v6/providers/ai-sdk-providers/openai#speech-models)         | `tts-1`                  |
| [OpenAI](/v6/providers/ai-sdk-providers/openai#speech-models)         | `tts-1-hd`               |
| [OpenAI](/v6/providers/ai-sdk-providers/openai#speech-models)         | `gpt-4o-mini-tts`        |
| [Mistral](/v6/providers/ai-sdk-providers/mistral#speech-models)       | `voxtral-mini-tts-2603`  |
| [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs#speech-models) | `eleven_v3`              |
| [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs#speech-models) | `eleven_multilingual_v2` |
| [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs#speech-models) | `eleven_flash_v2_5`      |
| [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs#speech-models) | `eleven_flash_v2`        |
| [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs#speech-models) | `eleven_turbo_v2_5`      |
| [ElevenLabs](/v6/providers/ai-sdk-providers/elevenlabs#speech-models) | `eleven_turbo_v2`        |
| [Hume](/v6/providers/ai-sdk-providers/hume#speech-models)             | `default`                |
| [Fish Audio](/v6/providers/ai-sdk-providers/fish-audio#speech-models) | `s1`                     |
| [Fish Audio](/v6/providers/ai-sdk-providers/fish-audio#speech-models) | `s2-pro`                 |
| [Fish Audio](/v6/providers/ai-sdk-providers/fish-audio#speech-models) | `s2.1-pro`               |

Above are a small subset of the speech models supported by the AI SDK providers. For more, see the respective provider documentation.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)