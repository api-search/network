---
description: CartesBancairesInfo schema from Adyen API
layout: schema
name: CartesBancairesInfo
properties_list:
- description: 'Cartes Bancaires SIRET. Format: 14 digits.'
  name: siret
  type: string
- description: Information regarding the transaction description.
  name: transactionDescription
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-cartes-bancaires-info-schema.json
slug: management-cartes-bancaires-info
tags:
- Payments
- Financial Services
- Fintech
title: CartesBancairesInfo
---
