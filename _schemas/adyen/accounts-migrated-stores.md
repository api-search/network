---
description: MigratedStores schema from Adyen API
layout: schema
name: MigratedStores
properties_list:
- description: The unique identifier of the business line associated with the migrated account holder in the balance platform.
  name: businessLineId
  type: string
- description: The unique identifier of the store associated with the migrated account holder in the classic integration.
  name: storeCode
  type: string
- description: The unique identifier of the store associated with the migrated account holder in the balance platform.
  name: storeId
  type: string
- description: Your reference for the store in the classic integration. The [Customer Area](https://ca-test.adyen.com/) uses this value for the store description.
  name: storeReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-migrated-stores-schema.json
slug: accounts-migrated-stores
tags:
- Payments
- Financial Services
- Fintech
title: MigratedStores
---
