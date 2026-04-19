---
description: Attachment schema from Adyen API
layout: schema
name: Attachment
properties_list:
- description: The document in Base64-encoded string format.
  name: content
  type: string
- description: 'The file format. Possible values: **application/pdf**, **image/jpg**, **image/jpeg**, **image/png**.'
  name: contentType
  type: string
- description: The name of the file including the file extension.
  name: filename
  type: string
- description: The name of the file including the file extension.
  name: pageName
  type: string
- description: Specifies which side of the ID card is uploaded. * When `type` is **driversLicense** or **identityCard**, set this to **front** or **back**. * When omitted, we infer the page number based on the order
  name: pageType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-attachment-schema.json
slug: legal-entity-attachment
tags:
- Payments
- Financial Services
- Fintech
title: Attachment
---
