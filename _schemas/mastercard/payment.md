---
description: A payment transaction processed through the Mastercard network, representing a transfer of funds between a payer and payee. Applicable across Mastercard Send, Account to Account Commerce, Bill Pay, and checkout solutions.
layout: schema
name: Mastercard Payment
properties_list:
- description: Unique identifier for the payment, generated using UUID logic to unambiguously link request and response messages.
  name: paymentId
  type: string
- description: Classification of the payment indicating its purpose and processing path.
  name: paymentType
  type: string
- description: Payment amount without decimal separators. The number of implied decimal places depends on the currency. For example, 10350 in USD represents $103.50.
  name: amount
  type: string
- description: ISO 4217 numeric currency code for the payment amount.
  name: currency
  type: string
- description: Current status of the payment in its lifecycle.
  name: status
  type: string
- description: Timestamp of the payment initiation in ISO 8601 format with timezone offset.
  name: timestamp
  type: string
- description: The party initiating or funding the payment.
  name: sender
  type: object
- description: The party receiving the payment funds.
  name: recipient
  type: object
- description: Primary Account Number (PAN) of the card used for the payment. Must pass Luhn algorithm validation.
  name: cardNumber
  type: string
- description: Payment token representing the card number for tokenized transactions (MDES).
  name: tokenNumber
  type: string
- description: Card acceptor or merchant unique identification number assigned by the acquirer.
  name: merchantId
  type: string
- description: Name of the card acceptor or merchant.
  name: merchantName
  type: string
- description: Four-digit ISO 18245 Merchant Category Code (MCC) classifying the type of business.
  name: merchantCategoryCode
  type: string
- description: Interbank Card Association (ICA) number of the acquiring institution.
  name: acquirerId
  type: string
- description: ICA number of the issuer or acquirer initiating the request.
  name: icaNumber
  type: string
- description: Authorization code returned by the issuer for an approved transaction.
  name: authorizationCode
  type: string
- description: Amount appearing on the cardholder statement in the billing currency, without decimals.
  name: billingAmount
  type: string
- description: ISO 4217 numeric currency code for the billing amount.
  name: billingCurrency
  type: string
- description: Currency conversion rate applied when the transaction and billing currencies differ.
  name: conversionRate
  type: string
- description: Payment network through which the transaction was processed.
  name: network
  type: string
- description: The channel through which the payment was initiated.
  name: channel
  type: string
- description: Point of service entry mode indicating how the card data was captured at the terminal.
  name: posEntryMode
  type: string
- description: Unique code identifying a terminal at the card acceptor location.
  name: terminalId
  type: string
- description: Date on which the transaction settles, in YYYYMMDD format.
  name: settlementDate
  type: string
- description: External reference identifier provided by the originator for reconciliation.
  name: referenceId
  type: string
- description: Brief description or comment provided by the originator supporting the payment.
  name: memo
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/payment.json
slug: payment
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Mastercard Payment
---
