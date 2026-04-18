---
description: Agreement Confirmation from DSP
layout: schema
name: AgreementConForPaymentAdvice
properties_list:
- description: Indicates true whether Agreement was confirmed by Debtor. False for any other reasons.
  name: agreementConfirmed
  type: boolean
- description: Reason for declined agreement. * Refer to Codes and Formats section for more details.
  name: agreementStatusReason
  type: string
- description: Nickname of the account is passed when agreementConfirmed is true.
  name: accountNickname
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-debtor-service-provider-resources-agreement-con-for-payment-advice-schema.json
slug: mastercard-debtor-service-provider-resources-agreement-con-for-payment-advice
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AgreementConForPaymentAdvice
---
