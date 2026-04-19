---
description: Request body for updating an event source mapping
layout: schema
name: UpdateEventSourceMappingRequest
properties_list:
- description: The name or ARN of the Lambda function
  name: FunctionName
  type: string
- description: If true, the event source mapping is active
  name: Enabled
  type: boolean
- description: ''
  name: BatchSize
  type: integer
- description: ''
  name: MaximumBatchingWindowInSeconds
  type: integer
- description: ''
  name: MaximumRecordAgeInSeconds
  type: integer
- description: ''
  name: BisectBatchOnFunctionError
  type: boolean
- description: ''
  name: MaximumRetryAttempts
  type: integer
- description: ''
  name: ParallelizationFactor
  type: integer
- description: ''
  name: TumblingWindowInSeconds
  type: integer
- description: ''
  name: FunctionResponseTypes
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-update-event-source-mapping-request-schema.json
slug: aws-lambda-update-event-source-mapping-request
tags: []
title: UpdateEventSourceMappingRequest
---
