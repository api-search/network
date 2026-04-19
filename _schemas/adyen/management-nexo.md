---
description: Nexo schema from Adyen API
layout: schema
name: Nexo
properties_list:
- description: The list of local and public URLs to send display notifications to when using Terminal API.
  name: displayUrls
  type: object
- description: The key you share with Adyen to secure local communications when using Terminal API.
  name: encryptionKey
  type: object
- description: The list of local and public URLs to send event notifications to when using Terminal API.
  name: eventUrls
  type: object
- description: One or more URLs to send event messages to when using Terminal API.
  name: nexoEventUrls
  type: array
- description: Configures sending event notifications by pressing a button on a terminal, for example used for pay-at-table.
  name: notification
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-nexo-schema.json
slug: management-nexo
tags:
- Payments
- Financial Services
- Fintech
title: Nexo
---
