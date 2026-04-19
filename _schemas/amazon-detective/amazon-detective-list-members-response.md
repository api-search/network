---
description: Response from listing member accounts
layout: schema
name: ListMembersResponse
properties_list:
- description: The list of member accounts in the behavior graph.
  name: MemberDetails
  type: array
- description: If there are more member accounts remaining in the results, then use this pagination token.
  name: NextToken
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-members-response-schema.json
slug: amazon-detective-list-members-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListMembersResponse
---
