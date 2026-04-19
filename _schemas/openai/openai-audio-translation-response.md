---
description: ''
layout: schema
name: TranslationResponse
properties_list:
- description: The translated text in English.
  name: text
  type: string
- description: The task performed, always translate.
  name: task
  type: string
- description: The detected language of the input audio.
  name: language
  type: string
- description: The duration of the input audio in seconds.
  name: duration
  type: number
- description: Segments of the translated text with timestamps.
  name: segments
  type: array
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-audio-translation-response-schema.json
slug: openai-audio-translation-response
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: TranslationResponse
---
