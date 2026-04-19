---
description: ApplicationInfo schema from Adyen API
layout: schema
name: ApplicationInfo
properties_list:
- description: Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc.
  name: adyenLibrary
  type: object
- description: Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc.
  name: adyenPaymentSource
  type: object
- description: Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc.
  name: externalPlatform
  type: object
- description: Merchant developed software, such as cashier application, used to interact with the Adyen API.
  name: merchantApplication
  type: object
- description: Merchant device information.
  name: merchantDevice
  type: object
- description: Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests.
  name: shopperInteractionDevice
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-application-info-schema.json
slug: checkout-application-info
tags:
- Payments
- Financial Services
- Fintech
title: ApplicationInfo
---
