---
description: Summary details of an investigation
layout: schema
name: InvestigationDetail
properties_list:
- description: The investigation ID of the investigation report.
  name: InvestigationId
  type: string
- description: The severity assigned to the investigation.
  name: Severity
  type: string
- description: The status based on the completion status of the investigation.
  name: Status
  type: string
- description: The current state of the investigation.
  name: State
  type: string
- description: The time stamp of the creation time of the investigation report.
  name: CreatedTime
  type: string
- description: The unique Amazon Resource Name (ARN) of the IAM user and IAM role.
  name: EntityArn
  type: string
- description: Type of entity. For example, IAM_ROLE or IAM_USER.
  name: EntityType
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-investigation-detail-schema.json
slug: amazon-detective-investigation-detail
tags:
- AWS
- Forensics
- Investigation
- Security
title: InvestigationDetail
---
