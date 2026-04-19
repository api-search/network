---
description: Specifies the settings for a new clone of a security configuration.
layout: schema
name: config-clone-post
properties_list:
- description: The configuration version to clone from.
  name: createFromVersion
  type: integer
- description: Specifies whether the application rules should be migrated to the latest version.
  name: ruleUpdate
  type: boolean
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-config-clone-post-schema.json
slug: api-security-config-clone-post
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: config-clone-post
---
