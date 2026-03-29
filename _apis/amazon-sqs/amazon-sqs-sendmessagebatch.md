---
aid: amazon-sqs:amazon-sqs-sendmessagebatch
name: Send up to 10 messages to a queue in a single request
tags:
- Messages
humanURL: 
properties: []
description: >-
  Delivers up to ten messages to the specified queue. This is a batch version of SendMessage. For a FIFO queue, multiple messages within a single batch are enqueued in the order they are sent. The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KiB.

---
