---
description: This data structure conveys the identification of the account and the associated loyalty brand. Data related to a loyalty account processed in the transaction.
layout: schema
name: LoyaltyAccount
properties_list:
- description: ''
  name: LoyaltyAccountID
  type: object
- description: If a card is analysed.
  name: LoyaltyBrand
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-loyalty-account-schema.json
slug: terminal-loyalty-account
tags:
- Payments
- Financial Services
- Fintech
title: LoyaltyAccount
---
