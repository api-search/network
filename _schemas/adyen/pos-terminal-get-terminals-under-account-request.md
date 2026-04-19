---
description: GetTerminalsUnderAccountRequest schema from Adyen API
layout: schema
name: GetTerminalsUnderAccountRequest
properties_list:
- description: Your company account. If you only specify this parameter, the response includes all terminals at all account levels.
  name: companyAccount
  type: string
- description: The merchant account. This is required if you are retrieving the terminals assigned to a store.If you don't specify a `store` the response includes the terminals assigned to the specified merchant acc
  name: merchantAccount
  type: string
- description: The store code of the store. With this parameter, the response only includes the terminals assigned to the specified store.
  name: store
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-get-terminals-under-account-request-schema.json
slug: pos-terminal-get-terminals-under-account-request
tags:
- Payments
- Financial Services
- Fintech
title: GetTerminalsUnderAccountRequest
---
