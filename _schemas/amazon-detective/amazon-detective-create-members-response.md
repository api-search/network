---
description: Response from creating member accounts
layout: schema
name: CreateMembersResponse
properties_list:
- description: The set of member account invitation or enablement requests.
  name: Members
  type: array
- description: The list of accounts for which Detective was unable to process the invitation.
  name: UnprocessedAccounts
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-create-members-response-schema.json
slug: amazon-detective-create-members-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: CreateMembersResponse
---
