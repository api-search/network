---
aid: deno:deno-streamrevisionprogress
name: Stream revision build progress
tags:
- Revisions
humanURL: 
properties: []
description: >-
  Streams real-time build progress for a revision as it moves through the preparing, installing, building, and deploying stages. Returns a Server-Sent Events stream or newline-delimited JSON stream depending on the Accept header. The stream emits message events containing RevisionProgress objects, a done event on completion, and an error event on failure.

---
