---
description: Document schema from Adyen API
layout: schema
name: Document
properties_list:
- description: Object that contains the document.
  name: attachment
  type: object
- description: Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document.
  name: attachments
  type: array
- description: The creation date of the document.
  name: creationDate
  type: string
- description: Your description for the document.
  name: description
  type: string
- description: The expiry date of the document, in YYYY-MM-DD format.
  name: expiryDate
  type: string
- description: The filename of the document.
  name: fileName
  type: string
- description: The unique identifier of the document.
  name: id
  type: string
- description: The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**.
  name: issuerCountry
  type: string
- description: The state or province where the document was issued (AU only).
  name: issuerState
  type: string
- description: The modification date of the document.
  name: modificationDate
  type: string
- description: The number in the document.
  name: number
  type: string
- description: Contains information about the resource that owns the document.
  name: owner
  type: object
- description: Type of document, used when providing an ID number or uploading a document. The possible values depend on the legal entity type. * For **organization**, the `type` values can be **proofOfAddress**, **
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-document-schema.json
slug: legal-entity-document
tags:
- Payments
- Financial Services
- Fintech
title: Document
---
