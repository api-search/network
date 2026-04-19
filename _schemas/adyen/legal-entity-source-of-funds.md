---
description: SourceOfFunds schema from Adyen API
layout: schema
name: SourceOfFunds
properties_list:
- description: The unique identifier of the business line that will be the source of funds.This must be a business line for a **receivePayments** or **receiveFromPlatformPayments** capability.
  name: acquiringBusinessLineId
  type: string
- description: Indicates whether the funds are coming from transactions processed by Adyen. If **false**, a `description` is required.
  name: adyenProcessedFunds
  type: boolean
- description: Text describing the source of funds. For example, for `type` **business**, provide a description of where the business transactions come from, such as payments through bank transfer. Required when `ad
  name: description
  type: string
- description: 'The type of the source of funds. Possible value: **business**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-source-of-funds-schema.json
slug: legal-entity-source-of-funds
tags:
- Payments
- Financial Services
- Fintech
title: SourceOfFunds
---
