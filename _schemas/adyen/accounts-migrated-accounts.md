---
description: MigratedAccounts schema from Adyen API
layout: schema
name: MigratedAccounts
properties_list:
- description: The unique identifier of the account of the migrated account holder in the balance platform.
  name: balanceAccountId
  type: string
- description: The unique identifier of the account of the migrated account holder in the classic integration.
  name: virtualAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-migrated-accounts-schema.json
slug: accounts-migrated-accounts
tags:
- Payments
- Financial Services
- Fintech
title: MigratedAccounts
---
