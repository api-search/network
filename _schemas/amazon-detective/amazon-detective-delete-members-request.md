---
description: Request to remove member accounts from a behavior graph
layout: schema
name: DeleteMembersRequest
properties_list:
- description: The ARN of the behavior graph to remove members from.
  name: GraphArn
  type: string
- description: The list of AWS account identifiers of the member accounts to remove.
  name: AccountIds
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-delete-members-request-schema.json
slug: amazon-detective-delete-members-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: DeleteMembersRequest
---
