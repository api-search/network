---
description: Request body for creating a function URL
layout: schema
name: CreateFunctionUrlConfigRequest
properties_list:
- description: The type of authentication. NONE allows public unauthenticated access. AWS_IAM requires IAM authentication.
  name: AuthType
  type: string
- description: ''
  name: InvokeMode
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-create-function-url-config-request-schema.json
slug: aws-lambda-create-function-url-config-request
tags: []
title: CreateFunctionUrlConfigRequest
---
