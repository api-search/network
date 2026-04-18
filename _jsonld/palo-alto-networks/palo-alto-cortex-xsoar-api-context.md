---
class_count: 11
classes:
- CreateEntryRequest
- CreateIncidentRequest
- Entry
- Incident
- IncidentSearchRequest
- IncidentSearchResponse
- Integration
- IntegrationInstance
- Investigation
- Playbook
- UpdateIncidentRequest
context_file: json-ld/palo-alto-cortex-xsoar-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xsoar-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cortex Xsoar Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cortex Xsoar Api Context
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
  name: CustomFields
  type: reference
- container: ''
  name: asc
  type: boolean
- container: ''
  name: beta
  type: boolean
- container: ''
  name: brand
  type: string
- container: ''
  name: byFrom
  type: dateTime
- container: ''
  name: byTo
  type: dateTime
- container: ''
  name: category
  type: string
- container: ''
  name: closeNotes
  type: string
- container: ''
  name: closeReason
  type: string
- container: ''
  name: closed
  type: dateTime
- container: ''
  name: configuration
  type: reference
- container: ''
  name: contents
  type: string
- container: ''
  name: createInvestigation
  type: boolean
- container: ''
  name: created
  type: dateTime
- container: ''
  name: data
  type: string
- container: ''
  name: deprecated
  type: boolean
- container: ''
  name: description
  type: string
- container: ''
  name: details
  type: string
- container: ''
  name: display
  type: string
- container: ''
  name: enabled
  type: string
- container: set
  name: entries
  type: reference
- container: ''
  name: field
  type: string
- container: ''
  name: filter
  type: reference
- container: ''
  name: fromDate
  type: dateTime
- container: ''
  name: fromVersion
  type: string
- container: ''
  name: humanReadable
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: incidentId
  type: string
- container: set
  name: incidents
  type: reference
- container: ''
  name: incomingMapperId
  type: string
- container: ''
  name: investigationId
  type: string
- container: ''
  name: isIntegrationScript
  type: boolean
- container: set
  name: labels
  type: reference
- container: ''
  name: mappingId
  type: string
- container: ''
  name: markdown
  type: boolean
- container: ''
  name: modified
  type: dateTime
- container: ''
  name: name
  type: string
- container: ''
  name: occurred
  type: dateTime
- container: ''
  name: owner
  type: string
- container: ''
  name: page
  type: integer
- container: ''
  name: period
  type: reference
- container: ''
  name: playbookId
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: rawJson
  type: string
- container: ''
  name: relation
  type: string
- container: set
  name: runningPlaybooks
  type: string
- container: ''
  name: searchResultTotal
  type: integer
- container: ''
  name: severity
  type: integer
- container: ''
  name: size
  type: integer
- container: set
  name: sort
  type: reference
- container: ''
  name: sourceBrand
  type: string
- container: ''
  name: sourceInstance
  type: string
- container: ''
  name: status
  type: integer
- container: set
  name: tags
  type: string
- container: ''
  name: toDate
  type: dateTime
- container: ''
  name: toVersion
  type: string
- container: ''
  name: total
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: user
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: version
  type: integer
property_count: 61
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cortex-xsoar-api-context
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
