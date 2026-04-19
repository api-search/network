---
description: An organization member with expense management access
layout: schema
name: Member
properties_list:
- description: Unique member identifier
  name: id
  type: string
- description: Member email address
  name: email
  type: string
- description: Member first name
  name: first_name
  type: string
- description: Member last name
  name: last_name
  type: string
- description: Current member status
  name: status
  type: string
- description: Member role in the organization
  name: role
  type: string
- description: Department the member belongs to
  name: department
  type: string
- description: Timestamp when the member was created
  name: created_at
  type: string
provider_name: Abacus
provider_slug: abacus
schema_file: json-schema/abacus-member-schema.json
slug: abacus-member
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
title: Member
---
