---
description: ''
layout: schema
name: CreditorForAgreementCreation
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
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-creditor-for-agreement-creation-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-creditor-for-agreement-creation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CreditorForAgreementCreation
---
