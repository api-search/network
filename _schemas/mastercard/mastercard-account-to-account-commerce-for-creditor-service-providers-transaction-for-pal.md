---
description: ''
layout: schema
name: TransactionForPAL
properties_list:
- description: Unique identifier assigned by Creditor to identify Payment Request in their system.
  name: endToEndId
  type: string
- description: Unique identifier for the transaction assigned by the transaction initiator (CSP).
  name: instructionId
  type: string
- description: Set by the Creditor/CSP to define the settlement type of the Payment Request. * Refer to Codes and Formats section for more details.
  name: paymentRequestType
  type: string
- description: ISO 8601 format date and time in Coordinated Universal Time (UTC) the Payment Request was created.
  name: transactionCreationDateTime
  type: string
- description: The total amount of the payment request, as specified by the Creditor.
  name: instructedAmount
  type: string
- description: Set by Creditor/CSP to indicate the Payment Request type. * Refer to Codes and Formats section for more details.
  name: purpose
  type: string
- description: Set by the Creditor/CSP to offer specific transaction processing. * Refer to Codes and Formats section for more details.
  name: categoryPurpose
  type: string
- description: Set by the Creditor/CSP to communicate any restrictions to be verified by DSP before payment authorization. * Refer to Codes and Formats section for more details.
  name: restriction
  type: string
- description: Indicator to specify Credit account can be used for the payment.
  name: creditAccountAllowed
  type: boolean
- description: Indicates a request from Creditor to DSP to step-up authentication for the transaction.
  name: strongCustomerAuthentication
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-transaction-for-pal-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-transaction-for-pal
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TransactionForPAL
---
