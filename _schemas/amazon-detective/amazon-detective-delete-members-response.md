---
description: Response from deleting member accounts
layout: schema
name: DeleteMembersResponse
properties_list:
- description: The list of AWS account identifiers of the member accounts that Detective successfully deleted.
  name: AccountIds
  type: array
- description: The list of member accounts that Detective was unable to delete.
  name: UnprocessedAccounts
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-delete-members-response-schema.json
slug: amazon-detective-delete-members-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: DeleteMembersResponse
---
