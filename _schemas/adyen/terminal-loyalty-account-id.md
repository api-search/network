---
description: In the Payment or the Loyalty Request message, it allows to identify the loyalty account by the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the Cashier on a scanner device). Identification of a Loyalty account.
layout: schema
name: LoyaltyAccountID
properties_list:
- description: ''
  name: EntryMode
  type: object
- description: ''
  name: IdentificationType
  type: object
- description: ''
  name: IdentificationSupport
  type: object
- description: ''
  name: LoyaltyID
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-loyalty-account-id-schema.json
slug: terminal-loyalty-account-id
tags:
- Payments
- Financial Services
- Fintech
title: LoyaltyAccountID
---
