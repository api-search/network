---
description: The PUT Response JSON for HTTP Header Logging.
layout: schema
name: header-logging-put-200
properties_list:
- description: Enables HTTP Header logging.
  name: allowSampling
  type: boolean
- description: Settings for cookie headers.
  name: cookies
  type: object
- description: Settings for custom headers.
  name: customHeaders
  type: object
- description: Settings for standard headers.
  name: standardHeaders
  type: object
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-header-logging-put-200-schema.json
slug: api-security-header-logging-put-200
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: header-logging-put-200
---
