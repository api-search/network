---
description: MerchantRiskIndicator schema from Adyen API
layout: schema
name: MerchantRiskIndicator
properties_list:
- description: Whether the chosen delivery address is identical to the billing address.
  name: addressMatch
  type: boolean
- description: 'Indicator regarding the delivery address. Allowed values: * `shipToBillingAddress` * `shipToVerifiedAddress` * `shipToNewAddress` * `shipToStore` * `digitalGoods` * `goodsNotShipped` * `other`'
  name: deliveryAddressIndicator
  type: string
- description: The delivery email address (for digital goods).
  name: deliveryEmail
  type: string
- description: 'For Electronic delivery, the email address to which the merchandise was delivered. Maximum length: 254 characters.'
  name: deliveryEmailAddress
  type: string
- description: 'The estimated delivery time for the shopper to receive the goods. Allowed values: * `electronicDelivery` * `sameDayShipping` * `overnightShipping` * `twoOrMoreDaysShipping`'
  name: deliveryTimeframe
  type: string
- description: For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s).
  name: giftCardAmount
  type: object
- description: For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased.
  name: giftCardCount
  type: integer
- description: 'For prepaid or gift card purchase, [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) three-digit currency code of the gift card, other than those listed in Table A.5 of the EMVCo 3D Secure '
  name: giftCardCurr
  type: string
- description: For pre-order purchases, the expected date this product will be available to the shopper.
  name: preOrderDate
  type: string
- description: Indicator for whether this transaction is for pre-ordering a product.
  name: preOrderPurchase
  type: boolean
- description: Indicates whether Cardholder is placing an order for merchandise with a future availability or release date.
  name: preOrderPurchaseInd
  type: string
- description: Indicator for whether the shopper has already purchased the same items in the past.
  name: reorderItems
  type: boolean
- description: Indicates whether the cardholder is reordering previously purchased merchandise.
  name: reorderItemsInd
  type: string
- description: Indicates shipping method chosen for the transaction.
  name: shipIndicator
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-merchant-risk-indicator-schema.json
slug: checkout-merchant-risk-indicator
tags:
- Payments
- Financial Services
- Fintech
title: MerchantRiskIndicator
---
