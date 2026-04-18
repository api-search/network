---
description: ''
layout: schema
name: JournalEntry
properties_list:
- description: Journal entry number
  name: JdtNum
  type: integer
- description: Reference date
  name: ReferenceDate
  type: string
- description: Remark or memo for the journal entry
  name: Memo
  type: string
- description: Debit and credit lines
  name: JournalEntryLines
  type: array
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-business-one-service-layer-journal-entry-schema.json
slug: sap-business-one-service-layer-journal-entry
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: JournalEntry
---
