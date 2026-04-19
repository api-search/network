---
description: CancelOrRefundRequest schema from Adyen API
layout: schema
name: CancelOrRefundRequest
properties_list:
- description: This field contains additional data, which may be required for a particular modification request. The additionalData object consists of entries, each of which includes the key and value.
  name: additionalData
  type: object
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires).
  name: mpiData
  type: object
- description: The original merchant reference to cancel.
  name: originalMerchantReference
  type: string
- description: 'The original pspReference of the payment to modify. This reference is returned in: * authorisation response * authorisation notification'
  name: originalReference
  type: string
- description: Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#chargebacks-and-disputes).
  name: platformChargebackLogic
  type: object
- description: 'Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters.'
  name: reference
  type: string
- description: The transaction reference provided by the PED. For point-of-sale integrations only.
  name: tenderReference
  type: string
- description: Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only.
  name: uniqueTerminalId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-cancel-or-refund-request-schema.json
slug: payments-cancel-or-refund-request
tags:
- Payments
- Financial Services
- Fintech
title: CancelOrRefundRequest
---
