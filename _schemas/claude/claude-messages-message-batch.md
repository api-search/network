---
description: A message batch object representing an asynchronous batch of message requests.
layout: schema
name: MessageBatch
properties_list:
- description: Unique identifier for the message batch.
  name: id
  type: string
- description: Object type. Always "message_batch".
  name: type
  type: string
- description: The processing status of the batch.
  name: processing_status
  type: string
- description: Tallies of requests by their status within the batch.
  name: request_counts
  type: object
- description: RFC 3339 datetime when the batch ended processing.
  name: ended_at
  type: string
- description: RFC 3339 datetime when the batch was created.
  name: created_at
  type: string
- description: RFC 3339 datetime when the batch results will expire.
  name: expires_at
  type: string
- description: URL to retrieve the batch results. Available when the batch is complete.
  name: results_url
  type: string
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-message-batch-schema.json
slug: claude-messages-message-batch
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: MessageBatch
---
