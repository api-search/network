---
description: ''
layout: schema
name: ProxyConfig
properties_list:
- description: ''
  name: check_host_against_uptime_tests
  type: boolean
- description: ''
  name: disable_strip_slash
  type: boolean
- description: ''
  name: enable_load_balancing
  type: boolean
- description: ''
  name: listen_path
  type: string
- description: ''
  name: preserve_host_header
  type: boolean
- description: ''
  name: strip_listen_path
  type: boolean
- description: ''
  name: target_list
  type: array
- description: ''
  name: target_url
  type: string
- description: ''
  name: transport
  type: object
provider_name: Tyk
provider_slug: tyk
schema_file: json-schema/tyk-gateway-proxy-config-schema.json
slug: tyk-gateway-proxy-config
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
title: ProxyConfig
---
