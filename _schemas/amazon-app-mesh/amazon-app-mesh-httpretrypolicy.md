---
description: An object that represents a retry policy. Specify at least one value for at least one of the types of <code>RetryEvents</code>, a value for <code>maxRetries</code>, and a value for <code>perRetryTimeout</code>. Both <code>server-error</code> and <code>gateway-error</code> under <code>httpRetryEvents</code> include the Envoy <code>reset</code> policy. For more information on the <code>reset</code> policy, see the <a href="https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on">Envoy documentation</a>.
layout: schema
name: HttpRetryPolicy
properties_list:
- description: ''
  name: httpRetryEvents
  type: object
- description: ''
  name: maxRetries
  type: object
- description: ''
  name: perRetryTimeout
  type: object
- description: ''
  name: tcpRetryEvents
  type: object
provider_name: Amazon App Mesh
provider_slug: amazon-app-mesh
schema_file: json-schema/amazon-app-mesh-httpretrypolicy-schema.json
slug: amazon-app-mesh-httpretrypolicy
tags:
- AWS
- Microservices
- Networking
- Service Mesh
title: HttpRetryPolicy
---
