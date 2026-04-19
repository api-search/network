---
description: Request body for updating a function's configuration
layout: schema
name: UpdateFunctionConfigurationRequest
properties_list:
- description: The ARN of the function's execution role
  name: Role
  type: string
- description: The name of the function handler
  name: Handler
  type: string
- description: A description of the function
  name: Description
  type: string
- description: Execution timeout in seconds
  name: Timeout
  type: integer
- description: Memory allocated in MB
  name: MemorySize
  type: integer
- description: ''
  name: Environment
  type: object
- description: The runtime identifier
  name: Runtime
  type: string
- description: ''
  name: DeadLetterConfig
  type: object
- description: ''
  name: KMSKeyArn
  type: string
- description: ''
  name: TracingConfig
  type: object
- description: Update only if the revision ID matches. Prevents modifying a function that has changed since you last read it.
  name: RevisionId
  type: string
- description: ''
  name: Layers
  type: array
- description: ''
  name: EphemeralStorage
  type: object
- description: ''
  name: SnapStart
  type: object
- description: ''
  name: LoggingConfig
  type: object
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-update-function-configuration-request-schema.json
slug: aws-lambda-update-function-configuration-request
tags: []
title: UpdateFunctionConfigurationRequest
---
