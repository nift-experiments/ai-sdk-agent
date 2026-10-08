---
title: createMCPClient
description: Create a client for connecting to MCP servers
url: "https://ai-sdk.dev/v6/docs/reference/ai-sdk-core/create-mcp-client"
docs_index: /llms.txt
---

> For an index of all documentation, see [/llms.txt](/llms.txt).

Creates a lightweight Model Context Protocol (MCP) client that connects to an MCP server. The client provides:

- **Tools**: Automatic conversion between MCP tools and AI SDK tools
- **Resources**: Methods to list, read, and discover resource templates from MCP servers
- **Prompts**: Methods to list available prompts and retrieve prompt messages
- **Completions**: Methods to request autocompletion suggestions for prompt arguments and resource template variables
- **Elicitation**: Support for handling server requests for additional input during tool execution

It currently does not support accepting notifications from an MCP server, and custom configuration of the client.

## Import

```
import { createMCPClient } from "@ai-sdk/mcp"
```

## API Signature

### Parameters

- `config` (`MCPClientConfig`): Configuration for the MCP client.
  - `MCPClientConfig`
    - `transport` (`MCPTransportConfig | MCPTransport`): Configuration for the message transport layer.
      - `MCPTransport`
        - `start` (`() => Promise<void>`): A method that starts the transport
        - `send` (`(message: JSONRPCMessage) => Promise<void>`): A method that sends a message through the transport
        - `close` (`() => Promise<void>`): A method that closes the transport
        - `onclose` (`() => void`): A method that is called when the transport is closed
        - `onerror` (`(error: Error) => void`): A method that is called when the transport encounters an error
        - `onmessage` (`(message: JSONRPCMessage) => void`): A method that is called when the transport receives a message
      - `MCPTransportConfig`
        - `type` (`'sse' | 'http`): Use Server-Sent Events for communication
        - `url` (`string`): URL of the MCP server
        - `headers?` (`Record<string, string>`): Additional HTTP headers to be sent with requests.
        - `authProvider?` (`OAuthClientProvider`): Optional OAuth provider for authorization to access protected remote MCP servers. Implement \`validateAuthorizationServerURL\` on the provider to allowlist discovered OAuth authorization server URLs before metadata is fetched.
        - `redirect?` (`'follow' | 'error'`): Controls how HTTP redirects are handled for transport requests. Set to 'error' to reject any redirect response, preventing servers from redirecting requests to unintended hosts. Defaults to 'follow'.
    - `initializationOptions?` (`RequestOptions`): Optional signal and timeout settings that bound transport startup and the initialize request. A timeout or abort closes the transport and rejects createMCPClient.
    - `clientName?` (`string`): Client name. Defaults to "ai-sdk-mcp-client".
    - `name?` (`string`): Deprecated. Use \`clientName\` instead. Defaults to "ai-sdk-mcp-client".
    - `version?` (`string`): Client version. Defaults to "1.0.0"
    - `onUncaughtError?` (`(error: unknown) => void`): Handler for uncaught errors
    - `maxRetries?` (`number`): Maximum number of retries for transient MCP tool call failures. Set to 0 to disable retries. Defaults to 0. Retries are opt-in and apply to tools/call requests.
    - `capabilities?` (`ClientCapabilities`): Optional client capabilities to advertise during initialization. For example, set \{ elicitation: \{} } to enable handling elicitation requests from the server.

### Returns

Returns a Promise that resolves to an `MCPClient` with the following properties and methods:

- `serverInfo` (`Configuration`): Information about the connected MCP server (name, version, optional title), as reported during the initialize handshake.
- `instructions?` (`string`): Optional instructions provided by the server during the initialize handshake. Describes how to use the server and its features. Useful for inclusion in the LLM system prompt.
- `tools` (`async (options?: {
      schemas?: TOOL_SCHEMAS
    }) => Promise<McpToolSet<TOOL_SCHEMAS>>`): Gets the tools available from the MCP server.
  - `options`
    - `schemas?` (`TOOL_SCHEMAS`): Schema definitions for compile-time type checking. When not provided, schemas are inferred from the server. Each tool schema can include inputSchema for typed inputs, and optionally outputSchema for typed outputs when the server returns structuredContent.
  - `TOOL_SCHEMAS`
    - `inputSchema` (`FlexibleSchema`): Zod schema or JSON schema defining the expected input parameters for the tool.
    - `outputSchema?` (`FlexibleSchema`): Zod schema or JSON schema defining the expected output structure. When provided, the client extracts and validates structuredContent from tool results, giving you typed outputs.
- `listResources` (`async (options?: {
      params?: PaginatedRequest['params'];
      options?: RequestOptions;
    }) => Promise<ListResourcesResult>`): Lists all available resources from the MCP server.
  - `options`
    - `params?` (`PaginatedRequest['params']`): Optional pagination parameters including cursor.
    - `options?` (`RequestOptions`): Optional request options including signal and timeout.
- `readResource` (`async (args: {
      uri: string;
      options?: RequestOptions;
    }) => Promise<ReadResourceResult>`): Reads the contents of a specific resource by URI.
  - `args`
    - `uri` (`string`): The URI of the resource to read.
    - `options?` (`RequestOptions`): Optional request options including signal and timeout.
- `listResourceTemplates` (`async (options?: {
      options?: RequestOptions;
    }) => Promise<ListResourceTemplatesResult>`): Lists all available resource templates from the MCP server.
  - `options`
    - `options?` (`RequestOptions`): Optional request options including signal and timeout.
- `complete` (`async (args: CompleteRequestParams & {
      options?: RequestOptions;
    }) => Promise<CompleteResult>`): Requests autocompletion suggestions for a prompt argument or resource template variable. The server must advertise the completions capability.
  - `args`
    - `ref` (`{ type: 'ref/prompt'; name: string } | { type: 'ref/resource'; uri: string }`): Reference to the prompt or resource template being completed.
    - `argument` (`{ name: string; value: string }`): Argument name and current partial value to complete.
    - `context?` (`{ arguments: Record<string, string> }`): Previously resolved argument values used to provide context for multi-argument prompts or resource templates.
    - `options?` (`RequestOptions`): Optional request options including signal and timeout.
- `experimental_listPrompts` (`async (options?: {
      params?: PaginatedRequest['params'];
      options?: RequestOptions;
    }) => Promise<ListPromptsResult>`): Lists available prompts from the MCP server. This method is experimental and may change in the future.
  - `options`
    - `params?` (`PaginatedRequest['params']`): Optional pagination parameters including cursor.
    - `options?` (`RequestOptions`): Optional request options including signal and timeout.
- `experimental_getPrompt` (`async (args: {
      name: string;
      arguments?: Record<string, unknown>;
      options?: RequestOptions;
    }) => Promise<GetPromptResult>`): Retrieves a prompt by name, optionally passing arguments. This method is experimental and may change in the future.
  - `args`
    - `name` (`string`): Prompt name to retrieve.
    - `arguments?` (`Record<string, unknown>`): Optional arguments to fill into the prompt.
    - `options?` (`RequestOptions`): Optional request options including signal and timeout.
- `onElicitationRequest` (`(
      schema: typeof ElicitationRequestSchema,
      handler: (request: ElicitationRequest) => Promise<ElicitResult> | ElicitResult
    ) => void`): Registers a handler for elicitation requests from the MCP server. The handler receives requests when the server needs additional input during tool execution.
  - `parameters`
    - `schema` (`typeof ElicitationRequestSchema`): The schema to validate requests against. Must be ElicitationRequestSchema.
    - `handler` (`(request: ElicitationRequest) => Promise<ElicitResult> | ElicitResult`): A function that handles the elicitation request. The request contains a message and requestedSchema. The handler must return an object with an action ("accept", "decline", or "cancel") and optionally content when accepting.
- `close` (`() => Promise<void>`): Closes the connection to the MCP server and cleans up resources.

## Example

```typescript
import { createMCPClient } from '@ai-sdk/mcp';
import { generateText } from 'ai';
import { Experimental_StdioMCPTransport } from '@ai-sdk/mcp/mcp-stdio';

let client;

try {
  client = await createMCPClient({
    transport: new Experimental_StdioMCPTransport({
      command: 'node server.js',
    }),
  });

  const tools = await client.tools();

  const response = await generateText({
    model: "anthropic/claude-sonnet-5.5",
    tools,
    messages: [{ role: 'user', content: 'Query the data' }],
  });

  console.log(response);
} catch (error) {
  console.error('Error:', error);
} finally {
  // ensure the client is closed even if an error occurs
  if (client) {
    await client.close();
  }
}
```

## Error Handling

The client throws `MCPClientError` for:

- Client initialization failures
- Protocol version mismatches
- Missing server capabilities
- Connection failures

For tool execution, errors are propagated as `CallToolError` errors.

For unknown errors, the client exposes an `onUncaughtError` callback that can be used to manually log or handle errors that are not covered by known error types.

---

For a semantic overview of all documentation, see [/sitemap.md](/sitemap.md)

For an index of all available documentation, see [/llms.txt](/llms.txt)

For agent-facing discovery, including API and MCP surfaces, see [/agents.md](/agents.md)