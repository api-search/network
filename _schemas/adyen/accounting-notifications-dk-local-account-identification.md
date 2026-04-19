---
description: DKLocalAccountIdentification schema from Adyen API
layout: schema
name: DKLocalAccountIdentification
properties_list:
- description: The 4-10 digits bank account number (Kontonummer) (without separators or whitespace).
  name: accountNumber
  type: string
- description: The 4-digit bank code (Registreringsnummer) (without separators or whitespace).
  name: bankCode
  type: string
- description: '**dkLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-dk-local-account-identification-schema.json
slug: accounting-notifications-dk-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: DKLocalAccountIdentification
---
