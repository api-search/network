---
description: PeopleSoft GL journal entry.
layout: schema
name: JournalEntry
properties_list:
- description: Business unit.
  name: BUSINESS_UNIT
  type: string
- description: Journal ID.
  name: JOURNAL_ID
  type: string
- description: Journal date.
  name: JOURNAL_DATE
  type: string
- description: Ledger name.
  name: LEDGER
  type: string
- description: Journal description.
  name: DESCR
  type: string
- description: Journal status.
  name: JRNL_HDR_STATUS
  type: string
- description: Currency code.
  name: CURRENCY_CD
  type: string
- description: Fiscal year.
  name: FISCAL_YEAR
  type: integer
- description: Accounting period.
  name: ACCOUNTING_PERIOD
  type: integer
- description: Journal lines.
  name: LINES
  type: array
provider_name: PeopleSoft
provider_slug: peoplesoft
schema_file: json-schema/peoplesoft-financials-journal-entry-schema.json
slug: peoplesoft-financials-journal-entry
tags:
- Campus Solutions
- CRM
- Enterprise Software
- ERP
- Financial Management
- HCM
- Supply Chain Management
title: JournalEntry
---
