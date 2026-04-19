---
description: TerminalReassignmentTarget schema from Adyen API
layout: schema
name: TerminalReassignmentTarget
properties_list:
- description: The unique identifier of the company account to which the terminal is reassigned.
  name: companyId
  type: string
- description: Indicates if the terminal is reassigned to the inventory of the merchant account. - If **true**, the terminal is in the inventory of the merchant account and cannot process transactions. - If **false*
  name: inventory
  type: boolean
- description: The unique identifier of the merchant account to which the terminal is reassigned.
  name: merchantId
  type: string
- description: The unique identifier of the store to which the terminal is reassigned.
  name: storeId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-reassignment-target-schema.json
slug: management-terminal-reassignment-target
tags:
- Payments
- Financial Services
- Fintech
title: TerminalReassignmentTarget
---
