---
description: GeneratePciDescriptionRequest schema from Adyen API
layout: schema
name: GeneratePciDescriptionRequest
properties_list:
- description: An array of additional sales channels to generate PCI questionnaires. Include the relevant sales channels if you need your user to sign PCI questionnaires. Not required if you [create stores](https://
  name: additionalSalesChannels
  type: array
- description: Sets the language of the PCI questionnaire. Its value is a two-character [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code, for example, **en**.
  name: language
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-generate-pci-description-request-schema.json
slug: legal-entity-generate-pci-description-request
tags:
- Payments
- Financial Services
- Fintech
title: GeneratePciDescriptionRequest
---
