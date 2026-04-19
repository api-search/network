---
description: Contains details about the hostname and its status.
layout: schema
name: hostname-object
properties_list:
- description: Whether the hostname is active in the production network.
  name: activeInProduction
  type: boolean
- description: Whether the hostname is active in the staging network.
  name: activeInStaging
  type: boolean
- description: Whether the hostname is Akamai Resource Locator (ARL) included.
  name: arlInclusion
  type: boolean
- description: Uniquely identifies the configuration that protects the hostname.
  name: configIdInProduction
  type: integer
- description: The name of the configuration that protects the hostname.
  name: configNameInProduction
  type: string
- description: The hostname.
  name: hostname
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-hostname-object-schema.json
slug: api-security-hostname-object
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: hostname-object
---
