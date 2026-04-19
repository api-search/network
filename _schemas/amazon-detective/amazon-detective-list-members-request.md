---
description: Request to list member accounts
layout: schema
name: ListMembersRequest
properties_list:
- description: The ARN of the behavior graph to list member accounts for.
  name: GraphArn
  type: string
- description: For requests to retrieve the next page of member account results.
  name: NextToken
  type: string
- description: The maximum number of member accounts to include in the response.
  name: MaxResults
  type: integer
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-members-request-schema.json
slug: amazon-detective-list-members-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListMembersRequest
---
