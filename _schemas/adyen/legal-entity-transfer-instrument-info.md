---
description: TransferInstrumentInfo schema from Adyen API
layout: schema
name: TransferInstrumentInfo
properties_list:
- description: Contains information about the legal entity's bank account.
  name: bankAccount
  type: object
- description: The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument.
  name: legalEntityId
  type: string
- description: 'The type of transfer instrument. Possible value: **bankAccount**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-transfer-instrument-info-schema.json
slug: legal-entity-transfer-instrument-info
tags:
- Payments
- Financial Services
- Fintech
title: TransferInstrumentInfo
---
