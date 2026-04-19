---
description: AdditionalSettingsResponse schema from Adyen API
layout: schema
name: AdditionalSettingsResponse
properties_list:
- description: Object containing list of event codes for which the notifcation will not be sent.
  name: excludeEventCodes
  type: array
- description: Object containing list of event codes for which the notifcation will be sent.
  name: includeEventCodes
  type: array
- description: 'Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates '
  name: properties
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-additional-settings-response-schema.json
slug: management-additional-settings-response
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalSettingsResponse
---
