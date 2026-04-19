---
description: A registered payment beneficiary
layout: schema
name: Beneficiary
properties_list:
- description: Unique beneficiary identifier
  name: beneficiaryId
  type: string
- description: Owning customer identifier
  name: customerId
  type: string
- description: Name of the beneficiary
  name: beneficiaryName
  type: string
- description: Beneficiary account number
  name: accountNumber
  type: string
- description: Beneficiary IBAN
  name: iban
  type: string
- description: Beneficiary bank BIC/SWIFT code
  name: bic
  type: string
- description: Name of the beneficiary bank
  name: bankName
  type: string
- description: Country of the beneficiary bank
  name: bankCountry
  type: string
- description: Default payment currency
  name: currency
  type: string
- description: Type of beneficiary
  name: beneficiaryType
  type: string
- description: Beneficiary status
  name: status
  type: string
- description: User-defined nickname for the beneficiary
  name: nickname
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-beneficiary-schema.json
slug: temenos-transact-core-banking-beneficiary
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Beneficiary
---
