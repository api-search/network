---
description: Represents a completion response from the API.
layout: schema
name: CreateCompletionResponse
properties_list:
- description: A unique identifier for the completion.
  name: id
  type: string
- description: The object type.
  name: object
  type: string
- description: The Unix timestamp of when the completion was created.
  name: created
  type: integer
- description: The model used for completion.
  name: model
  type: string
- description: The list of completion choices.
  name: choices
  type: array
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-completion-response-schema.json
slug: azure-openai-service-create-completion-response
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateCompletionResponse
---
