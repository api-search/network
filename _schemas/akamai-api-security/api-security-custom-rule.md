---
description: Contains settings for a custom rule.
layout: schema
name: custom-rule
properties_list:
- description: Contains the details about the condition that triggers the custom rule.
  name: conditions
  type: array
- description: The custom rule description.
  name: description
  type: string
- description: The time period during which the custom rule is active.
  name: effectiveTimePeriod
  type: object
- description: Uniquely identifies the rule.
  name: id
  type: integer
- description: Whether to inspect the HTTP request for unstructured custom rules.
  name: inspectRequest
  type: boolean
- description: Whether to inspect the HTTP response for unstructured custom rules.
  name: inspectResponse
  type: boolean
- description: The specific conditions to be logged.
  name: loggingOptions
  type: array
- description: The metadata you provided for unstructured custom rules.
  name: metadata
  type: string
- description: The custom rule name.
  name: name
  type: string
- description: Specify `AND` logic to require all conditions, or `OR` logic to require at least one condition to match.
  name: operation
  type: string
- description: Whether the rule is active in the configuration.
  name: ruleActivated
  type: boolean
- description: The portion of traffic to sample, expressed as a percent.
  name: samplingRate
  type: integer
- description: Whether to show traffic from only the staging network, or all traffic. The default setting is `false` and only shows in the response when `true`.
  name: stagingOnly
  type: boolean
- description: Whether you created the rule with the structured custom rule builder or free-form XML. This needs to be `true`.
  name: structured
  type: boolean
- description: The list of labels you assigned to the custom rule.
  name: tag
  type: array
- description: The custom rule version.
  name: version
  type: integer
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-custom-rule-schema.json
slug: api-security-custom-rule
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: custom-rule
---
