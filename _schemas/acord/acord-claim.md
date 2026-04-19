---
description: JSON Schema for an ACORD NGDS insurance claim object, representing a first notice of loss through claim settlement.
layout: schema
name: ACORD Claim
properties_list:
- description: Unique internal claim identifier
  name: claimId
  type: string
- description: Carrier-assigned claim number
  name: claimNumber
  type: string
- description: Reference to the associated policy
  name: policyId
  type: string
- description: ''
  name: policyNumber
  type: string
- description: ''
  name: status
  type: string
- description: Date the loss or incident occurred
  name: lossDate
  type: string
- description: Date the claim was reported
  name: reportedDate
  type: string
- description: Narrative description of the loss
  name: lossDescription
  type: string
- description: Type of loss event
  name: lossType
  type: string
- description: ''
  name: lossLocation
  type: object
- description: ''
  name: claimant
  type: object
- description: ''
  name: adjuster
  type: object
- description: Current reserve amount set for this claim
  name: reserveAmount
  type: number
- description: Total amount paid on this claim to date
  name: paidAmount
  type: number
- description: ''
  name: currency
  type: string
- description: ''
  name: payments
  type: array
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
provider_name: ACORD
provider_slug: acord
schema_file: json-schema/acord-claim-schema.json
slug: acord-claim
tags:
- Claims
- Insurance
- Policy
- Standards
- Underwriting
title: ACORD Claim
---
