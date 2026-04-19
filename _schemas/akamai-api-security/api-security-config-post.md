---
description: Specifies the details of a security config.
layout: schema
name: config-post
properties_list:
- description: Contract ID.
  name: contractId
  type: string
- description: Contains details about a source configuration and version for cloning a new security configuration.
  name: createFrom
  type: object
- description: Describes the security configuration.
  name: description
  type: string
- description: Group ID.
  name: groupId
  type: integer
- description: List of hostnames to be added to the configuration.
  name: hostnames
  type: array
- description: The name you assigned to the security configuration.
  name: name
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-config-post-schema.json
slug: api-security-config-post
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: config-post
---
