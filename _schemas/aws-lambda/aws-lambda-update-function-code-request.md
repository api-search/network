---
description: Request body for updating a function's code
layout: schema
name: UpdateFunctionCodeRequest
properties_list:
- description: Base64-encoded contents of the deployment package. AWS SDK and CLI clients handle encoding automatically.
  name: ZipFile
  type: string
- description: An S3 bucket in the same AWS Region as the function
  name: S3Bucket
  type: string
- description: The S3 key of the deployment package
  name: S3Key
  type: string
- description: For versioned S3 objects, the version of the deployment package
  name: S3ObjectVersion
  type: string
- description: URI of a container image in Amazon ECR
  name: ImageUri
  type: string
- description: Set to true to publish a new version of the function after updating the code
  name: Publish
  type: boolean
- description: Set to true to validate the request without updating the code
  name: DryRun
  type: boolean
- description: Update only if the revision ID matches
  name: RevisionId
  type: string
- description: ''
  name: Architectures
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-update-function-code-request-schema.json
slug: aws-lambda-update-function-code-request
tags: []
title: UpdateFunctionCodeRequest
---
