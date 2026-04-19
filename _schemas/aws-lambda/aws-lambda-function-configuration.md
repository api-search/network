---
description: A Lambda function's configuration and metadata
layout: schema
name: FunctionConfiguration
properties_list:
- description: The name of the function
  name: FunctionName
  type: string
- description: The function's Amazon Resource Name (ARN)
  name: FunctionArn
  type: string
- description: The identifier of the function's runtime. Runtime is required if the deployment package is a .zip file archive.
  name: Runtime
  type: string
- description: The function's execution role ARN
  name: Role
  type: string
- description: The function entrypoint in your code. The format includes the file name without extension and the handler function name (e.g. index.handler)
  name: Handler
  type: string
- description: The size of the function's deployment package in bytes
  name: CodeSize
  type: integer
- description: The function's description
  name: Description
  type: string
- description: The amount of time in seconds that Lambda allows a function to run before stopping it. Maximum is 900 seconds (15 minutes).
  name: Timeout
  type: integer
- description: The amount of memory available to the function at runtime in MB. Lambda allocates CPU power in proportion to the amount of memory configured.
  name: MemorySize
  type: integer
- description: The date and time the function was last updated in ISO 8601 format
  name: LastModified
  type: string
- description: The SHA-256 hash of the function's deployment package
  name: CodeSha256
  type: string
- description: The version of the Lambda function
  name: Version
  type: string
- description: The function's dead-letter queue configuration
  name: DeadLetterConfig
  type: object
- description: The function's environment variables
  name: Environment
  type: object
- description: The ARN of the KMS key used to encrypt the function's environment variables at rest
  name: KMSKeyArn
  type: string
- description: The function's X-Ray tracing configuration
  name: TracingConfig
  type: object
- description: For Lambda@Edge functions, the ARN of the main function
  name: MasterArn
  type: string
- description: The latest updated revision of the function
  name: RevisionId
  type: string
- description: The function's layers
  name: Layers
  type: array
- description: The current state of the function
  name: State
  type: string
- description: The reason for the function's current state
  name: StateReason
  type: string
- description: The reason code for the function's current state
  name: StateReasonCode
  type: string
- description: The status of the last update that was performed on the function
  name: LastUpdateStatus
  type: string
- description: The reason for the last update that was performed on the function
  name: LastUpdateStatusReason
  type: string
- description: The reason code for the last update
  name: LastUpdateStatusReasonCode
  type: string
- description: The type of deployment package
  name: PackageType
  type: string
- description: The function's image configuration values for container images
  name: ImageConfigResponse
  type: object
- description: The instruction set architecture that the function supports
  name: Architectures
  type: array
- description: The size of the function's /tmp directory in MB
  name: EphemeralStorage
  type: object
- description: The function's SnapStart setting for reducing cold start latency
  name: SnapStart
  type: object
- description: The ARN of the runtime and any errors that occurred
  name: RuntimeVersionConfig
  type: object
- description: The function's Amazon CloudWatch Logs configuration
  name: LoggingConfig
  type: object
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-function-configuration-schema.json
slug: aws-lambda-function-configuration
tags: []
title: FunctionConfiguration
---
