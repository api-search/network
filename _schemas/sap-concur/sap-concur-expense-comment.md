---
description: A comment on a report or expense
layout: schema
name: Comment
properties_list:
- description: The comment text content
  name: comment
  type: string
- description: The user who authored the comment
  name: author
  type: object
- description: When the comment was created
  name: creationDate
  type: string
- description: Whether this is the most recent comment
  name: isLatest
  type: boolean
- description: Whether this is a system-generated audit entry
  name: isAuditLog
  type: boolean
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-comment-schema.json
slug: sap-concur-expense-comment
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: Comment
---
