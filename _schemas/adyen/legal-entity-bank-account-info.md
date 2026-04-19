---
description: BankAccountInfo schema from Adyen API
layout: schema
name: BankAccountInfo
properties_list:
- description: Identification of the bank account.
  name: accountIdentification
  type: object
- description: The type of bank account.
  name: accountType
  type: string
- description: The name of the banking institution where the bank account is held.
  name: bankName
  type: string
- description: The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the bank account is registered. For example, **NL**.
  name: countryCode
  type: string
- description: Identifies if the bank account was created through [instant bank verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding).
  name: trustedSource
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-bank-account-info-schema.json
slug: legal-entity-bank-account-info
tags:
- Payments
- Financial Services
- Fintech
title: BankAccountInfo
---
