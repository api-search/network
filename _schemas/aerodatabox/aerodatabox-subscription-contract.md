---
description: Describes subscription
layout: schema
name: SubscriptionContract
properties_list:
- description: Identifier of a subscription. Use this ID to control the subscription in future (e.g. update or delete).
  name: id
  type: string
- description: Specifies if the subscription is active
  name: isActive
  type: boolean
- description: ''
  name: billingType
  type: object
- description: Time (UTC) before which subscription must be activated (may be applicable to some non-active newly created subscriptions)
  name: activateBeforeUtc
  type: string
- description: Time (UTC) when subscription expires and will be removed. If not specified, subscription never expires.
  name: expiresOnUtc
  type: string
- description: Time (UTC) when subscription was created
  name: createdOnUtc
  type: string
- description: ''
  name: subject
  type: object
- description: ''
  name: subscriber
  type: object
- description: Additional messages
  name: notices
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-subscription-contract-schema.json
slug: aerodatabox-subscription-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: SubscriptionContract
---
