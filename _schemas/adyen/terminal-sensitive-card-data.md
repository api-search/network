---
description: This data structure could be CMS protected (EnvelopedData). In this case the data structure SensitiveCardData is replaced by the data structure ProtectedCardData of type ContentInformationType. When this data is protected, the exact content is unknown by the Sale System, and might include all the information which are required by an external backup POI Server to make a batch payment transaction in case of problem with the POI System. Sensitive information related to the payment card, entered or read by the Sale System.
layout: schema
name: SensitiveCardData
properties_list:
- description: ''
  name: PAN
  type: integer
- description: if EntryMode is File, Keyed or Manual.
  name: CardSeqNumb
  type: integer
- description: if EntryMode is File.
  name: ExpiryDate
  type: integer
- description: ''
  name: TrackData
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-sensitive-card-data-schema.json
slug: terminal-sensitive-card-data
tags:
- Payments
- Financial Services
- Fintech
title: SensitiveCardData
---
