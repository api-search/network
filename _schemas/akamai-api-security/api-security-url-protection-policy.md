---
description: Contains details about a URL protection policy.
layout: schema
name: url-protection-policy
properties_list:
- description: The API endpoints to match on in incoming requests. This only applies to the `api` `matchType`.
  name: apiDefinitions
  type: array
- description: Exempts specific clients from being processed by the URL protection policy.
  name: bypassCondition
  type: object
- description: The traffic categories to perform load shedding on when the origin traffic rate exceeds the load shedding threshold. If `intelligentLoadShedding` is set to `true`, specify one or more categories.
  name: categories
  type: array
- description: Uniquely identifies the security configuration.
  name: configId
  type: integer
- description: The security configuration version.
  name: configVersion
  type: integer
- description: __Read-only__ The timestamp when you created the URL protection policy.
  name: createDate
  type: string
- description: __Read-only__ The username of the person who created the URL protection policy.
  name: createdBy
  type: string
- description: A description of the rate policy.
  name: description
  type: string
- description: The hostname and path combinations to match on.
  name: hostnamePaths
  type: array
- description: Enable or disable intelligent load shedding. If enabled, traffic that matches the load shedding categories is eligible for shedding if the origin rate exceeds the load shedding threshold.
  name: intelligentLoadShedding
  type: boolean
- description: The rate policy's unique name.
  name: name
  type: string
- description: __Read-only__ Uniquely identifies the URL protection policy.
  name: policyId
  type: integer
- description: If matching on `hostnamePaths`, specify `SINGLE` to match on a hostname and path, or `MULTIPLE` to match on hostname and path combinations.
  name: protectionType
  type: string
- description: The allowed hits per second during any five-second interval.
  name: rateThreshold
  type: integer
- description: Specify the threshold value, in hits per second, after which traffic can be shed. The `sheddingThresholdHitsPerSec` value must be between 70%-90% of the `rateThreshold` value. If you enabled `intellig
  name: sheddingThresholdHitsPerSec
  type: integer
- description: __Read-only__ The ISO 8601 timestamp when you last updated the URL protection policy.
  name: updateDate
  type: string
- description: __Read-only__ Username who last updated the URL protection policy.
  name: updatedBy
  type: string
- description: __Read-only__ Whether you're currently using the URL protection policy.
  name: used
  type: boolean
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-url-protection-policy-schema.json
slug: api-security-url-protection-policy
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: url-protection-policy
---
