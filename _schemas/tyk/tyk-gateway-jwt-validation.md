---
description: ''
layout: schema
name: JWTValidation
properties_list:
- description: ''
  name: enabled
  type: boolean
- description: ''
  name: expires_at_validation_skew
  type: integer
- description: ''
  name: identity_base_field
  type: string
- description: ''
  name: issued_at_validation_skew
  type: integer
- description: ''
  name: not_before_validation_skew
  type: integer
- description: ''
  name: signing_method
  type: string
- description: ''
  name: source
  type: string
provider_name: Tyk
provider_slug: tyk
schema_file: json-schema/tyk-gateway-jwt-validation-schema.json
slug: tyk-gateway-jwt-validation
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
title: JWTValidation
---
