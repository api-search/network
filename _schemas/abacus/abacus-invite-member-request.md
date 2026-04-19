---
description: Request body for inviting a new member
layout: schema
name: InviteMemberRequest
properties_list:
- description: Email address for the new member
  name: email
  type: string
- description: First name of the new member
  name: first_name
  type: string
- description: Last name of the new member
  name: last_name
  type: string
- description: Role to assign to the new member
  name: role
  type: string
- description: Department to assign the new member to
  name: department
  type: string
provider_name: Abacus
provider_slug: abacus
schema_file: json-schema/abacus-invite-member-request-schema.json
slug: abacus-invite-member-request
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
title: InviteMemberRequest
---
