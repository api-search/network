---
description: Resource schema from Adyen API
layout: schema
name: Resource
properties_list:
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: The ID of the resource.
  name: id
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-resource-schema.json
slug: transfer-webhooks-resource
tags:
- Payments
- Financial Services
- Fintech
title: Resource
---
