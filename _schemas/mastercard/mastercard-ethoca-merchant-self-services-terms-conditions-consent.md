---
description: ''
layout: schema
name: TermsConditionsConsent
properties_list:
- description: Date stamp in which the sub-merchant provided his consent on the terms and conditions. Date must be in [ISO 8601 format](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6)
  name: date
  type: string
- description: First name of person that gave consent
  name: firstName
  type: string
- description: Last name of person that gave consent
  name: lastName
  type: string
- description: Job title of person that gave consent
  name: jobTitle
  type: string
- description: Universally Unique Identifier (UUID) of the consent that the user consented to
  name: consentUuid
  type: string
- description: Version of the consent that the user consented to
  name: consentVersion
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-ethoca-merchant-self-services-terms-conditions-consent-schema.json
slug: mastercard-ethoca-merchant-self-services-terms-conditions-consent
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TermsConditionsConsent
---
