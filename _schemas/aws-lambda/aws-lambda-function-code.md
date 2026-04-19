---
description: The code for the Lambda function. You can provide your deployment package as a .zip file archive uploaded directly, from S3, or as a container image from Amazon ECR.
layout: schema
name: FunctionCode
properties_list:
- description: Base64-encoded contents of the deployment package .zip file
  name: ZipFile
  type: string
- description: An S3 bucket in the same AWS Region as your function
  name: S3Bucket
  type: string
- description: The S3 key of the deployment package
  name: S3Key
  type: string
- description: The version of the S3 object for versioned buckets
  name: S3ObjectVersion
  type: string
- description: URI of a container image in the Amazon ECR registry
  name: ImageUri
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-function-code-schema.json
slug: aws-lambda-function-code
tags: []
title: FunctionCode
---
