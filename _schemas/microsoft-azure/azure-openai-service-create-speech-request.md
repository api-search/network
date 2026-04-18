---
description: Request body for generating speech from text.
layout: schema
name: CreateSpeechRequest
properties_list:
- description: The TTS model to use.
  name: model
  type: string
- description: The text to generate audio for.
  name: input
  type: string
- description: The voice to use when generating the audio.
  name: voice
  type: string
- description: The format to audio in.
  name: response_format
  type: string
- description: The speed of the generated audio.
  name: speed
  type: number
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-speech-request-schema.json
slug: azure-openai-service-create-speech-request
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateSpeechRequest
---
