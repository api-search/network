---
description: Paginated list of message batches.
layout: schema
name: MessageBatchList
properties_list:
- description: ''
  name: data
  type: array
- description: Whether there are more results available.
  name: has_more
  type: boolean
- description: ID of the first item. Use as before_id for the previous page.
  name: first_id
  type: string
- description: ID of the last item. Use as after_id for the next page.
  name: last_id
  type: string
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-message-batch-list-schema.json
slug: claude-messages-message-batch-list
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: MessageBatchList
---
