---
description: PersonalDocumentData schema from Adyen API
layout: schema
name: PersonalDocumentData
properties_list:
- description: The expiry date of the document, in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**.
  name: expirationDate
  type: string
- description: The country where the document was issued, in the two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**.
  name: issuerCountry
  type: string
- description: The state where the document was issued (if applicable).
  name: issuerState
  type: string
- description: The number in the document.
  name: number
  type: string
- description: 'The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**, **VISA**. To delete an existing entry for a document `type`, send only the `type` field in your'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-personal-document-data-schema.json
slug: accounts-personal-document-data
tags:
- Payments
- Financial Services
- Fintech
title: PersonalDocumentData
---
