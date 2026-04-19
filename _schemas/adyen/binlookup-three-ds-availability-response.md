---
description: ThreeDSAvailabilityResponse schema from Adyen API
layout: schema
name: ThreeDSAvailabilityResponse
properties_list:
- description: Bin Group Details
  name: binDetails
  type: object
- description: List of Directory Server (DS) public keys.
  name: dsPublicKeys
  type: array
- description: Indicator if 3D Secure 1 is supported.
  name: threeDS1Supported
  type: boolean
- description: List of brand and card range pairs.
  name: threeDS2CardRangeDetails
  type: array
- description: Indicator if 3D Secure 2 is supported.
  name: threeDS2supported
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-three-ds-availability-response-schema.json
slug: binlookup-three-ds-availability-response
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDSAvailabilityResponse
---
