---
description: Command to create web-hook subscription
layout: schema
name: CreateWebHookSubscription
properties_list:
- description: 'Destination HTTP-endpoint where notifications will be sent to. Requirements: * must be a valid public HTTP(S) URL not requiring additional authorization; * must use standard or alternative HTTP or HTT'
  name: url
  type: string
- description: 'Maximum number of times a delivery attempt is retried after initial delivery attempt failure. Current default value is: * `2` for the old, lifetime-based web-hook subscriptions (will be phased out aft'
  name: maxDeliveryRetries
  type: integer
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-create-web-hook-subscription-schema.json
slug: aerodatabox-create-web-hook-subscription
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: CreateWebHookSubscription
---
