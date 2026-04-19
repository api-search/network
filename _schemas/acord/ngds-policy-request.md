---
description: PolicyRequest schema from ACORD NGDS API
layout: schema
name: PolicyRequest
properties_list:
- description: ''
  name: lineOfBusiness
  type: string
- description: ''
  name: effectiveDate
  type: string
- description: ''
  name: expirationDate
  type: string
- description: ''
  name: premiumAmount
  type: number
- description: ''
  name: currency
  type: string
- description: ''
  name: insuredParty
  type: object
- description: ''
  name: coverages
  type: array
provider_name: ACORD
provider_slug: acord
schema_file: json-schema/ngds-policy-request-schema.json
slug: ngds-policy-request
tags:
- Claims
- Insurance
- Policy
- Standards
- Underwriting
title: PolicyRequest
---
