---
description: PciSigningResponse schema from Adyen API
layout: schema
name: PciSigningResponse
properties_list:
- description: The unique identifiers of the signed PCI documents.
  name: pciQuestionnaireIds
  type: array
- description: The [legal entity ID](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) of the individual who signed the PCI questionnaire.
  name: signedBy
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-pci-signing-response-schema.json
slug: legal-entity-pci-signing-response
tags:
- Payments
- Financial Services
- Fintech
title: PciSigningResponse
---
