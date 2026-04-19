---
description: TerminalAssignment schema from Adyen API
layout: schema
name: TerminalAssignment
properties_list:
- description: The unique identifier of the company account to which terminal is assigned.
  name: companyId
  type: string
- description: The unique identifier of the merchant account to which terminal is assigned.
  name: merchantId
  type: string
- description: Indicates where the terminal is in the process of being reassigned to.
  name: reassignmentTarget
  type: object
- description: 'The status of the reassignment. Possible values: * `reassignmentInProgress`: the terminal was boarded and is now scheduled to remove the configuration. Wait for the terminal to synchronize with the Ad'
  name: status
  type: string
- description: The unique identifier of the store to which terminal is assigned.
  name: storeId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-assignment-schema.json
slug: management-terminal-assignment
tags:
- Payments
- Financial Services
- Fintech
title: TerminalAssignment
---
