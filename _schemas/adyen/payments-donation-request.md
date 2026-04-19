---
description: DonationRequest schema from Adyen API
layout: schema
name: DonationRequest
properties_list:
- description: The Adyen account name of the charity.
  name: donationAccount
  type: string
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The amount to be donated.The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount.
  name: modificationAmount
  type: object
- description: 'The original pspReference of the payment to modify. This reference is returned in: * authorisation response * authorisation notification'
  name: originalReference
  type: string
- description: Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#chargebacks-and-disputes).
  name: platformChargebackLogic
  type: object
- description: 'Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters.'
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-donation-request-schema.json
slug: payments-donation-request
tags:
- Payments
- Financial Services
- Fintech
title: DonationRequest
---
