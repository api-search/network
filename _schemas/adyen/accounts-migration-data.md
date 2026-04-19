---
description: MigrationData schema from Adyen API
layout: schema
name: MigrationData
properties_list:
- description: The unique identifier of the account holder in the balance platform.
  name: accountHolderId
  type: string
- description: The unique identifier of the balance platfrom to which the account holder was migrated.
  name: balancePlatform
  type: string
- description: Set to **true** if the account holder has been migrated.
  name: migrated
  type: boolean
- description: Contains the mapping of virtual account codes (classic integration) to the balance account codes (balance platform) associated with the migrated account holder.
  name: migratedAccounts
  type: array
- description: Contains the mapping of shareholders associated with the migrated legal entities.
  name: migratedShareholders
  type: array
- description: Contains the mapping of business lines and stores associated with the migrated account holder.
  name: migratedStores
  type: array
- description: The date when account holder was migrated.
  name: migrationDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-migration-data-schema.json
slug: accounts-migration-data
tags:
- Payments
- Financial Services
- Fintech
title: MigrationData
---
