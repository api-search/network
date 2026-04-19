---
description: DataCenter schema from Adyen API
layout: schema
name: DataCenter
properties_list:
- description: 'The unique [live URL prefix](https://docs.adyen.com/development-resources/live-endpoints#live-url-prefix) for your live endpoint. Each data center has its own live URL prefix. This field is empty for '
  name: livePrefix
  type: string
- description: 'The name assigned to a data center, for example **EU** for the European data center. Possible values are: * **default**: the European data center. This value is always returned in the test environment'
  name: name
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-data-center-schema.json
slug: management-data-center
tags:
- Payments
- Financial Services
- Fintech
title: DataCenter
---
