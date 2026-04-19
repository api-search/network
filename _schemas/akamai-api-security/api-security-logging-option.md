---
description: Condition to be logged.
layout: schema
name: logging-option
properties_list:
- description: The unique identifier for each logging option. See [Logging option values](https://techdocs.akamai.com/application-security/reference/logging-option-values).
  name: id
  type: string
- description: A description of the logging option type.
  name: name
  type: string
- description: The value on which to match when determining whether to log the custom rule condition.
  name: value
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-logging-option-schema.json
slug: api-security-logging-option
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: logging-option
---
