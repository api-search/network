---
description: CardDetails schema from Adyen API
layout: schema
name: CardDetails
properties_list:
- description: 'Secondary brand of the card. For example: **plastix**, **hmclub**.'
  name: brand
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: ''
  name: cupsecureplus.smscode
  type: string
- description: The card verification code. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide).
  name: cvc
  type: string
- description: The encrypted card number.
  name: encryptedCardNumber
  type: string
- description: The encrypted card expiry month.
  name: encryptedExpiryMonth
  type: string
- description: The encrypted card expiry year.
  name: encryptedExpiryYear
  type: string
- description: The encrypted card verification code.
  name: encryptedSecurityCode
  type: string
- description: The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide).
  name: expiryMonth
  type: string
- description: The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide).
  name: expiryYear
  type: string
- description: The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.
  name: fundingSource
  type: string
- description: The name of the card holder.
  name: holderName
  type: string
- description: The network token reference. This is the [`networkTxReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-network
  name: networkPaymentReference
  type: string
- description: The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide).
  name: number
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: The `shopperNotificationReference` returned in the response when you requested to notify the shopper. Used only for recurring payments in India.
  name: shopperNotificationReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.
  name: threeDS2SdkVersion
  type: string
- description: Default payment method details. Common for scheme payment methods, and for simple payment method details.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-card-details-schema.json
slug: checkout-card-details
tags:
- Payments
- Financial Services
- Fintech
title: CardDetails
---
