---
description: TransferInstrumentReference schema from Adyen API
layout: schema
name: TransferInstrumentReference
properties_list:
- description: The masked IBAN or bank account number.
  name: accountIdentifier
  type: string
- description: The unique identifier of the resource.
  name: id
  type: string
- description: Four last digits of the bank account number. If the transfer instrument is created using [instant bank account verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#relea
  name: realLastFour
  type: string
- description: Identifies if the bank account was created through [instant bank verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding).
  name: trustedSource
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-transfer-instrument-reference-schema.json
slug: legal-entity-transfer-instrument-reference
tags:
- Payments
- Financial Services
- Fintech
title: TransferInstrumentReference
---
