---
description: Modification schema from Adyen API
layout: schema
name: Modification
properties_list:
- description: The direction of the money movement.
  name: direction
  type: string
- description: Our reference for the modification.
  name: id
  type: string
- description: Your reference for the modification, used internally within your platform.
  name: reference
  type: string
- description: The status of the transfer event.
  name: status
  type: string
- description: The type of transfer modification.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-modification-schema.json
slug: transfer-webhooks-modification
tags:
- Payments
- Financial Services
- Fintech
title: Modification
---
