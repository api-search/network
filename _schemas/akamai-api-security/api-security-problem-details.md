---
description: Details the errors you can receive.
layout: schema
name: problem-details
properties_list:
- description: The detailed error message.
  name: detail
  type: string
- description: Pointers to fields for which invalid input was provided, whose values are messages detailing the reason this input was invalid for this field.
  name: fieldErrors
  type: object
- description: The non-referenceable URI that indicates the error instance.
  name: instance
  type: string
- description: The HTTP status code.
  name: status
  type: integer
- description: The error title.
  name: title
  type: string
- description: The URL for the error type.
  name: type
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-problem-details-schema.json
slug: api-security-problem-details
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: problem-details
---
