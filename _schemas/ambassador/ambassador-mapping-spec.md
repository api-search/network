---
description: Specification for an Ambassador Mapping
layout: schema
name: MappingSpec
properties_list:
- description: Hostname to match for this Mapping. Use '*' to match all hostnames.
  name: hostname
  type: string
- description: URL prefix to match for routing
  name: prefix
  type: string
- description: Whether the prefix should be interpreted as a regular expression
  name: prefix_regex
  type: boolean
- description: Whether the prefix should be matched exactly rather than as a prefix
  name: prefix_exact
  type: boolean
- description: Target service to route to, in the format service-name.namespace:port or a full URL
  name: service
  type: string
- description: Prefix rewrite rule applied to the URL before forwarding to the backend service. Set to empty string to disable rewriting.
  name: rewrite
  type: string
- description: HTTP method to match
  name: method
  type: string
- description: Whether the method value is a regular expression
  name: method_regex
  type: boolean
- description: HTTP headers that must be present on the request for this Mapping to match. Values can be exact strings or regular expressions.
  name: headers
  type: object
- description: Query parameters that must be present for this Mapping to match
  name: query_parameters
  type: object
- description: Deprecated. Use hostname instead.
  name: host
  type: string
- description: Deprecated. Whether host is a regular expression.
  name: host_regex
  type: boolean
- description: Request timeout in milliseconds
  name: timeout_ms
  type: integer
- description: Idle timeout for streaming connections in milliseconds
  name: idle_timeout_ms
  type: integer
- description: Upstream connection timeout in milliseconds
  name: connect_timeout_ms
  type: integer
- description: Idle timeout for upstream connections in the cluster in milliseconds
  name: cluster_idle_timeout_ms
  type: integer
- description: Weight for traffic splitting when multiple Mappings match the same prefix. Used in canary deployments.
  name: weight
  type: integer
- description: Whether to bypass the external authentication service for this Mapping
  name: bypass_auth
  type: boolean
- description: Circuit breaker configurations for the upstream cluster
  name: circuit_breakers
  type: array
- description: Rate limiting labels to apply to requests matching this Mapping. Labels are sent to the rate limiting service for evaluation.
  name: labels
  type: object
- description: Headers to add to the request before forwarding to the upstream
  name: add_request_headers
  type: object
- description: Headers to add to the response before sending to the client
  name: add_response_headers
  type: object
- description: Header names to remove from the request
  name: remove_request_headers
  type: array
- description: Header names to remove from the response
  name: remove_response_headers
  type: array
- description: Protocols to allow upgrade to, such as websocket
  name: allow_upgrade
  type: array
- description: Whether the upstream service uses gRPC
  name: grpc
  type: boolean
- description: Whether to enable IPv4 DNS lookups for the upstream service
  name: enable_ipv4
  type: boolean
- description: Whether to enable IPv6 DNS lookups for the upstream service
  name: enable_ipv6
  type: boolean
- description: List of Ambassador IDs that should apply this Mapping. Used to partition a single Kubernetes cluster among multiple Ambassador instances.
  name: ambassador_id
  type: array
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-mapping-spec-schema.json
slug: ambassador-mapping-spec
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: MappingSpec
---
