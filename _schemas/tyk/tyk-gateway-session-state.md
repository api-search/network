---
description: ''
layout: schema
name: SessionState
properties_list:
- description: ''
  name: access_rights
  type: object
- description: ''
  name: alias
  type: string
- description: ''
  name: allowance
  type: number
- description: ''
  name: apply_policies
  type: array
- description: deprecated use apply_policies going forward instead to send a list of policies ids
  name: apply_policy_id
  type: string
- description: ''
  name: certificate
  type: string
- description: ''
  name: data_expires
  type: integer
- description: ''
  name: date_created
  type: string
- description: deprecated use enable_detailed_recording going forward instead
  name: enable_detail_recording
  type: boolean
- description: ''
  name: enable_detailed_recording
  type: boolean
- description: ''
  name: enable_http_signature_validation
  type: boolean
- description: ''
  name: expires
  type: integer
- description: ''
  name: hmac_enabled
  type: boolean
- description: ''
  name: hmac_string
  type: string
- description: ''
  name: id_extractor_deadline
  type: integer
- description: ''
  name: is_inactive
  type: boolean
- description: ''
  name: last_check
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
  name: oauth_client_id
  type: string
- description: ''
  name: oauth_keys
  type: object
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
  name: quota_remaining
  type: integer
- description: ''
  name: quota_renewal_rate
  type: integer
- description: ''
  name: quota_renews
  type: integer
- description: ''
  name: rate
  type: number
- description: ''
  name: rsa_certificate_id
  type: string
- description: ''
  name: session_lifetime
  type: integer
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
schema_file: json-schema/tyk-gateway-session-state-schema.json
slug: tyk-gateway-session-state
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
title: SessionState
---
