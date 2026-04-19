---
description: ShopperInput schema from Adyen API
layout: schema
name: ShopperInput
properties_list:
- description: 'Specifies visibility of billing address fields. Permitted values: * editable * hidden * readOnly'
  name: billingAddress
  type: string
- description: 'Specifies visibility of delivery address fields. Permitted values: * editable * hidden * readOnly'
  name: deliveryAddress
  type: string
- description: 'Specifies visibility of personal details. Permitted values: * editable * hidden * readOnly'
  name: personalDetails
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-shopper-input-schema.json
slug: checkout-shopper-input
tags:
- Payments
- Financial Services
- Fintech
title: ShopperInput
---
