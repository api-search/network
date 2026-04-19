---
description: <p>A signal that represents a vehicle device such as the engine, heater, and door locks. Data from an actuator reports the state of a certain vehicle device.</p> <note> <p> Updating actuator data can change the state of a device. For example, you can turn on or off the heater by updating its actuator data.</p> </note>
layout: schema
name: Actuator
properties_list:
- description: ''
  name: fullyQualifiedName
  type: object
- description: ''
  name: dataType
  type: object
- description: ''
  name: description
  type: object
- description: ''
  name: unit
  type: object
- description: ''
  name: allowedValues
  type: object
- description: ''
  name: min
  type: object
- description: ''
  name: max
  type: object
- description: ''
  name: assignedValue
  type: object
- description: ''
  name: deprecationMessage
  type: object
- description: ''
  name: comment
  type: object
provider_name: Amazon IoT FleetWise
provider_slug: amazon-iot-fleetwise
schema_file: json-schema/iot-fleetwise-actuator-schema.json
slug: iot-fleetwise-actuator
tags:
- Automotive
- AWS
- Connected Vehicles
- IoT
- Telematics
- Vehicle Data
title: Actuator
---
