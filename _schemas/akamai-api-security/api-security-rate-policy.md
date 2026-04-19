---
description: Contains details about a rate policy.
layout: schema
name: rate-policy
properties_list:
- description: The list of additional match conditions.
  name: additionalMatchOptions
  type: array
- description: The API endpoints to match in incoming requests. This only applies to the `api` `matchType`.
  name: apiSelectors
  type: array
- description: The allowed hits per second during any two-minute interval.
  name: averageThreshold
  type: integer
- description: The list of body parameters to match on.
  name: bodyParameters
  type: array
- description: The allowed hits per second during any five-second interval.
  name: burstThreshold
  type: integer
- description: The time span for the `burstThreshold` interval. For existing rate policies, analyze your traffic in Alert mode before you reduce the measure window from 5 seconds. [Learn more about thresholds here](
  name: burstWindow
  type: integer
- description: The client identifier you want to use to identify and track request senders. The value is required only for WAF type, and `api-key` is supported only for API match criteria. Using `ip-useragent` is ty
  name: clientIdentifier
  type: string
- description: Contains information about the criteria that trigger the rate policy.
  name: condition
  type: object
- description: The rate policy counter type. Either `per_edge` for rate limiting to work per edge node, or `region_aggregated` for rate limiting to work using aggregated rate accounting across multiple edge nodes.
  name: counterType
  type: string
- description: __Read-only__ The time stamp when you created the rate policy.
  name: createDate
  type: string
- description: Descriptive text you provide about a policy.
  name: description
  type: string
- description: Contains details about rate policy evaluation.
  name: evaluation
  type: object
- description: Contains the file extension match criteria.
  name: fileExtensions
  type: object
- description: __Deprecated__. The hostnames to match. This array member is deprecated. Use the `hosts` object instead.
  name: hostnames
  type: array
- description: The hostnames to match, and whether to trigger on a match or absence of match.
  name: hosts
  type: object
- description: __Read-only__ Uniquely identifies each rate policy.
  name: id
  type: integer
- description: The match type in a rate policy. Either `path` to match website paths or `api` to match API paths.
  name: matchType
  type: string
- description: The name you assign to a rate policy.
  name: name
  type: string
- description: Contains details about the path match criteria.
  name: path
  type: object
- description: 'The type of paths to match in incoming requests. Either `AllRequests` to match an empty path or any path that ends in a trailing slash (`/`), `TopLevel` to match top-level hostnames only, or `Custom` '
  name: pathMatchType
  type: string
- description: Whether the condition should trigger on a match (`true`) or a lack of match (`false`).
  name: pathUriPositiveMatch
  type: boolean
- description: The list of query parameter objects to match on.
  name: queryParameters
  type: array
- description: The type of requests to count towards the rate policy's thresholds. Either `ClientRequest` to count client requests to edge servers, `ClientResponse` to count edge responses to the client, `ForwardRes
  name: requestType
  type: string
- description: Whether to apply the same action to the IPv6 traffic as to the IPv4 traffic.
  name: sameActionOnIpv6
  type: boolean
- description: The rate policy type. Either `WAF` for Web Application Firewall, or `BOTMAN` for Bot Manager.
  name: type
  type: string
- description: __Read-only__ The ISO 8601 timestamp when you last updated the rate policy.
  name: updateDate
  type: string
- description: Whether to check the contents of the `X-Forwarded-For` header in incoming requests.
  name: useXForwardForHeaders
  type: boolean
- description: __Read-only__ Whether you're currently using the rate policy.
  name: used
  type: boolean
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-rate-policy-schema.json
slug: api-security-rate-policy
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: rate-policy
---
