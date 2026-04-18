---
description: The insights details associated with the device.
layout: schema
name: DeviceInsights
properties_list:
- description: The generated unique device identifier.
  name: uDeviceId
  type: string
- description: The ISO UTC timestamp when the device was last seen.
  name: lastSeen
  type: string
- description: The ISO UTC timestamp when the device was first seen.
  name: firstSeen
  type: string
- description: Number of of days since the device was last seen. If the device has not been observed before, lastSeenDays will be 0.
  name: lastSeenDays
  type: integer
- description: Number of days since the device was first seen. If the device has not been observed before, firstSeenDays will be 0.
  name: firstSeenDays
  type: integer
- description: This field contains the account device identification hash. If hashedAccountId (optional field) is not present in the request or the device resolved to a default UDID, the accountDeviceId field will b
  name: accountDeviceId
  type: string
- description: ''
  name: alerts
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-device-insights-schema.json
slug: mastercard-identity-insights-for-transactions-device-insights
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DeviceInsights
---
