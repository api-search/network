---
description: Contains a list of selected hostnames for the specified configuration version.
layout: schema
name: hostnames
properties_list:
- description: The list of hostnames for a configuration version.
  name: hostnameList
  type: array
- description: The type of update you want to make to the evaluation hostname list. Use `append` to add additional hostnames, `remove` to delete the hostnames from the list, or `replace` to replace the existing list
  name: mode
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-hostnames-schema.json
slug: api-security-hostnames
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: hostnames
---
