---
class_count: 6
classes:
- Thermostat
- HvacSchedule
- SensorReading
- EnergyReport
- name
- description
context_file: json-ld/aircon-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/json-ld/aircon-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aircon from Aircon.
layout: jsonld
name: Aircon Context
namespaces:
- prefix: aircon
  uri: https://aircon.api-evangelist.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: currentTemperature
  type: decimal
- container: ''
  name: targetTemperature
  type: decimal
- container: ''
  name: hvacMode
  type: string
- container: ''
  name: hvacStatus
  type: string
- container: ''
  name: fanMode
  type: string
- container: ''
  name: humidity
  type: decimal
- container: ''
  name: targetHumidity
  type: decimal
- container: ''
  name: isOnline
  type: boolean
- container: ''
  name: heatSetpoint
  type: decimal
- container: ''
  name: coolSetpoint
  type: decimal
- container: ''
  name: startTime
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: sensorType
  type: string
- container: ''
  name: inUse
  type: boolean
- container: ''
  name: heatingRuntimeMinutes
  type: integer
- container: ''
  name: coolingRuntimeMinutes
  type: integer
- container: ''
  name: fanRuntimeMinutes
  type: integer
- container: ''
  name: estimatedKwh
  type: decimal
- container: ''
  name: averageIndoorTemp
  type: decimal
- container: ''
  name: averageOutdoorTemp
  type: decimal
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: lastUpdated
  type: dateTime
property_count: 22
provider_name: Aircon
provider_slug: aircon
slug: aircon-context
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
- JSON-LD
- Linked Data
- Semantic Web
---
