---
description: The header settings for HTTP Header Logging.
layout: schema
name: logging-header-setting
properties_list:
- description: 'Use `all` to log headers for all requests with any standard header. Use `none` to exclude headers for any requests with any standard header from logging. Use `exclude` to exclude headers for requests '
  name: type
  type: string
- description: List of headers to include or exclude depending on the `type` setting.
  name: values
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-logging-header-setting-schema.json
slug: api-security-logging-header-setting
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: logging-header-setting
---
