---
description: A response that contains the results of an AWS Lambda function finding aggregation.
layout: schema
name: LambdaFunctionAggregationResponse
properties_list:
- description: ''
  name: accountId
  type: object
- description: ''
  name: functionName
  type: object
- description: ''
  name: lambdaTags
  type: object
- description: ''
  name: lastModifiedAt
  type: object
- description: ''
  name: resourceId
  type: object
- description: ''
  name: runtime
  type: object
- description: An object that contains the counts of aggregated finding per severity.
  name: severityCounts
  type: object
provider_name: Amazon Inspector
provider_slug: amazon-inspector
schema_file: json-schema/inspector-lambda-function-aggregation-response-schema.json
slug: inspector-lambda-function-aggregation-response
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
title: LambdaFunctionAggregationResponse
---
