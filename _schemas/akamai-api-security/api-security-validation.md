---
description: Contains feedback on validation.
layout: schema
name: validation
properties_list:
- description: The explanation of the error message.
  name: detail
  type: string
- description: The name of the field causing the validation problem.
  name: fieldName
  type: string
- description: The JSON reference to the field in the resource.
  name: jsonReference
  type: string
- description: The title for the error.
  name: title
  type: string
- description: The URL for the error type.
  name: type
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-validation-schema.json
slug: api-security-validation
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: validation
---
