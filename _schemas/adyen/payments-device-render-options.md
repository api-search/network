---
description: DeviceRenderOptions schema from Adyen API
layout: schema
name: DeviceRenderOptions
properties_list:
- description: 'Supported SDK interface types. Allowed values: * native * html * both'
  name: sdkInterface
  type: string
- description: 'UI types supported for displaying specific challenges. Allowed values: * text * singleSelect * outOfBand * otherHtml * multiSelect'
  name: sdkUiType
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-device-render-options-schema.json
slug: payments-device-render-options
tags:
- Payments
- Financial Services
- Fintech
title: DeviceRenderOptions
---
