---
description: Configuration for a Lambda function URL
layout: schema
name: FunctionUrlConfig
properties_list:
- description: The HTTP URL endpoint for the function
  name: FunctionUrl
  type: string
- description: The ARN of the function
  name: FunctionArn
  type: string
- description: The type of authentication the function URL uses
  name: AuthType
  type: string
- description: When the function URL was created in ISO 8601 format
  name: CreationTime
  type: string
- description: When the function URL was last modified
  name: LastModifiedTime
  type: string
- description: Use BUFFERED for synchronous invocation or RESPONSE_STREAM for response streaming
  name: InvokeMode
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-function-url-config-schema.json
slug: aws-lambda-function-url-config
tags: []
title: FunctionUrlConfig
---
