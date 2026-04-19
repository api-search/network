---
description: A structure that identifies filter criteria for <code>GetCoverageStatistics</code>.
layout: schema
name: CoverageFilterCriteria
properties_list:
- description: ''
  name: accountId
  type: object
- description: ''
  name: ec2InstanceTags
  type: object
- description: ''
  name: ecrImageTags
  type: object
- description: ''
  name: ecrRepositoryName
  type: object
- description: ''
  name: lambdaFunctionName
  type: object
- description: ''
  name: lambdaFunctionRuntime
  type: object
- description: ''
  name: lambdaFunctionTags
  type: object
- description: ''
  name: lastScannedAt
  type: object
- description: ''
  name: resourceId
  type: object
- description: ''
  name: resourceType
  type: object
- description: ''
  name: scanStatusCode
  type: object
- description: ''
  name: scanStatusReason
  type: object
- description: ''
  name: scanType
  type: object
provider_name: Amazon Inspector
provider_slug: amazon-inspector
schema_file: json-schema/inspector-coverage-filter-criteria-schema.json
slug: inspector-coverage-filter-criteria
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
title: CoverageFilterCriteria
---
