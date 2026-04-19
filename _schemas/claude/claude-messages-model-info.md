---
description: Metadata about a Claude model.
layout: schema
name: ModelInfo
properties_list:
- description: Unique model identifier.
  name: id
  type: string
- description: Object type. Always "model" for model objects.
  name: type
  type: string
- description: A human-readable name for the model.
  name: display_name
  type: string
- description: RFC 3339 datetime string representing when the model was released.
  name: created_at
  type: string
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-model-info-schema.json
slug: claude-messages-model-info
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: ModelInfo
---
