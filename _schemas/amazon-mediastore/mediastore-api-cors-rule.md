---
description: A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
layout: schema
name: CorsRule
properties_list:
- description: ''
  name: AllowedOrigins
  type: object
- description: ''
  name: AllowedMethods
  type: object
- description: ''
  name: AllowedHeaders
  type: object
- description: ''
  name: MaxAgeSeconds
  type: object
- description: ''
  name: ExposeHeaders
  type: object
provider_name: Amazon MediaStore
provider_slug: amazon-mediastore
schema_file: json-schema/mediastore-api-cors-rule-schema.json
slug: mediastore-api-cors-rule
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CorsRule
---
