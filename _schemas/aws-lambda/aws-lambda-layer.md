---
description: An Lambda layer attached to a function
layout: schema
name: Layer
properties_list:
- description: The ARN of the function layer
  name: Arn
  type: string
- description: The size of the layer archive in bytes
  name: CodeSize
  type: integer
- description: The ARN of a signing profile version
  name: SigningProfileVersionArn
  type: string
- description: The ARN of a signing job
  name: SigningJobArn
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-layer-schema.json
slug: aws-lambda-layer
tags: []
title: Layer
---
