---
description: OwnerEntity schema from Adyen API
layout: schema
name: OwnerEntity
properties_list:
- description: Unique identifier of the resource that owns the document. For `type` **legalEntity**, this value is the unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/p
  name: id
  type: string
- description: 'Type of resource that owns the document. Possible values: **legalEntity**, **bankAccount**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-owner-entity-schema.json
slug: legal-entity-owner-entity
tags:
- Payments
- Financial Services
- Fintech
title: OwnerEntity
---
