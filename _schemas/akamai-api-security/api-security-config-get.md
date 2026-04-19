---
description: Contains details about a security configuration.
layout: schema
name: config-get
properties_list:
- description: __Read-only__ Describes the security configuration.
  name: description
  type: string
- description: __Read-only__ Uniquely identifies the security configuration.
  name: id
  type: integer
- description: __Read-only__ The latest version of the security configuration.
  name: latestVersion
  type: integer
- description: __Read-only__ The security configuration name.
  name: name
  type: string
- description: __Read-only__ The list of hostnames protected by this security configuration in the production network.
  name: productionHostnames
  type: array
- description: __Read-only__ The latest security configuration version active in the production network.
  name: productionVersion
  type: integer
- description: __Read-only__ The latest security configuration version active in the staging network.
  name: stagingVersion
  type: integer
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-config-get-schema.json
slug: api-security-config-get
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: config-get
---
