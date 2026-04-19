---
description: Response from listing invitations
layout: schema
name: ListInvitationsResponse
properties_list:
- description: The list of behavior graphs for which the member account has open or accepted invitations.
  name: Invitations
  type: array
- description: If there are more invitations remaining in the results, then use this pagination token.
  name: NextToken
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-invitations-response-schema.json
slug: amazon-detective-list-invitations-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListInvitationsResponse
---
