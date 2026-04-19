---
description: FundRecipient schema from Adyen API
layout: schema
name: FundRecipient
properties_list:
- description: The address where to send the invoice.
  name: billingAddress
  type: object
- description: the used paymentMetohd
  name: paymentMethod
  type: object
- description: the email address of the person
  name: shopperEmail
  type: string
- description: the name of the person
  name: shopperName
  type: object
- description: 'Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identif'
  name: shopperReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: Required for Back-to-Back/ purchase driven load in Wallet transactions. Contains the final merchant who will be receiving the money, also known as subMerchant, information.
  name: subMerchant
  type: object
- description: the telephone number of the person
  name: telephoneNumber
  type: string
- description: indicates where the money is going
  name: walletIdentifier
  type: string
- description: indicates the tax identifier of the fund recepient
  name: walletOwnerTaxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-fund-recipient-schema.json
slug: checkout-fund-recipient
tags:
- Payments
- Financial Services
- Fintech
title: FundRecipient
---
