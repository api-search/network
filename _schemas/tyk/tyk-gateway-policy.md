---
description: ''
layout: schema
name: Policy
properties_list:
- description: ''
  name: _id
  type: string
- description: ''
  name: access_rights
  type: object
- description: ''
  name: active
  type: boolean
- description: ''
  name: enable_http_signature_validation
  type: boolean
- description: ''
  name: graphql_access_rights
  type: object
- description: ''
  name: hmac_enabled
  type: boolean
- description: ''
  name: id
  type: string
- description: ''
  name: is_inactive
  type: boolean
- description: ''
  name: key_expires_in
  type: integer
- description: ''
  name: last_updated
  type: string
- description: ''
  name: max_query_depth
  type: integer
- description: ''
  name: meta_data
  type: object
- description: ''
  name: name
  type: string
- description: ''
  name: org_id
  type: string
- description: ''
  name: per
  type: number
- description: ''
  name: quota_max
  type: integer
- description: ''
  name: quota_renewal_rate
  type: integer
- description: ''
  name: rate
  type: number
- description: ''
  name: tags
  type: array
- description: ''
  name: throttle_interval
  type: number
- description: ''
  name: throttle_retry_limit
  type: integer
provider_name: Tyk
provider_slug: tyk
schema_file: json-schema/tyk-gateway-policy-schema.json
slug: tyk-gateway-policy
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
title: Policy
---
