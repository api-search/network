---
description: Represents an Amazon GuardDuty security finding with its associated details, severity, and metadata.
layout: schema
name: Amazon GuardDuty Finding
properties_list:
- description: The unique identifier of the finding
  name: id
  type: string
- description: The AWS account ID where the finding was generated
  name: accountId
  type: string
- description: The AWS Region where the finding was generated
  name: region
  type: string
- description: The type of finding (e.g., UnauthorizedAccess:EC2/MaliciousIPCaller)
  name: type
  type: string
- description: The severity of the finding (0.0 to 10.0)
  name: severity
  type: number
- description: The title of the finding
  name: title
  type: string
- description: The description of the finding
  name: description
  type: string
- description: The confidence level of the finding
  name: confidence
  type: number
- description: The resource affected by the finding
  name: resource
  type: object
- description: Additional information about the finding
  name: service
  type: object
- description: The time the finding was first observed
  name: createdAt
  type: string
- description: The time the finding was last updated
  name: updatedAt
  type: string
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
schema_file: json-schema/amazon-guardduty-schema.json
slug: amazon-guardduty
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
title: Amazon GuardDuty Finding
---
