---
description: An AWS Lambda function.
layout: schema
name: Function
properties_list:
- description: The name of the function.
  name: FunctionName
  type: string
- description: The function's Amazon Resource Name (ARN).
  name: FunctionArn
  type: string
- description: The function's runtime identifier.
  name: Runtime
  type: string
- description: The function's execution role ARN.
  name: Role
  type: string
- description: The function that Lambda calls to begin execution.
  name: Handler
  type: string
- description: The size of the function's deployment package, in bytes.
  name: CodeSize
  type: integer
- description: The function's description.
  name: Description
  type: string
- description: The amount of time (in seconds) that Lambda allows a function to run.
  name: Timeout
  type: integer
- description: The amount of memory available to the function at runtime.
  name: MemorySize
  type: integer
- description: The date and time the function was last updated.
  name: LastModified
  type: string
- description: The current state of the function.
  name: State
  type: string
- description: The type of deployment package.
  name: PackageType
  type: string
provider_name: Amazon Lambda
provider_slug: amazon-lambda
schema_file: json-schema/amazon-lambda-function-schema.json
slug: amazon-lambda-function
tags:
- AWS
- Compute
- Event-Driven
- FaaS
- Functions
- Serverless
title: Function
---
