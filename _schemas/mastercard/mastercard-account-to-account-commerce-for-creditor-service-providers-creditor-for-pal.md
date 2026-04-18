---
description: ''
layout: schema
name: CreditorForPAL
properties_list:
- description: Unique identifier assigned to the Creditor by the CSP.
  name: creditorId
  type: string
- description: Unique identifier assigned to the CSP during Mastercard onboarding.
  name: creditorServiceProviderId
  type: string
- description: Return string (in URL encoded format) that is passed to the DSP to return the Debtor back to the Creditor's checkout page.
  name: creditorReturnString
  type: string
- description: Unique identifier assigned by the CSP of the ultimateCreditor to which the Payment is requested. When this value is populated, ultimateCreditor's Trade name is returned in creditorTradeName to DSP, wh
  name: ultimateCreditorId
  type: string
- description: Creditor's Account Information. Either the IBAN or account number should be used. This is provided only for Me-to-Me payments.
  name: creditorAccount
  type: object
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-creditor-for-pal-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-creditor-for-pal
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CreditorForPAL
---
