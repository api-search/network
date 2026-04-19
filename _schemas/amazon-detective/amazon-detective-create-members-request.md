---
description: Request to invite member accounts to a behavior graph
layout: schema
name: CreateMembersRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: Customized message text to include in the invitation email message.
  name: Message
  type: string
- description: If set to true, invitation emails are not sent.
  name: DisableEmailNotification
  type: boolean
- description: The list of AWS accounts to invite to become member accounts.
  name: Accounts
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-create-members-request-schema.json
slug: amazon-detective-create-members-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: CreateMembersRequest
---
