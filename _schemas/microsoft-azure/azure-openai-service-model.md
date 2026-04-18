---
description: Describes an OpenAI model.
layout: schema
name: Model
properties_list:
- description: The model identifier.
  name: id
  type: string
- description: ''
  name: object
  type: string
- description: The Unix timestamp when the model was created.
  name: created
  type: integer
- description: The organization that owns the model.
  name: owned_by
  type: string
- description: The capabilities of the model.
  name: capabilities
  type: object
- description: The lifecycle status of the model.
  name: lifecycle_status
  type: string
- description: Deprecation information for the model.
  name: deprecation
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-model-schema.json
slug: azure-openai-service-model
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Model
---
