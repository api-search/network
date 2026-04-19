---
description: AcctInfo schema from Adyen API
layout: schema
name: AcctInfo
properties_list:
- description: 'Length of time that the cardholder has had the account with the 3DS Requestor. Allowed values: * **01** — No account * **02** — Created during this transaction * **03** — Less than 30 days * **04** — '
  name: chAccAgeInd
  type: string
- description: 'Date that the cardholder’s account with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added. Format: **YYYYMMDD**'
  name: chAccChange
  type: string
- description: 'Length of time since the cardholder’s account information with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added. Allowed values: * *'
  name: chAccChangeInd
  type: string
- description: 'Date that cardholder’s account with the 3DS Requestor had a password change or account reset. Format: **YYYYMMDD**'
  name: chAccPwChange
  type: string
- description: 'Indicates the length of time since the cardholder’s account with the 3DS Requestor had a password change or account reset. Allowed values: * **01** — No change * **02** — Changed during this transacti'
  name: chAccPwChangeInd
  type: string
- description: 'Date that the cardholder opened the account with the 3DS Requestor. Format: **YYYYMMDD**'
  name: chAccString
  type: string
- description: 'Number of purchases with this cardholder account during the previous six months. Max length: 4 characters.'
  name: nbPurchaseAccount
  type: string
- description: 'String that the payment account was enrolled in the cardholder’s account with the 3DS Requestor. Format: **YYYYMMDD**'
  name: paymentAccAge
  type: string
- description: 'Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS Requestor. Allowed values: * **01** — No account (guest checkout) * **02** — During this tra'
  name: paymentAccInd
  type: string
- description: 'Number of Add Card attempts in the last 24 hours. Max length: 3 characters.'
  name: provisionAttemptsDay
  type: string
- description: 'String when the shipping address used for this transaction was first used with the 3DS Requestor. Format: **YYYYMMDD**'
  name: shipAddressUsage
  type: string
- description: 'Indicates when the shipping address used for this transaction was first used with the 3DS Requestor. Allowed values: * **01** — This transaction * **02** — Less than 30 days * **03** — 30–60 days * **'
  name: shipAddressUsageInd
  type: string
- description: 'Indicates if the Cardholder Name on the account is identical to the shipping Name used for this transaction. Allowed values: * **01** — Account Name identical to shipping Name * **02** — Account Name '
  name: shipNameIndicator
  type: string
- description: 'Indicates whether the 3DS Requestor has experienced suspicious activity (including previous fraud) on the cardholder account. Allowed values: * **01** — No suspicious activity has been observed * **02'
  name: suspiciousAccActivity
  type: string
- description: 'Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous 24 hours. Max length: 3 characters.'
  name: txnActivityDay
  type: string
- description: 'Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous year. Max length: 3 characters.'
  name: txnActivityYear
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-acct-info-schema.json
slug: payments-acct-info
tags:
- Payments
- Financial Services
- Fintech
title: AcctInfo
---
