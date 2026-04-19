---
description: A general abstraction of a signal. A node can be specified as an actuator, attribute, branch, or sensor.
layout: schema
name: Node
properties_list:
- description: ''
  name: branch
  type: object
- description: <p>An input component that reports the environmental condition of a vehicle.</p> <note> <p>You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.</p> </not
  name: sensor
  type: object
- description: ''
  name: actuator
  type: object
- description: ''
  name: attribute
  type: object
provider_name: Amazon IoT FleetWise
provider_slug: amazon-iot-fleetwise
schema_file: json-schema/iot-fleetwise-node-schema.json
slug: iot-fleetwise-node
tags:
- Automotive
- AWS
- Connected Vehicles
- IoT
- Telematics
- Vehicle Data
title: Node
---
