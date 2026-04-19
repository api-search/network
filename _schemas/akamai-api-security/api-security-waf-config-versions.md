---
description: Contains details about a security configuration's versions.
layout: schema
name: waf-config-versions
properties_list:
- description: Uniquely identifies the security configuration.
  name: configId
  type: integer
- description: The name you assigned to the security configuration.
  name: configName
  type: string
- description: The version number of the security configuration that you created most recently.
  name: lastCreatedVersion
  type: integer
- description: The current page number.
  name: page
  type: integer
- description: Represents the number of items per page.
  name: pageSize
  type: integer
- description: The version number of the security configuration that is currently active on the production network.
  name: productionActiveVersion
  type: integer
- description: Uniquely identifies the expedite activation request of the configuration version on the production network.
  name: productionExpediteRequestId
  type: integer
- description: The version number of the security configuration that is currently active on the staging network.
  name: stagingActiveVersion
  type: integer
- description: Uniquely identifies the expedite activation request of the configuration version on the staging network.
  name: stagingExpediteRequestId
  type: integer
- description: The total number of configuration versions.
  name: totalSize
  type: integer
- description: The security configuration's versions.
  name: versionList
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-waf-config-versions-schema.json
slug: api-security-waf-config-versions
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: waf-config-versions
---
