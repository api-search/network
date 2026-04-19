---
description: MigratedShareholders schema from Adyen API
layout: schema
name: MigratedShareholders
properties_list:
- description: The unique identifier of the legal entity of that shareholder in the balance platform.
  name: legalEntityCode
  type: string
- description: The unique identifier of the account of the migrated shareholder in the classic integration.
  name: shareholderCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-migrated-shareholders-schema.json
slug: accounts-migrated-shareholders
tags:
- Payments
- Financial Services
- Fintech
title: MigratedShareholders
---
