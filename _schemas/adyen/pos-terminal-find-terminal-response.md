---
description: FindTerminalResponse schema from Adyen API
layout: schema
name: FindTerminalResponse
properties_list:
- description: The company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account.
  name: companyAccount
  type: string
- description: The merchant account that the terminal is associated with. If the response doesn't contain a `store` the terminal is assigned to this merchant account.
  name: merchantAccount
  type: string
- description: Boolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal is assigned to a merchant account. - If **true**, this indicates that the terminal is i
  name: merchantInventory
  type: boolean
- description: The store code of the store that the terminal is assigned to.
  name: store
  type: string
- description: The unique terminal ID.
  name: terminal
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-find-terminal-response-schema.json
slug: pos-terminal-find-terminal-response
tags:
- Payments
- Financial Services
- Fintech
title: FindTerminalResponse
---
