---
channels:
- description: Publish/subscribe channel for order creation events. Messages are published to a topic exchange and routed to all bound queues.
  name: orderCreated
- description: Point-to-point channel for order processing. Messages are sent to a direct exchange and consumed by a single worker from a shared queue.
  name: orderProcessing
- description: Request channel for the request/reply pattern. Clients send requests with a reply-to header and correlation ID for response matching.
  name: orderStatusRequest
- description: Reply channel for the request/reply pattern. The server publishes responses to the client-specified reply-to queue with the matching correlation ID.
  name: orderStatusReply
- description: Fanout channel for broadcasting notifications to all subscribers. Uses a fanout exchange to deliver messages to every bound queue regardless of routing key.
  name: notifications
description: AsyncAPI specification for AMQP (Advanced Message Queuing Protocol) messaging patterns including publish/subscribe, request/reply, and point-to-point messaging. AMQP 0-9-1 defines exchanges, queues, and bindings as the core building blocks for flexible message routing.
layout: asyncapi
messages:
- description: ''
  name: OrderCreated
  summary: Event published when a new order is created
  title: Order Created Event
- description: ''
  name: OrderProcess
  summary: Command to process an order
  title: Order Processing Command
- description: ''
  name: OrderStatusRequest
  summary: Request for the current status of an order
  title: Order Status Request
- description: ''
  name: OrderStatusReply
  summary: Reply containing the current status of an order
  title: Order Status Reply
- description: ''
  name: Notification
  summary: A notification broadcast to all subscribers
  title: Notification Message
name: AMQP Messaging API
provider_name: AMQP
provider_slug: amqp
servers:
- description: Production AMQP broker
  name: production
  protocol: amqp
  url: ''
slug: amqp-messaging
spec_file: asyncapi/amqp-messaging.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/asyncapi/amqp-messaging.yml
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
