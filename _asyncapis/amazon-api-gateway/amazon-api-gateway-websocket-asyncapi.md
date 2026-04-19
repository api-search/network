---
channels:
- description: The $connect route is invoked when a client first connects to the WebSocket API. This is where authentication and authorization occur. The connection is established only if the integration returns a successful response. Query string parameters and headers from the initial HTTP upgrade request are available to the integration.
  name: connect
- description: The $disconnect route is invoked after a client disconnects from the WebSocket API. This route is best-effort and may not be invoked in all cases (e.g., network interruptions). Use this route for cleanup operations such as removing connection records from a database.
  name: disconnect
- description: The $default route is invoked when no other route matches the incoming message. This serves as a fallback handler for messages that do not match any custom route selection expression. It is also used when the route selection expression evaluates to a value that does not match any defined route key.
  name: default
- description: Custom routes are defined by route keys that match values derived from the route selection expression applied to incoming messages. The default route selection expression is $request.body.action, which extracts the action property from the JSON message body to determine routing.
  name: customRoute
- description: The @connections endpoint allows backend services to send messages to specific connected clients, retrieve connection information, or disconnect clients. This is accessed via HTTPS POST, GET, or DELETE from the backend.
  name: connectionManagement
description: Amazon API Gateway WebSocket APIs enable real-time two-way communication between clients and backend services. Clients connect via WebSocket protocol and exchange messages through routes that map to Lambda functions, HTTP endpoints, or other AWS services. The gateway manages connection lifecycle including $connect, $disconnect, and $default routes, plus custom routes based on message content.
layout: asyncapi
messages:
- description: ''
  name: ConnectionRequest
  summary: The initial connection request sent when a client establishes a WebSocket connection. Includes headers, query parameters, and request context from the HTTP upgrade request.
  title: WebSocket Connection Request
- description: ''
  name: DisconnectionNotice
  summary: Notification sent when a client disconnects from the WebSocket API, either through a clean close or due to a timeout or error.
  title: WebSocket Disconnection Notice
- description: ''
  name: DefaultMessage
  summary: A message received on the $default route when no custom route matches the incoming message content.
  title: Default Route Message
- description: ''
  name: CustomRouteMessage
  summary: A message matched to a custom route based on the route selection expression. The message body is passed to the route's integration.
  title: Custom Route Message
- description: ''
  name: PostToConnectionMessage
  summary: A message sent from the backend to a specific connected WebSocket client via the @connections management API.
  title: Post to Connection
- description: ''
  name: ConnectionStatusResponse
  summary: Connection information returned when querying the @connections management endpoint for a specific connection ID.
  title: Connection Status
name: Amazon API Gateway WebSocket API
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
servers:
- description: WebSocket API endpoint. Clients establish persistent connections to this endpoint for real-time bidirectional communication.
  name: websocketEndpoint
  protocol: wss
  url: ''
- description: The @connections management endpoint for sending messages to connected WebSocket clients and managing connection state from backend services.
  name: managementEndpoint
  protocol: https
  url: ''
slug: amazon-api-gateway-websocket-asyncapi
spec_file: asyncapi/amazon-api-gateway-websocket-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/asyncapi/amazon-api-gateway-websocket-asyncapi.yml
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
- AsyncAPI
- Webhooks
- Events
version: '2018-11-29'
---
