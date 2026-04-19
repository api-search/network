---
description: AllowedOrigin schema from Adyen API
layout: schema
name: AllowedOrigin
properties_list:
- description: References to resources linked to the allowed origin.
  name: _links
  type: object
- description: Domain of the allowed origin.
  name: domain
  type: string
- description: Unique identifier of the allowed origin.
  name: id
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-allowed-origin-schema.json
slug: management-allowed-origin
tags:
- Payments
- Financial Services
- Fintech
title: AllowedOrigin
---
