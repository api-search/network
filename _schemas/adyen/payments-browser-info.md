---
description: BrowserInfo schema from Adyen API
layout: schema
name: BrowserInfo
properties_list:
- description: The accept header value of the shopper's browser.
  name: acceptHeader
  type: string
- description: 'The color depth of the shopper''s browser in bits per pixel. This should be obtained by using the browser''s `screen.colorDepth` property. Accepted values: 1, 4, 8, 15, 16, 24, 30, 32 or 48 bit color de'
  name: colorDepth
  type: integer
- description: Boolean value indicating if the shopper's browser is able to execute Java.
  name: javaEnabled
  type: boolean
- description: Boolean value indicating if the shopper's browser is able to execute JavaScript. A default 'true' value is assumed if the field is not present.
  name: javaScriptEnabled
  type: boolean
- description: The `navigator.language` value of the shopper's browser (as defined in IETF BCP 47).
  name: language
  type: string
- description: The total height of the shopper's device screen in pixels.
  name: screenHeight
  type: integer
- description: The total width of the shopper's device screen in pixels.
  name: screenWidth
  type: integer
- description: Time difference between UTC time and the shopper's browser local time, in minutes.
  name: timeZoneOffset
  type: integer
- description: The user agent value of the shopper's browser.
  name: userAgent
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-browser-info-schema.json
slug: payments-browser-info
tags:
- Payments
- Financial Services
- Fintech
title: BrowserInfo
---
