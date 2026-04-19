---
description: ThreeDS2CardRangeDetail schema from Adyen API
layout: schema
name: ThreeDS2CardRangeDetail
properties_list:
- description: 'Provides additional information to the 3DS Server. Possible values: - 01 (Authentication is available at ACS) - 02 (Attempts supported by ACS or DS) - 03 (Decoupled authentication supported) - 04 (Whi'
  name: acsInfoInd
  type: array
- description: Card brand.
  name: brandCode
  type: string
- description: BIN end range.
  name: endRange
  type: string
- description: BIN start range.
  name: startRange
  type: string
- description: Supported 3D Secure protocol versions
  name: threeDS2Versions
  type: array
- description: In a 3D Secure 2 browser-based flow, this is the URL where you should send the device fingerprint to.
  name: threeDSMethodURL
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-three-ds2-card-range-detail-schema.json
slug: binlookup-three-ds2-card-range-detail
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDS2CardRangeDetail
---
