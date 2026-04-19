---
description: BankAccountIdentificationTypeRequirement schema from Adyen API
layout: schema
name: BankAccountIdentificationTypeRequirement
properties_list:
- description: 'List of bank account identification types: eg.; [iban , numberAndBic]'
  name: bankAccountIdentificationTypes
  type: array
- description: Specifies the bank account details for a particular route per required field in this object depending on the country of the bank account and the currency of the transfer.
  name: description
  type: string
- description: '**bankAccountIdentificationTypeRequirement**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-bank-account-identification-type-requirement-schema.json
slug: configuration-bank-account-identification-type-requirement
tags:
- Payments
- Financial Services
- Fintech
title: BankAccountIdentificationTypeRequirement
---
