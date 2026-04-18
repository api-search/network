---
class_count: 15
classes:
- ApiInfo
- Issue
- Manager
- Node
- QuerySummary
- Software
- User
- DataCenter
- System
- Bridge
- Connector
- Link
- Fabric
- Network
- CommPolicy
context_file: json-ld/teradata-querygrid-manager-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/json-ld/teradata-querygrid-manager-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Teradata Querygrid Manager Api from Teradata.
layout: jsonld
name: Teradata Querygrid Manager Api Context
namespaces:
- prefix: td
  uri: https://developer.teradata.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: version
  type: string
- container: ''
  name: build
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: name
  type: string
- container: ''
  name: hostname
  type: string
- container: ''
  name: systemId
  type: string
- container: ''
  name: softwareVersion
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: dataCenterId
  type: string
- container: ''
  name: sourceSystemId
  type: string
- container: ''
  name: targetSystemId
  type: string
- container: ''
  name: subnet
  type: string
- container: ''
  name: encryption
  type: boolean
- container: ''
  name: compression
  type: boolean
- container: ''
  name: maxBandwidth
  type: integer
- container: ''
  name: fabricId
  type: string
- container: set
  name: roles
  type: ''
- container: ''
  name: username
  type: string
property_count: 23
provider_name: Teradata
provider_slug: teradata
slug: teradata-querygrid-manager-api-context
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
- JSON-LD
- Linked Data
- Semantic Web
---
