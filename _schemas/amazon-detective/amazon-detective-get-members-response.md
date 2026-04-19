---
description: Response from getting member details
layout: schema
name: GetMembersResponse
properties_list:
- description: The member account details that Detective retrieved.
  name: MemberDetails
  type: array
- description: The requested member accounts for which Detective was unable to return member details.
  name: UnprocessedAccounts
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-get-members-response-schema.json
slug: amazon-detective-get-members-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: GetMembersResponse
---
