---
description: GrantOffer schema from Adyen API
layout: schema
name: GrantOffer
properties_list:
- description: The identifier of the account holder to which the grant is offered.
  name: accountHolderId
  type: string
- description: The principal amount of the grant.
  name: amount
  type: object
- description: 'The contract type of the grant offer. Possible value: **cashAdvance**, **loan**.'
  name: contractType
  type: string
- description: The end date of the grant offer validity period.
  name: expiresAt
  type: string
- description: Details of the fee configuration.
  name: fee
  type: object
- description: The unique identifier of the grant offer.
  name: id
  type: string
- description: Details of the repayment configuration.
  name: repayment
  type: object
- description: The starting date of the grant offer validity period.
  name: startsAt
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-grant-offer-schema.json
slug: configuration-grant-offer
tags:
- Payments
- Financial Services
- Fintech
title: GrantOffer
---
