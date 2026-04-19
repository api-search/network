---
description: ViasName schema from Adyen API
layout: schema
name: ViasName
properties_list:
- description: The first name.
  name: firstName
  type: string
- description: 'The gender. >The following values are permitted: `MALE`, `FEMALE`, `UNKNOWN`.'
  name: gender
  type: string
- description: The name's infix, if applicable. >A maximum length of twenty (20) characters is imposed.
  name: infix
  type: string
- description: The last name.
  name: lastName
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-vias-name-schema.json
slug: notifications-vias-name
tags:
- Payments
- Financial Services
- Fintech
title: ViasName
---
