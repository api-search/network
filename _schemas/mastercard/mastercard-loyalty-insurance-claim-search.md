---
description: ''
layout: schema
name: ClaimSearch
properties_list:
- description: Insurance claim identifier, cardholder should be able to retrieve once the claim is submitted on the target website.
  name: claimId
  type: string
- description: Postal code associated with insurance claim.
  name: postalCode
  type: string
- description: User's preferred language in localized ISO 639-1 format such as pt-BR
  name: preferredLanguage
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-loyalty-insurance-claim-search-schema.json
slug: mastercard-loyalty-insurance-claim-search
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ClaimSearch
---
