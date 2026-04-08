---
aid: prisma:prisma-consumestreamevents
name: Prisma Consume events from a named stream
tags:
- Streams
humanURL: 
properties: []
description: >-
  Opens a long-lived connection to receive events from a named stream. Events are delivered in order with at-least-once delivery guarantees when event persistence is enabled. The connection uses server-sent events (SSE) for real-time delivery. If the stream was previously consumed and has a saved cursor position, events resume from that position.

---
