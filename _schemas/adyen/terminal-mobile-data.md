---
description: Mobile phone is used as a payment instrument for the transaction. Information related to the mobile for the payment transaction.
layout: schema
name: MobileData
properties_list:
- description: If data available.
  name: MobileCountryCode
  type: integer
- description: If data available.
  name: MobileNetworkCode
  type: integer
- description: If data available.
  name: MaskedMSISDN
  type: integer
- description: ''
  name: Geolocation
  type: object
- description: SensitiveMobileData.
  name: ProtectedMobileData
  type: string
- description: ''
  name: SensitiveMobileData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-mobile-data-schema.json
slug: terminal-mobile-data
tags:
- Payments
- Financial Services
- Fintech
title: MobileData
---
