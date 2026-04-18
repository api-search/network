---
description: Usage statistics for the API call.
layout: schema
name: Usage
properties_list:
- description: Number of tokens in the prompt.
  name: prompt_tokens
  type: integer
- description: Number of tokens in the generated completion.
  name: completion_tokens
  type: integer
- description: Total number of tokens used in the request.
  name: total_tokens
  type: integer
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-usage-schema.json
slug: azure-openai-service-usage
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Usage
---
