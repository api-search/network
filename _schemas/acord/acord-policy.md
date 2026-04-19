---
description: JSON Schema for an ACORD NGDS insurance policy object, representing an insurance contract with coverages and insured party.
layout: schema
name: ACORD Policy
properties_list:
- description: Unique internal policy identifier
  name: policyId
  type: string
- description: Carrier-assigned policy number
  name: policyNumber
  type: string
- description: Insurance line of business
  name: lineOfBusiness
  type: string
- description: Current policy status
  name: status
  type: string
- description: Policy effective date
  name: effectiveDate
  type: string
- description: Policy expiration date
  name: expirationDate
  type: string
- description: Total policy premium amount
  name: premiumAmount
  type: number
- description: ISO 4217 currency code
  name: currency
  type: string
- description: ''
  name: insuredParty
  type: object
- description: List of coverages under the policy
  name: coverages
  type: array
- description: Policy endorsements and amendments
  name: endorsements
  type: array
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
provider_name: ACORD
provider_slug: acord
schema_file: json-schema/acord-policy-schema.json
slug: acord-policy
tags:
- Claims
- Insurance
- Policy
- Standards
- Underwriting
title: ACORD Policy
---
