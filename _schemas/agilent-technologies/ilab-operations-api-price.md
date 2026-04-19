---
description: A pricing tier for a service.
layout: schema
name: Price
properties_list:
- description: Unique identifier for this price record.
  name: id
  type: integer
- description: Member type this price applies to (internal, external, collaborator).
  name: member_type
  type: string
- description: Price amount.
  name: amount
  type: number
- description: Currency code (ISO 4217).
  name: currency
  type: string
- description: Unit of measurement for the price.
  name: unit
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-price-schema.json
slug: ilab-operations-api-price
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Price
---
