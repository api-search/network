---
aid: prisma:prisma-createstream
name: Prisma Create a named event stream
tags:
- Streams
humanURL: 
properties: []
description: >-
  Creates a new named event stream for a specific database model. Named streams are resumable, meaning that if the consumer disconnects and reconnects with the same stream name, it will resume from where it left off. Requires event persistence to be enabled on the environment. The stream() API provides at-least-once delivery with correct ordering guarantees.

---
