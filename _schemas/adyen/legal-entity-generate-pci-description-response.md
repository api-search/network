---
description: GeneratePciDescriptionResponse schema from Adyen API
layout: schema
name: GeneratePciDescriptionResponse
properties_list:
- description: The generated questionnaires in a base64 encoded format.
  name: content
  type: string
- description: The two-letter [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code for the questionnaire. For example, **en**.
  name: language
  type: string
- description: The array of Adyen-generated unique identifiers for the questionnaires.
  name: pciTemplateReferences
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-generate-pci-description-response-schema.json
slug: legal-entity-generate-pci-description-response
tags:
- Payments
- Financial Services
- Fintech
title: GeneratePciDescriptionResponse
---
