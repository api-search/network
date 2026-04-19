---
description: CapabilityProblemEntity schema from Adyen API
layout: schema
name: CapabilityProblemEntity
properties_list:
- description: List of document IDs to which the verification errors related to the capabilities correspond to.
  name: documents
  type: array
- description: The ID of the entity.
  name: id
  type: string
- description: Contains details about the owner of the entity that has an error.
  name: owner
  type: object
- description: 'Type of entity. Possible values: **LegalEntity**, **BankAccount**, **Document**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-capability-problem-entity-schema.json
slug: configuration-capability-problem-entity
tags:
- Payments
- Financial Services
- Fintech
title: CapabilityProblemEntity
---
