---
description: ''
layout: schema
name: TransactionForPaymentRetrieval
properties_list:
- description: Unique identifier assigned by Mastercard, to identify the payment request in subsequent transactions or services.
  name: paymentRequestLifecycleId
  type: string
- description: Unique identifier of the Debtor provided to Mastercard by the DSP.
  name: debtorId
  type: string
- description: Unique identifier assigned to the DSP during Mastercard onboarding.
  name: debtorServiceProviderId
  type: string
- description: Set by DSP to specify Payment Request retrieval initiation method. * Refer to Codes and Formats section for more details.
  name: retrieveInitMethod
  type: string
- description: Unique 6 character reference provided by Mastercard to the CSP to be conveyed to the Debtor to make a payment.
  name: paymentRequestReferenceNumber
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-debtor-service-provider-resources-transaction-for-payment-retrieval-schema.json
slug: mastercard-debtor-service-provider-resources-transaction-for-payment-retrieval
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TransactionForPaymentRetrieval
---
