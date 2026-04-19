---
description: Details about a published layer version
layout: schema
name: PublishLayerVersionResponse
properties_list:
- description: ''
  name: Content
  type: object
- description: The ARN of the layer
  name: LayerArn
  type: string
- description: The ARN of the layer version
  name: LayerVersionArn
  type: string
- description: Description of the version
  name: Description
  type: string
- description: The date the layer version was created in ISO 8601 format
  name: CreatedDate
  type: string
- description: The version number
  name: Version
  type: integer
- description: ''
  name: CompatibleRuntimes
  type: array
- description: ''
  name: LicenseInfo
  type: string
- description: ''
  name: CompatibleArchitectures
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-publish-layer-version-response-schema.json
slug: aws-lambda-publish-layer-version-response
tags: []
title: PublishLayerVersionResponse
---
