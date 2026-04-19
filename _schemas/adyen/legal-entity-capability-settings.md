---
description: CapabilitySettings schema from Adyen API
layout: schema
name: CapabilitySettings
properties_list:
- description: The maximum amount a card holder can spend per industry.
  name: amountPerIndustry
  type: object
- description: The number of card holders who can use the card.
  name: authorizedCardUsers
  type: boolean
- description: The funding source of the card, for example **debit**.
  name: fundingSource
  type: array
- description: The period when the rule conditions apply.
  name: interval
  type: string
- description: The maximum amount a card holder can withdraw per day.
  name: maxAmount
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-capability-settings-schema.json
slug: legal-entity-capability-settings
tags:
- Payments
- Financial Services
- Fintech
title: CapabilitySettings
---
