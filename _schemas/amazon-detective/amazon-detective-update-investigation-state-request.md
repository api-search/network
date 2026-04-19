---
description: Request to update the state of an investigation
layout: schema
name: UpdateInvestigationStateRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: The investigation ID of the investigation report.
  name: InvestigationId
  type: string
- description: The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.
  name: State
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-update-investigation-state-request-schema.json
slug: amazon-detective-update-investigation-state-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: UpdateInvestigationStateRequest
---
