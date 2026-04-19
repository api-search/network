---
description: Contains the list of hostnames available for protection and its details.
layout: schema
name: host-info-in-config
properties_list:
- description: The available hosts set for the current user.
  name: availableSet
  type: array
- description: Uniquely identifies the security configuration.
  name: configId
  type: integer
- description: The security configuration version.
  name: configVersion
  type: integer
- description: The requested hosts aren't available in this configuration version.
  name: errorSet
  type: array
- description: Whether the host defined in the ARL file has legacy WAF enabled in the configuration.
  name: protectARLInclusionHost
  type: boolean
- description: The selected set of hostnames in this configuration version.
  name: selectedSet
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-host-info-in-config-schema.json
slug: api-security-host-info-in-config
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: host-info-in-config
---
