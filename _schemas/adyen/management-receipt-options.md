---
description: ReceiptOptions schema from Adyen API
layout: schema
name: ReceiptOptions
properties_list:
- description: The receipt logo converted to a Base64-encoded string. The image must be a .bmp file of < 256 KB, dimensions 240 (H) x 384 (W) px.
  name: logo
  type: string
- description: Indicates whether a screen appears asking if you want to print the shopper receipt.
  name: promptBeforePrinting
  type: boolean
- description: 'Data to print on the receipt as a QR code. This can include static text and the following variables: - `${merchantreference}`: the merchant reference of the transaction. - `${pspreference}`: the PSP r'
  name: qrCodeData
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-receipt-options-schema.json
slug: management-receipt-options
tags:
- Payments
- Financial Services
- Fintech
title: ReceiptOptions
---
