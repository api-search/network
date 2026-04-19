---
description: CapabilityProblemEntity-recursive schema from Adyen API
layout: schema
name: CapabilityProblemEntity-recursive
properties_list:
- description: List of document IDs to which the verification errors related to the capabilities correspond to.
  name: documents
  type: array
- description: The ID of the entity.
  name: id
  type: string
- description: 'Type of entity. Possible values: **LegalEntity**, **BankAccount**, **Document**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-capability-problem-entity-recursive-schema.json
slug: configuration-webhooks-capability-problem-entity-recursive
tags:
- Payments
- Financial Services
- Fintech
title: CapabilityProblemEntity-recursive
---
