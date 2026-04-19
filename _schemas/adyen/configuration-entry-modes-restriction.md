---
description: EntryModesRestriction schema from Adyen API
layout: schema
name: EntryModesRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: 'List of point-of-sale entry modes. Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**.'
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-entry-modes-restriction-schema.json
slug: configuration-entry-modes-restriction
tags:
- Payments
- Financial Services
- Fintech
title: EntryModesRestriction
---
