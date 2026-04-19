---
description: Request to start an investigation
layout: schema
name: StartInvestigationRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: The unique Amazon Resource Name (ARN) of the IAM user and IAM role.
  name: EntityArn
  type: string
- description: The data and time when the investigation began.
  name: ScopeStartTime
  type: string
- description: The data and time when the investigation ended.
  name: ScopeEndTime
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-start-investigation-request-schema.json
slug: amazon-detective-start-investigation-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: StartInvestigationRequest
---
