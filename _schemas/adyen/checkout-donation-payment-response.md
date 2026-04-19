---
description: DonationPaymentResponse schema from Adyen API
layout: schema
name: DonationPaymentResponse
properties_list:
- description: Authorised amount in the transaction.
  name: amount
  type: object
- description: The Adyen account name of your charity. We will provide you with this account name once your chosen charity has been [onboarded](https://docs.adyen.com/online-payments/donations#onboarding).
  name: donationAccount
  type: string
- description: Your unique resource identifier.
  name: id
  type: string
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: Action to be taken for completing the payment.
  name: payment
  type: object
- description: The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a require
  name: reference
  type: string
- description: 'The status of the donation transaction. Possible values: * **completed** * **pending** * **refused**'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-donation-payment-response-schema.json
slug: checkout-donation-payment-response
tags:
- Payments
- Financial Services
- Fintech
title: DonationPaymentResponse
---
