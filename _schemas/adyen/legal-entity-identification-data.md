---
description: IdentificationData schema from Adyen API
layout: schema
name: IdentificationData
properties_list:
- description: The card number of the document that was issued (AU only).
  name: cardNumber
  type: string
- description: The expiry date of the document, in YYYY-MM-DD format.
  name: expiryDate
  type: string
- description: The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**.
  name: issuerCountry
  type: string
- description: The state or province where the document was issued (AU only).
  name: issuerState
  type: string
- description: Applies only to individuals in the US. Set to **true** if the individual does not have an SSN. To verify their identity, Adyen will require them to upload an ID document.
  name: nationalIdExempt
  type: boolean
- description: The number in the document.
  name: number
  type: string
- description: Type of identity data. For **individual**, the `type` value is **nationalIdNumber**.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-identification-data-schema.json
slug: legal-entity-identification-data
tags:
- Payments
- Financial Services
- Fintech
title: IdentificationData
---
