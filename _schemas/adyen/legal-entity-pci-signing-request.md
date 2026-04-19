---
description: PciSigningRequest schema from Adyen API
layout: schema
name: PciSigningRequest
properties_list:
- description: The array of Adyen-generated unique identifiers for the questionnaires.
  name: pciTemplateReferences
  type: array
- description: The [legal entity ID](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) of the individual who signs the PCI questionnaire.
  name: signedBy
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-pci-signing-request-schema.json
slug: legal-entity-pci-signing-request
tags:
- Payments
- Financial Services
- Fintech
title: PciSigningRequest
---
