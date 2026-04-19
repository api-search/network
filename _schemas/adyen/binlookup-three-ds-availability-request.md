---
description: ThreeDSAvailabilityRequest schema from Adyen API
layout: schema
name: ThreeDSAvailabilityRequest
properties_list:
- description: This field contains additional data, which may be required for a particular request. The `additionalData` object consists of entries, each of which includes the key and value.
  name: additionalData
  type: object
- description: List of brands.
  name: brands
  type: array
- description: Card number or BIN.
  name: cardNumber
  type: string
- description: The merchant account identifier.
  name: merchantAccount
  type: string
- description: A recurring detail reference corresponding to a card.
  name: recurringDetailReference
  type: string
- description: The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID).
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-three-ds-availability-request-schema.json
slug: binlookup-three-ds-availability-request
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDSAvailabilityRequest
---
