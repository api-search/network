---
description: Request body for creating an audio transcription.
layout: schema
name: CreateTranscriptionRequest
properties_list:
- description: 'The audio file object to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.'
  name: file
  type: string
- description: The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.
  name: language
  type: string
- description: An optional text to guide the model's style or continue a previous audio segment.
  name: prompt
  type: string
- description: The format of the transcript output.
  name: response_format
  type: string
- description: The sampling temperature, between 0 and 1.
  name: temperature
  type: number
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-transcription-request-schema.json
slug: azure-openai-service-create-transcription-request
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateTranscriptionRequest
---
