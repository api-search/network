---
description: Request body for creating an event source mapping
layout: schema
name: CreateEventSourceMappingRequest
properties_list:
- description: The ARN of the event source. Required for Kinesis, DynamoDB Streams, SQS, MQ, MSK, and DocumentDB.
  name: EventSourceArn
  type: string
- description: The name or ARN of the Lambda function
  name: FunctionName
  type: string
- description: If true, the event source mapping is active
  name: Enabled
  type: boolean
- description: Maximum number of records in each batch
  name: BatchSize
  type: integer
- description: Maximum time to gather records before invoking
  name: MaximumBatchingWindowInSeconds
  type: integer
- description: Number of batches to process concurrently per shard
  name: ParallelizationFactor
  type: integer
- description: Starting position in the stream
  name: StartingPosition
  type: string
- description: ''
  name: StartingPositionTimestamp
  type: string
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
  name: TumblingWindowInSeconds
  type: integer
- description: ''
  name: FunctionResponseTypes
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-create-event-source-mapping-request-schema.json
slug: aws-lambda-create-event-source-mapping-request
tags: []
title: CreateEventSourceMappingRequest
---
