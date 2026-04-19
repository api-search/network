---
description: Contains configuration version details.
layout: schema
name: waf-config-version
properties_list:
- description: __Read-only__ The version from which you cloned this version.
  name: basedOn
  type: integer
- description: __Read-only__ Uniquely identifies the security configuration.
  name: configId
  type: integer
- description: The security configuration name.
  name: configName
  type: string
- description: __Read-only__ The date when you created the configuration version.
  name: createDate
  type: string
- description: __Read-only__ The user who created the configuration version.
  name: createdBy
  type: string
- description: __Read-only__ The activation status of the configuration version in the production network.
  name: production
  type: object
- description: __Read-only__ The activation status of the configuration version in the staging network.
  name: staging
  type: object
- description: __Read-only__ The security configuration version.
  name: version
  type: integer
- description: The notes you entered for the configuration version.
  name: versionNotes
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-waf-config-version-schema.json
slug: api-security-waf-config-version
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: waf-config-version
---
