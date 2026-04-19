---
description: Url schema from Adyen API
layout: schema
name: Url
properties_list:
- description: Indicates if the message sent to this URL should be encrypted.
  name: encrypted
  type: boolean
- description: The password for authentication of the notifications.
  name: password
  type: string
- description: 'The URL in the format: http(s)://domain.com.'
  name: url
  type: string
- description: The username for authentication of the notifications.
  name: username
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-url-schema.json
slug: management-url
tags:
- Payments
- Financial Services
- Fintech
title: Url
---
