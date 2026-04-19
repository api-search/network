---
description: Schema defining the structure of an Amazon Inspector vulnerability finding, including severity, resource details, vulnerability information, and remediation guidance.
layout: schema
name: Amazon Inspector Finding Definition
properties_list:
- description: The Amazon Resource Name (ARN) of the finding.
  name: findingArn
  type: string
- description: The severity of the finding.
  name: severity
  type: string
- description: The status of the finding.
  name: status
  type: string
- description: The type of the finding.
  name: type
  type: string
- description: The title of the finding.
  name: title
  type: string
- description: The description of the finding.
  name: description
  type: string
- description: The AWS account ID associated with the finding.
  name: awsAccountId
  type: string
- description: The date and time the finding was first observed.
  name: firstObservedAt
  type: string
- description: The date and time the finding was last observed.
  name: lastObservedAt
  type: string
- description: The date and time the finding was last updated.
  name: updatedAt
  type: string
- description: The Amazon Inspector score for the finding.
  name: inspectorScore
  type: number
- description: The resources affected by the finding.
  name: resources
  type: array
- description: ''
  name: remediation
  type: object
- description: ''
  name: packageVulnerabilityDetails
  type: object
- description: ''
  name: networkReachabilityDetails
  type: object
provider_name: Amazon Inspector
provider_slug: amazon-inspector
schema_file: json-schema/amazon-inspector-schema.json
slug: amazon-inspector
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
title: Amazon Inspector Finding Definition
---
