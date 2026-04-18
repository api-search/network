---
description: Cognitive Services account.
layout: schema
name: Account
properties_list:
- description: Fully qualified resource ID.
  name: id
  type: string
- description: The name of the resource.
  name: name
  type: string
- description: The type of the resource.
  name: type
  type: string
- description: Resource ETag.
  name: etag
  type: string
- description: The kind (type) of cognitive service account. Examples include OpenAI, TextAnalytics, ComputerVision, SpeechServices, etc.
  name: kind
  type: string
- description: The geo-location where the resource lives.
  name: location
  type: string
- description: Resource tags.
  name: tags
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cognitive-services-account-schema.json
slug: azure-cognitive-services-account
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Account
---
