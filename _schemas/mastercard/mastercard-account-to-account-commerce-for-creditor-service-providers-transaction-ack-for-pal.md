---
description: ''
layout: schema
name: TransactionAckForPAL
properties_list:
- description: Unique identifier assigned by Mastercard, to identify the payment request in subsequent transactions or services.
  name: paymentRequestLifecycleId
  type: string
- description: Unique 6 character reference provided by Mastercard to the CSP to be conveyed to the Debtor in order to make a payment. This value is only returned for payment request without agreement.
  name: paymentRequestReferenceNumber
  type: string
- description: Unique identifier assigned by Mastercard, to identify a particular payment (also referred to as settlement identifier) associated with a Payment Request.
  name: accountServicerReference
  type: string
- description: Time window given in seconds within which the Payment Confirmation must be received by the Creditor.
  name: confirmationExpiryTimeInterval
  type: number
- description: Reconciliation identifier assigned by Mastercard to the transaction.
  name: reconId
  type: string
- description: Status of the Payment Request returned by Mastercard. * Refer to Codes and Formats section for more details.
  name: paymentRequestStatus
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-transaction-ack-for-pal-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-transaction-ack-for-pal
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TransactionAckForPAL
---
