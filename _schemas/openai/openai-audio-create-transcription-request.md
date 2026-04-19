---
description: ''
layout: schema
name: CreateTranscriptionRequest
properties_list:
- description: 'The audio file object to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm. File uploads are limited to 25 MB.'
  name: file
  type: string
- description: ID of the model to use. Only whisper-1 and gpt-4o-transcribe are currently available.
  name: model
  type: string
- description: The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.
  name: language
  type: string
- description: An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language.
  name: prompt
  type: string
- description: The format of the transcript output. Defaults to json. verbose_json includes additional metadata like word-level timestamps.
  name: response_format
  type: string
- description: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
  name: temperature
  type: number
- description: The timestamp granularities to populate for this transcription. response_format must be set to verbose_json to use this parameter.
  name: timestamp_granularities
  type: array
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-audio-create-transcription-request-schema.json
slug: openai-audio-create-transcription-request
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CreateTranscriptionRequest
---
