---
description: Product that is payable by the payment card. Product codes that are payable by the payment card.
layout: schema
name: AllowedProduct
properties_list:
- description: Product code of item purchased with the transaction.
  name: ProductCode
  type: integer
- description: Standard product code of item purchased with the transaction.
  name: EanUpc
  type: integer
- description: Product name of an item purchased with the transaction.
  name: ProductLabel
  type: string
- description: Additionl information related to the line item.
  name: AdditionalProductInfo
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-allowed-product-schema.json
slug: terminal-allowed-product
tags:
- Payments
- Financial Services
- Fintech
title: AllowedProduct
---
