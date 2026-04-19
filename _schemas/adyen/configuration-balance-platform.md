---
description: BalancePlatform schema from Adyen API
layout: schema
name: BalancePlatform
properties_list:
- description: Your description of the balance platform, maximum 300 characters.
  name: description
  type: string
- description: The unique identifier of the balance platform.
  name: id
  type: string
- description: 'The status of the balance platform. Possible values: **Active**, **Inactive**, **Closed**, **Suspended**.'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-balance-platform-schema.json
slug: configuration-balance-platform
tags:
- Payments
- Financial Services
- Fintech
title: BalancePlatform
---
