---
description: Available financing offer details for the requested purchase amount.
layout: schema
name: OfferContent
properties_list:
- description: Minimum purchase amount eligible for Affirm financing.
  name: minimum_loan_amount
  type: number
- description: Maximum purchase amount eligible for Affirm financing.
  name: maximum_loan_amount
  type: number
- description: Array of available financing term options for this amount.
  name: terms
  type: array
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/promos-offer-content-schema.json
slug: promos-offer-content
tags: []
title: OfferContent
---
