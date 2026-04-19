---
description: OfflineProcessing schema from Adyen API
layout: schema
name: OfflineProcessing
properties_list:
- description: The maximum offline transaction amount for chip cards, in the processing currency and specified in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: chipFloorLimit
  type: integer
- description: The maximum offline transaction amount for swiped cards, in the specified currency.
  name: offlineSwipeLimits
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-offline-processing-schema.json
slug: management-offline-processing
tags:
- Payments
- Financial Services
- Fintech
title: OfflineProcessing
---
