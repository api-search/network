---
description: Schema for an AWS Lambda function configuration. Defines the structure of a Lambda function resource including its code, runtime, execution role, memory, timeout, environment variables, VPC configuration, layers, concurrency, and other settings used by the Lambda service API.
layout: schema
name: AWS Lambda Function
properties_list:
- description: The name of the Lambda function. Can include letters, numbers, hyphens, and underscores. Must be between 1 and 64 characters.
  name: FunctionName
  type: string
- description: 'The function''s Amazon Resource Name (ARN). Format: arn:aws:lambda:{region}:{account-id}:function:{function-name}'
  name: FunctionArn
  type: string
- description: The identifier of the function's runtime. Required for .zip deployment packages. Not required for container image deployment packages.
  name: Runtime
  type: string
- description: The ARN of the function's execution role. This IAM role grants the function permission to access AWS services and resources.
  name: Role
  type: string
- description: The name of the method within your code that Lambda calls to run your function. The format includes the file name without an extension and the handler function or method name, separated by a dot (e.g.
  name: Handler
  type: string
- description: The size of the function's deployment package in bytes.
  name: CodeSize
  type: integer
- description: A description of the function's purpose.
  name: Description
  type: string
- description: The amount of time in seconds that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds (15 minutes).
  name: Timeout
  type: integer
- description: The amount of memory available to the function at runtime in megabytes. Lambda allocates CPU power in proportion to the amount of memory configured. The default is 128 MB. The value can be any multipl
  name: MemorySize
  type: integer
- description: The date and time that the function was last updated, in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
  name: LastModified
  type: string
- description: The SHA-256 hash of the function's deployment package.
  name: CodeSha256
  type: string
- description: The version of the Lambda function. $LATEST for the unpublished version, or a numeric string for a published version.
  name: Version
  type: string
- description: The function's networking configuration for connecting to resources in a VPC
  name: VpcConfig
  type: object
- description: A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing
  name: DeadLetterConfig
  type: object
- description: Environment variables that are accessible from function code during execution
  name: Environment
  type: object
- description: The ARN of the AWS KMS key used to encrypt the function's environment variables. If not provided, Lambda uses a default service key.
  name: KMSKeyArn
  type: string
- description: The function's AWS X-Ray tracing configuration
  name: TracingConfig
  type: object
- description: For Lambda@Edge functions, the ARN of the main function.
  name: MasterArn
  type: string
- description: The latest updated revision of the function or alias. Changes each time the function configuration or code is updated.
  name: RevisionId
  type: string
- description: A list of function layer ARNs (including version) applied to the function. Lambda applies layers in the order specified. Maximum of 5 layers.
  name: Layers
  type: array
- description: The current state of the function. When the state is Inactive, you can reactivate the function by invoking it.
  name: State
  type: string
- description: The reason for the function's current state.
  name: StateReason
  type: string
- description: The reason code for the function's current state. When the code is Creating, you cannot invoke or modify the function.
  name: StateReasonCode
  type: string
- description: The status of the last update that was performed on the function. Set to Successful after a function update completes.
  name: LastUpdateStatus
  type: string
- description: The reason for the last update that was performed on the function.
  name: LastUpdateStatusReason
  type: string
- description: The reason code for the last update that was performed on the function.
  name: LastUpdateStatusReasonCode
  type: string
- description: The type of deployment package. Zip for .zip file archive or Image for container image.
  name: PackageType
  type: string
- description: The function's image configuration values for container image deployment
  name: ImageConfigResponse
  type: object
- description: The instruction set architecture that the function supports. Lambda provides x86_64 (default) and arm64 (AWS Graviton2).
  name: Architectures
  type: array
- description: The size of the function's /tmp directory
  name: EphemeralStorage
  type: object
- description: SnapStart configuration to reduce cold start latency. Currently supported for Java runtime functions.
  name: SnapStart
  type: object
- description: The function's Amazon CloudWatch Logs configuration settings
  name: LoggingConfig
  type: object
- description: Key-value pairs attached to the function for organization, cost allocation, and access control.
  name: Tags
  type: object
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-function-schema.json
slug: aws-lambda-function
tags: []
title: AWS Lambda Function
---
