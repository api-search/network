---
description: Common error response for all Azure Resource Manager APIs.
layout: schema
name: ErrorResponse
properties_list:
- description: The error code.
  name: code
  type: string
- description: The error message.
  name: message
  type: string
- description: The error target.
  name: target
  type: string
- description: The error details.
  name: details
  type: array
- description: The error additional info.
  name: additionalInfo
  type: array
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-resource-manager-error-response-schema.json
slug: azure-resource-manager-error-response
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: ErrorResponse
---
