---
description: PciDocumentInfo schema from Adyen API
layout: schema
name: PciDocumentInfo
properties_list:
- description: The date the questionnaire was created, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00
  name: createdAt
  type: string
- description: The unique identifier of the signed questionnaire.
  name: id
  type: string
- description: The expiration date of the questionnaire, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00
  name: validUntil
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-pci-document-info-schema.json
slug: legal-entity-pci-document-info
tags:
- Payments
- Financial Services
- Fintech
title: PciDocumentInfo
---
