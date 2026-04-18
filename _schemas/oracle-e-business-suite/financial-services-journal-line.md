---
description: ''
layout: schema
name: JournalLine
properties_list:
- description: Journal line number
  name: jeLineNum
  type: integer
- description: Chart of accounts code combination identifier
  name: codeCombinatonId
  type: integer
- description: Debit amount in functional currency
  name: accountedDr
  type: number
- description: Credit amount in functional currency
  name: accountedCr
  type: number
- description: Debit amount in entered currency
  name: enteredDr
  type: number
- description: Credit amount in entered currency
  name: enteredCr
  type: number
- description: Line description
  name: description
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/financial-services-journal-line-schema.json
slug: financial-services-journal-line
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: JournalLine
---
