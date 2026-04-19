---
description: Summary information about a layer version
layout: schema
name: LayerVersionSummary
properties_list:
- description: The ARN of the layer version
  name: LayerVersionArn
  type: string
- description: The version number
  name: Version
  type: integer
- description: Description of the version
  name: Description
  type: string
- description: The date the version was created
  name: CreatedDate
  type: string
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
schema_file: json-schema/aws-lambda-layer-version-summary-schema.json
slug: aws-lambda-layer-version-summary
tags: []
title: LayerVersionSummary
---
