---
description: A mapping between an AWS resource and a Lambda function. Lambda reads items from the event source and invokes the function.
layout: schema
name: EventSourceMappingConfiguration
properties_list:
- description: The identifier of the event source mapping
  name: UUID
  type: string
- description: The position in a stream from which to start reading
  name: StartingPosition
  type: string
- description: The time from which to start reading with AT_TIMESTAMP position
  name: StartingPositionTimestamp
  type: string
- description: The maximum number of records in each batch that Lambda pulls from the event source
  name: BatchSize
  type: integer
- description: Maximum amount of time in seconds to gather records before invoking the function
  name: MaximumBatchingWindowInSeconds
  type: integer
- description: The number of batches to process concurrently from each shard
  name: ParallelizationFactor
  type: integer
- description: The ARN of the event source
  name: EventSourceArn
  type: string
- description: The ARN of the Lambda function
  name: FunctionArn
  type: string
- description: The date that the event source mapping was last updated
  name: LastModified
  type: string
- description: The result of the last invocation
  name: LastProcessingResult
  type: string
- description: The state of the event source mapping
  name: State
  type: string
- description: The reason for the current state
  name: StateTransitionReason
  type: string
- description: Maximum age of a record that Lambda sends to a function for processing (in seconds). For Kinesis and DynamoDB Streams only.
  name: MaximumRecordAgeInSeconds
  type: integer
- description: If true, Lambda splits the batch in two and retries when a function returns an error
  name: BisectBatchOnFunctionError
  type: boolean
- description: Maximum number of retry attempts for failed batches. -1 means infinite retries.
  name: MaximumRetryAttempts
  type: integer
- description: The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources
  name: TumblingWindowInSeconds
  type: integer
- description: A list of current response type enums applied to the event source mapping
  name: FunctionResponseTypes
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-event-source-mapping-configuration-schema.json
slug: aws-lambda-event-source-mapping-configuration
tags: []
title: EventSourceMappingConfiguration
---
