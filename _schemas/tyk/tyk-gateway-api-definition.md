---
description: ''
layout: schema
name: APIDefinition
properties_list:
- description: ''
  name: active
  type: boolean
- description: ''
  name: allowed_ips
  type: array
- description: ''
  name: api_id
  type: string
- description: ''
  name: auth_configs
  type: object
- description: ''
  name: base_identity_provided_by
  type: string
- description: ''
  name: basic_auth
  type: object
- description: ''
  name: blacklisted_ips
  type: array
- description: ''
  name: certificate_pinning_disabled
  type: boolean
- description: ''
  name: certificates
  type: array
- description: ''
  name: client_certificates
  type: array
- description: ''
  name: config_data
  type: object
- description: ''
  name: config_data_disabled
  type: boolean
- description: ''
  name: custom_middleware_bundle
  type: string
- description: ''
  name: custom_middleware_bundle_disabled
  type: boolean
- description: ''
  name: custom_plugin_auth_enabled
  type: boolean
- description: ''
  name: detailed_tracing
  type: boolean
- description: ''
  name: disable_quota
  type: boolean
- description: ''
  name: disable_rate_limit
  type: boolean
- description: ''
  name: do_not_track
  type: boolean
- description: ''
  name: domain
  type: string
- description: ''
  name: domain_disabled
  type: boolean
- description: ''
  name: dont_set_quota_on_create
  type: boolean
- description: ''
  name: enable_batch_request_support
  type: boolean
- description: ''
  name: enable_context_vars
  type: boolean
- description: ''
  name: enable_coprocess_auth
  type: boolean
- description: ''
  name: enable_detailed_recording
  type: boolean
- description: ''
  name: enable_ip_blacklisting
  type: boolean
- description: ''
  name: enable_ip_whitelisting
  type: boolean
- description: ''
  name: enable_jwt
  type: boolean
- description: ''
  name: enable_proxy_protocol
  type: boolean
- description: ''
  name: enable_signature_checking
  type: boolean
- description: ''
  name: expiration
  type: string
- description: ''
  name: expire_analytics_after
  type: integer
- description: ''
  name: hmac_allowed_algorithms
  type: array
- description: ''
  name: hmac_allowed_clock_skew
  type: number
- description: ''
  name: id
  type: string
- description: ''
  name: idp_client_id_mapping_disabled
  type: boolean
- description: ''
  name: internal
  type: boolean
- description: ''
  name: is_oas
  type: boolean
- description: ''
  name: jwt_client_base_field
  type: string
- description: ''
  name: jwt_default_policies
  type: array
- description: ''
  name: jwt_expires_at_validation_skew
  type: integer
- description: ''
  name: jwt_identity_base_field
  type: string
- description: ''
  name: jwt_issued_at_validation_skew
  type: integer
- description: ''
  name: jwt_not_before_validation_skew
  type: integer
- description: ''
  name: jwt_policy_field_name
  type: string
- description: ''
  name: jwt_scope_claim_name
  type: string
- description: ''
  name: jwt_scope_to_policy_mapping
  type: object
- description: ''
  name: jwt_signing_method
  type: string
- description: ''
  name: jwt_skip_kid
  type: boolean
- description: ''
  name: jwt_source
  type: string
- description: ''
  name: listen_port
  type: integer
- description: ''
  name: name
  type: string
- description: ''
  name: oauth_meta
  type: object
- description: ''
  name: org_id
  type: string
- description: ''
  name: pinned_public_keys
  type: object
- description: ''
  name: protocol
  type: string
- description: ''
  name: response_processors
  type: array
- description: ''
  name: session_lifetime
  type: integer
- description: ''
  name: session_lifetime_respects_key_expiration
  type: boolean
- description: ''
  name: slug
  type: string
- description: ''
  name: strip_auth_data
  type: boolean
- description: ''
  name: tag_headers
  type: array
- description: ''
  name: tags
  type: array
- description: ''
  name: tags_disabled
  type: boolean
- description: ''
  name: upstream_certificates
  type: object
- description: ''
  name: upstream_certificates_disabled
  type: boolean
- description: ''
  name: use_basic_auth
  type: boolean
- description: ''
  name: use_go_plugin_auth
  type: boolean
- description: ''
  name: use_keyless
  type: boolean
- description: ''
  name: use_mutual_tls_auth
  type: boolean
- description: ''
  name: use_oauth2
  type: boolean
- description: ''
  name: use_openid
  type: boolean
- description: ''
  name: use_standard_auth
  type: boolean
provider_name: Tyk
provider_slug: tyk
schema_file: json-schema/tyk-gateway-api-definition-schema.json
slug: tyk-gateway-api-definition
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
title: APIDefinition
---
