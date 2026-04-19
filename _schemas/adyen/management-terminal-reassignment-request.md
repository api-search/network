---
description: TerminalReassignmentRequest schema from Adyen API
layout: schema
name: TerminalReassignmentRequest
properties_list:
- description: The unique identifier of the company account to which the terminal is reassigned.
  name: companyId
  type: string
- description: 'Must be specified when reassigning terminals to a merchant account: - If set to **true**, reassigns terminals to the inventory of the merchant account and the terminals cannot process transactions. - '
  name: inventory
  type: boolean
- description: The unique identifier of the merchant account to which the terminal is reassigned. When reassigning terminals to a merchant account, you must specify the `inventory` field.
  name: merchantId
  type: string
- description: The unique identifier of the store to which the terminal is reassigned.
  name: storeId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-reassignment-request-schema.json
slug: management-terminal-reassignment-request
tags:
- Payments
- Financial Services
- Fintech
title: TerminalReassignmentRequest
---
