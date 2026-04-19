---
description: ''
layout: schema
name: ServiceProviderConfig
properties_list:
- description: ''
  name: schemas
  type: array
- description: An HTTP-addressable URL pointing to the service provider's human-consumable help documentation.
  name: documentationUri
  type: string
- description: A complex type that specifies PATCH configuration options.
  name: patch
  type: object
- description: A complex type that specifies bulk configuration options.
  name: bulk
  type: object
- description: A complex type that specifies FILTER options.
  name: filter
  type: object
- description: A complex type that specifies configuration options related to changing a password.
  name: changePassword
  type: object
- description: A complex type that specifies sort result options.
  name: sort
  type: object
- description: A complex type that specifies ETag configuration options.
  name: etag
  type: object
- description: A complex type that specifies supported authentication scheme properties.
  name: authenticationSchemes
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-procure-to-pay-scim-service-provider-config-schema.json
slug: factset-procure-to-pay-scim-service-provider-config
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: ServiceProviderConfig
---
