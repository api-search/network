---
description: Request to start monitoring a member account
layout: schema
name: StartMonitoringMemberRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: The account ID of the member account to try to enable.
  name: AccountId
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-start-monitoring-member-request-schema.json
slug: amazon-detective-start-monitoring-member-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: StartMonitoringMemberRequest
---
