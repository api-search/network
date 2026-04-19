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
- description: The owner of the entity that has an error. For example, if the `entity.type` is **BankAccount**, then the `owner` contains the details of the legal entity that owns the bank account.
  name: owner
  type: object
- description: 'The type of entity. Possible values: **LegalEntity**, **BankAccount**, or **Document**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhooks-capability-problem-entity-schema.json
slug: management-webhooks-capability-problem-entity
tags:
- Payments
- Financial Services
- Fintech
title: CapabilityProblemEntity
---
