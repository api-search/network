---
description: DeviceInfo schema from Adyen API
layout: schema
name: DeviceInfo
properties_list:
- description: The technology used to capture the card details.
  name: cardCaptureTechnology
  type: string
- description: The name of the device.
  name: deviceName
  type: string
- description: The form factor of the device to be provisioned.
  name: formFactor
  type: string
- description: The IMEI number of the device being provisioned.
  name: imei
  type: string
- description: The 2-digit device type provided on the ISO messages that the token is being provisioned to.
  name: isoDeviceType
  type: string
- description: The MSISDN of the device being provisioned.
  name: msisdn
  type: string
- description: The name of the device operating system.
  name: osName
  type: string
- description: The version of the device operating system.
  name: osVersion
  type: string
- description: Different types of payments supported for the network token.
  name: paymentTypes
  type: array
- description: The serial number of the device.
  name: serialNumber
  type: string
- description: The architecture or technology used for network token storage.
  name: storageTechnology
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-device-info-schema.json
slug: configuration-device-info
tags:
- Payments
- Financial Services
- Fintech
title: DeviceInfo
---
