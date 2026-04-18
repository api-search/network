---
description: Configuration details for an Issuer.
layout: schema
name: IssuerConfiguration
properties_list:
- description: Comma separated account range must be between 4 and 8 supported by an Issuer.
  name: supportedAccountRange
  type: string
- description: Privacy Notice URL.
  name: privacyNoticeURL
  type: string
- description: Terms and conditions URL for the given user.
  name: termsAndConditionURL
  type: string
- description: Opt out URL for the given user.
  name: optOutURL
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-carbon-calculator-experience-issuer-configuration-schema.json
slug: mastercard-carbon-calculator-experience-issuer-configuration
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: IssuerConfiguration
---
