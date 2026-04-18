---
description: FunctionEnvelope resource specific properties
layout: schema
name: FunctionEnvelopeProperties
properties_list:
- description: Function App ID.
  name: function_app_id
  type: string
- description: Script root path URI.
  name: script_root_path_href
  type: string
- description: Script URI.
  name: script_href
  type: string
- description: Config URI.
  name: config_href
  type: string
- description: Test data URI.
  name: test_data_href
  type: string
- description: Secrets file URI.
  name: secrets_file_href
  type: string
- description: Function URI.
  name: href
  type: string
- description: Config information.
  name: config
  type: object
- description: File list.
  name: files
  type: object
- description: Test data used when testing via the Azure Portal.
  name: test_data
  type: string
- description: The invocation URL
  name: invoke_url_template
  type: string
- description: The function language
  name: language
  type: string
- description: Gets or sets a value indicating whether the function is disabled
  name: isDisabled
  type: boolean
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
schema_file: json-schema/azure-functions-function-envelope-properties-schema.json
slug: azure-functions-function-envelope-properties
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
title: FunctionEnvelopeProperties
---
