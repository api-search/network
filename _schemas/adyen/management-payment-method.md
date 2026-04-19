---
description: PaymentMethod schema from Adyen API
layout: schema
name: PaymentMethod
properties_list:
- description: Afterpay Touch details.
  name: afterpayTouch
  type: object
- description: Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your merchant account.
  name: allowed
  type: boolean
- description: Apple Pay details.
  name: applePay
  type: object
- description: Bancontact details.
  name: bcmc
  type: object
- description: The unique identifier of the business line. Required if you have a [platform setup](https://docs.adyen.com/marketplaces-and-platforms/platform-structure-resources/platform-setup/).
  name: businessLineId
  type: string
- description: Cartes Bancaires details.
  name: cartesBancaires
  type: object
- description: Clearpay details.
  name: clearpay
  type: object
- description: The list of countries where a payment method is available. By default, all countries supported by the payment method.
  name: countries
  type: array
- description: China Union Pay details.
  name: cup
  type: object
- description: The list of currencies that a payment method supports. By default, all currencies supported by the payment method.
  name: currencies
  type: array
- description: The list of custom routing flags to route payment to the intended acquirer.
  name: customRoutingFlags
  type: array
- description: Diners details.
  name: diners
  type: object
- description: Discover details.
  name: discover
  type: object
- description: Eftpos Australia details.
  name: eftpos_australia
  type: object
- description: Indicates whether the payment method is enabled (**true**) or disabled (**false**).
  name: enabled
  type: boolean
- description: giropay details.
  name: giroPay
  type: object
- description: Girocard details.
  name: girocard
  type: object
- description: Google Pay details.
  name: googlePay
  type: object
- description: The identifier of the resource.
  name: id
  type: string
- description: iDeal details.
  name: ideal
  type: object
- description: Interac Card details.
  name: interac_card
  type: object
- description: JCB details.
  name: jcb
  type: object
- description: Klarna details.
  name: klarna
  type: object
- description: Maestro details.
  name: maestro
  type: object
- description: MasterCard details.
  name: mc
  type: object
- description: Meal Voucher FR details.
  name: mealVoucher_FR
  type: object
- description: PayPal details.
  name: paypal
  type: object
- description: Your reference for the payment method. Supported characters a-z, A-Z, 0-9.
  name: reference
  type: string
- description: The sales channel.
  name: shopperInteraction
  type: string
- description: Sofort details.
  name: sofort
  type: object
- description: The unique identifier of the store for which to configure the payment method, if any.
  name: storeIds
  type: array
- description: Swish details.
  name: swish
  type: object
- description: Twint details.
  name: twint
  type: object
- description: Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).
  name: type
  type: string
- description: 'Payment method status. Possible values: * **valid** * **pending** * **invalid** * **rejected**'
  name: verificationStatus
  type: string
- description: Vipps details.
  name: vipps
  type: object
- description: Visa details.
  name: visa
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-payment-method-schema.json
slug: management-payment-method
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethod
---
