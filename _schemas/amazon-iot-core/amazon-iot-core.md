---
description: Schema defining the structure of an Amazon IoT Core thing resource, including attributes, thing type, thing group membership, certificates, and shadow state.
layout: schema
name: Amazon IoT Core Thing Definition
properties_list:
- description: The name of the thing.
  name: thingName
  type: string
- description: The unique identifier of the thing.
  name: thingId
  type: string
- description: The ARN of the thing.
  name: thingArn
  type: string
- description: The name of the thing type, if assigned.
  name: thingTypeName
  type: string
- description: A list of thing attributes as name-value pairs.
  name: attributes
  type: object
- description: The current version of the thing record.
  name: version
  type: integer
- description: The name of the billing group the thing belongs to.
  name: billingGroupName
  type: string
- description: The default MQTT client ID.
  name: defaultClientId
  type: string
- description: ''
  name: shadow
  type: object
- description: Certificates attached to the thing.
  name: certificates
  type: array
- description: Policies attached to the thing's certificates.
  name: policies
  type: array
- description: The thing groups the thing belongs to.
  name: thingGroups
  type: array
provider_name: Amazon IoT Core
provider_slug: amazon-iot-core
schema_file: json-schema/amazon-iot-core-schema.json
slug: amazon-iot-core
tags:
- AWS
- Device Management
- IoT
- MQTT
- Message Routing
title: Amazon IoT Core Thing Definition
---
