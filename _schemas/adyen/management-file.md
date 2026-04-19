---
description: File schema from Adyen API
layout: schema
name: File
properties_list:
- description: The certificate content converted to a Base64-encoded string.
  name: data
  type: string
- description: The name of the certificate. Must be unique across Wi-Fi profiles.
  name: name
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-file-schema.json
slug: management-file
tags:
- Payments
- Financial Services
- Fintech
title: File
---
