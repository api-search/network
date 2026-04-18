---
description: ''
layout: schema
name: DSPDetails
properties_list:
- description: Unique identifier assigned to the DSP during Mastercard onboarding.
  name: debtorServiceProviderId
  type: string
- description: The DSP Short Name captured by Mastercard during onboarding.
  name: debtorServiceProviderName
  type: string
- description: DSP's Logo (in URL encoded format).
  name: debtorServiceProviderLogoUrl
  type: string
- description: DSP's universal link to where creditor can re-direct the consumer for authorization
  name: debtorServiceProviderUniversalLink
  type: string
- description: List of categoryPurposes supported by the DSP along with features supported for each categoryPurpose.
  name: categoryPurposeList
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-dsp-details-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-dsp-details
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DSPDetails
---
