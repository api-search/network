---
description: Key schema from Adyen API
layout: schema
name: Key
properties_list:
- description: The unique identifier of the shared key.
  name: identifier
  type: string
- description: The secure passphrase to protect the shared key.
  name: passphrase
  type: string
- description: The version number of the shared key.
  name: version
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-key-schema.json
slug: management-key
tags:
- Payments
- Financial Services
- Fintech
title: Key
---
