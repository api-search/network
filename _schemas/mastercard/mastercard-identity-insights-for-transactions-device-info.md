---
description: This field contains information related to the consumer device used to authorize with your product or service.
layout: schema
name: DeviceInfo
properties_list:
- description: The device type used to authorize your product or service.
  name: deviceType
  type: string
- description: The country where the consumer device is located when attempting to authorize with your product or service.
  name: country
  type: string
- description: The service provider used by the consumer device when attempting to authorize with your product or service.
  name: ipCarrier
  type: string
- description: The city where the consumer device is located when attempting to authorize with your product or service.
  name: city
  type: string
- description: The name of the browser used to authorize your product or service.
  name: browser
  type: string
- description: The state where the consumer device is located when attempting to authorize with your product or service.
  name: state
  type: string
- description: The device platform used to authorize your product or service.
  name: platform
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-device-info-schema.json
slug: mastercard-identity-insights-for-transactions-device-info
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DeviceInfo
---
