---
description: ''
layout: schema
name: Annotation
properties_list:
- description: The type of annotation.
  name: type
  type: string
- description: The start index of the annotation in the text.
  name: start_index
  type: integer
- description: The end index of the annotation in the text.
  name: end_index
  type: integer
- description: The URL cited. Present for url_citation type.
  name: url
  type: string
- description: The title of the cited resource.
  name: title
  type: string
- description: The ID of the cited file. Present for file_citation and file_path types.
  name: file_id
  type: string
- description: The relevant quote from the file.
  name: quote
  type: string
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-responses-annotation-schema.json
slug: chatgpt-responses-annotation
tags:
- Agents
- AI
- ChatGPT
- Embeddings
- Fine-Tuning
- GPT-4
- GPT-5
- Language Model
- OpenAI
- Realtime
title: Annotation
---
