---
description: DocumentReference schema from Adyen API
layout: schema
name: DocumentReference
properties_list:
- description: Identifies whether the document is active and used for checks.
  name: active
  type: boolean
- description: Your description for the document.
  name: description
  type: string
- description: Document name.
  name: fileName
  type: string
- description: The unique identifier of the resource.
  name: id
  type: string
- description: The modification date of the document.
  name: modificationDate
  type: string
- description: List of document pages
  name: pages
  type: array
- description: Type of document, used when providing an ID number or uploading a document.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-document-reference-schema.json
slug: legal-entity-document-reference
tags:
- Payments
- Financial Services
- Fintech
title: DocumentReference
---
