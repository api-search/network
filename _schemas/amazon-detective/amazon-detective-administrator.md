---
description: An organization admin account for Amazon Detective
layout: schema
name: Administrator
properties_list:
- description: The AWS account identifier of the Detective administrator account.
  name: AccountId
  type: string
- description: The ARN of the organization behavior graph.
  name: GraphArn
  type: string
- description: The date and time when the Detective administrator account was enabled.
  name: DelegationTime
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-administrator-schema.json
slug: amazon-detective-administrator
tags:
- AWS
- Forensics
- Investigation
- Security
title: Administrator
---
