---
description: Contains details about an overlapping configuration.
layout: schema
name: overlap-config
properties_list:
- description: The configuration ID.
  name: configId
  type: integer
- description: The configuration name.
  name: configName
  type: string
- description: The configuration version.
  name: configVersion
  type: integer
- description: The contract ID.
  name: contractId
  type: string
- description: The contract name.
  name: contractName
  type: string
- description: List of version tags, any combination of `STAGING` and `LAST_CREATED`.
  name: hostnames
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-overlap-config-schema.json
slug: api-security-overlap-config
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: overlap-config
---
