---
description: AttributionEvent schema from Amplitude Attribution API
layout: schema
name: AttributionEvent
properties_list:
- description: The user ID to attribute the campaign event to. Required unless device_id is present.
  name: user_id
  type: string
- description: The device ID. Required unless user_id is present.
  name: device_id
  type: string
- description: The type of attribution event, typically a campaign-related event such as install or re-engage.
  name: event_type
  type: string
- description: The platform of the device, such as iOS or Android.
  name: platform
  type: string
- description: The operating system name.
  name: os_name
  type: string
- description: The operating system version.
  name: os_version
  type: string
- description: The brand of the device.
  name: device_brand
  type: string
- description: The manufacturer of the device.
  name: device_manufacturer
  type: string
- description: The model of the device.
  name: device_model
  type: string
- description: The carrier of the device.
  name: carrier
  type: string
- description: The country of the user.
  name: country
  type: string
- description: The region or state of the user.
  name: region
  type: string
- description: The city of the user.
  name: city
  type: string
- description: The language setting of the user.
  name: language
  type: string
- description: The Google Play Services advertising ID (Android).
  name: adid
  type: string
- description: The Identifier for Advertiser (iOS).
  name: idfa
  type: string
- description: The Identifier for Vendor (iOS).
  name: idfv
  type: string
- description: User property operations to set alongside the attribution event. Typically used to set campaign-related properties like utm_source, utm_medium, utm_campaign, utm_term, and utm_content.
  name: user_properties
  type: object
- description: Additional properties associated with the attribution event such as campaign name, ad group, ad creative, and network.
  name: event_properties
  type: object
- description: The timestamp of the event in milliseconds since epoch.
  name: time
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/attribution-api-attribution-event-schema.json
slug: attribution-api-attribution-event
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: AttributionEvent
---
