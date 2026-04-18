---
description: ''
layout: schema
name: JournalEntry
properties_list:
- description: Journal entry header identifier
  name: jeHeaderId
  type: integer
- description: Journal batch identifier
  name: jeBatchId
  type: integer
- description: Ledger identifier
  name: ledgerId
  type: integer
- description: Accounting period name
  name: periodName
  type: string
- description: Journal entry name
  name: journalName
  type: string
- description: Journal category
  name: journalCategory
  type: string
- description: Journal source
  name: journalSource
  type: string
- description: Currency code (ISO 4217)
  name: currencyCode
  type: string
- description: Journal status
  name: status
  type: string
- description: Journal description
  name: description
  type: string
- description: Journal effective date
  name: effectiveDate
  type: string
- description: ''
  name: lines
  type: array
- description: ''
  name: createdBy
  type: integer
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdatedBy
  type: integer
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/financial-services-journal-entry-schema.json
slug: financial-services-journal-entry
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: JournalEntry
---
