---
description: EventUrl schema from Adyen API
layout: schema
name: EventUrl
properties_list:
- description: One or more local URLs to send event notifications to when using Terminal API.
  name: eventLocalUrls
  type: array
- description: One or more public URLs to send event notifications to when using Terminal API.
  name: eventPublicUrls
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-event-url-schema.json
slug: management-event-url
tags:
- Payments
- Financial Services
- Fintech
title: EventUrl
---
