---
description: Request to get member details
layout: schema
name: GetMembersRequest
properties_list:
- description: The ARN of the behavior graph to get member details for.
  name: GraphArn
  type: string
- description: The list of AWS account identifiers of the member accounts to get information on.
  name: AccountIds
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-get-members-request-schema.json
slug: amazon-detective-get-members-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: GetMembersRequest
---
