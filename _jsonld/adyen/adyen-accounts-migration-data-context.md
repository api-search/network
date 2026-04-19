---
class_count: 1
classes:
- MigrationData
context_file: json-ld/adyen-accounts-migration-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-migration-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Migration Data from Adyen.
layout: jsonld
name: Adyen Accounts Migration Data Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: accountHolderId
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: migrated
  type: boolean
- container: set
  name: migratedAccounts
  type: string
- container: set
  name: migratedShareholders
  type: string
- container: set
  name: migratedStores
  type: string
- container: ''
  name: migrationDate
  type: dateTime
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-migration-data-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
