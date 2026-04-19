---
class_count: 3
classes:
- MachineLocation
- Telemetry
- Machine
context_file: json-ld/agco-telematics-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agco/refs/heads/main/json-ld/agco-telematics-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agco Telematics from agco.
layout: jsonld
name: Agco Telematics Context
namespaces:
- prefix: agco
  uri: https://agcocorp.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: machineId
  type: string
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: altitude
  type: decimal
- container: ''
  name: heading
  type: decimal
- container: ''
  name: groundSpeed
  type: decimal
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: engineSpeed
  type: decimal
- container: ''
  name: engineLoad
  type: decimal
- container: ''
  name: engineHours
  type: decimal
- container: ''
  name: fuelLevel
  type: decimal
- container: ''
  name: fuelConsumptionRate
  type: decimal
- container: ''
  name: coolantTemperature
  type: decimal
- container: set
  name: faultCodes
  type: string
- container: ''
  name: operatingMode
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: serialNumber
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
property_count: 24
provider_name: agco
provider_slug: agco
slug: agco-telematics-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
