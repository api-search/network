---
description: ''
layout: schema
name: termsAndConditionsRequest
properties_list:
- description: List of Fixed Income Security identifiers. Supported symbol types include CUSIP, SEDOL, ISIN, and FactSet Security Permanent Identifier (-S). **ID LIMIT = 250** *per request*.
  name: ids
  type: array
- description: List of Terms and Conditions data items.
  name: fields
  type: array
- description: Selects the Fixed Income metrics by major category - * **SECURITY_DETAILS** = Detailed information about the security. * **COUPON_DETAILS** = Coupon details. * **CONVERTIBLE_FEATURES** = Features of c
  name: categories
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-terms-and-conditions-request-schema.json
slug: factset-terms-and-conditions-terms-and-conditions-request
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: termsAndConditionsRequest
---
