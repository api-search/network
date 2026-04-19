---
description: Response from getting investigation details
layout: schema
name: GetInvestigationResponse
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: The investigation ID of the investigation report.
  name: InvestigationId
  type: string
- description: The unique Amazon Resource Name (ARN) of the IAM user and IAM role.
  name: EntityArn
  type: string
- description: Type of entity. For example, IAM_ROLE or IAM_USER.
  name: EntityType
  type: string
- description: The creation time of the investigation report in UTC time stamp format.
  name: CreatedTime
  type: string
- description: The start date and time used to set the scope time within which you want Detective to investigate.
  name: ScopeStartTime
  type: string
- description: The end date and time used to set the scope time within which you want Detective to investigate.
  name: ScopeEndTime
  type: string
- description: The status based on the completion status of the investigation.
  name: Status
  type: string
- description: The severity assigned is based on the likelihood and impact of the indicators of compromise discovered in the investigation.
  name: Severity
  type: string
- description: The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.
  name: State
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-get-investigation-response-schema.json
slug: amazon-detective-get-investigation-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: GetInvestigationResponse
---
