---
class_count: 9
classes:
- EmailDestination
- EmailDestinationRequest
- ForwardingStatus
- HTTPSDestination
- HTTPSDestinationRequest
- LogForwardingProfile
- LogForwardingProfileRequest
- SyslogDestination
- SyslogDestinationRequest
context_file: json-ld/palo-alto-strata-logging-service-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-strata-logging-service-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Strata Logging Service Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Strata Logging Service Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: andAlsoTo
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: ''
  name: destinationCount
  type: integer
- container: ''
  name: destinationId
  type: string
- container: ''
  name: destinationType
  type: string
- container: set
  name: destinations
  type: reference
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: errorCount24h
  type: integer
- container: ''
  name: facility
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: gateway
  type: string
- container: ''
  name: headers
  type: reference
- container: ''
  name: httpMethod
  type: string
- container: ''
  name: lastError
  type: string
- container: ''
  name: lastSuccessfulDelivery
  type: dateTime
- container: set
  name: logTypes
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: overallStatus
  type: string
- container: ''
  name: port
  type: integer
- container: ''
  name: profileId
  type: string
- container: ''
  name: protocol
  type: string
- container: ''
  name: server
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: tlsVerify
  type: boolean
- container: ''
  name: to
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: uri
  type: reference
property_count: 29
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-strata-logging-service-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
