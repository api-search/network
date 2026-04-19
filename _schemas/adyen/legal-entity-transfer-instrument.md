---
description: TransferInstrument schema from Adyen API
layout: schema
name: TransferInstrument
properties_list:
- description: Contains information about the legal entity's bank account.
  name: bankAccount
  type: object
- description: List of capabilities for this transfer instrument.
  name: capabilities
  type: object
- description: List of documents uploaded for the transfer instrument.
  name: documentDetails
  type: array
- description: The unique identifier of the transfer instrument.
  name: id
  type: string
- description: The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument.
  name: legalEntityId
  type: string
- description: The verification errors related to capabilities for this transfer instrument.
  name: problems
  type: array
- description: 'The type of transfer instrument. Possible value: **bankAccount**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-transfer-instrument-schema.json
slug: legal-entity-transfer-instrument
tags:
- Payments
- Financial Services
- Fintech
title: TransferInstrument
---
