---
class_count: 0
classes: []
context_file: json-ld/splunk-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/json-ld/splunk-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Splunk from Splunk.
layout: jsonld
name: Splunk Context
namespaces:
- prefix: splunk
  uri: https://dev.splunk.com/enterprise/reference#
- prefix: splunkrest
  uri: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: hydra
  uri: http://www.w3.org/ns/hydra/core#
- prefix: spdx
  uri: http://spdx.org/rdf/terms#
- prefix: ssn
  uri: http://www.w3.org/ns/ssn/
- prefix: sosa
  uri: http://www.w3.org/ns/sosa/
properties:
- container: ''
  name: SearchJob
  type: ''
- container: ''
  name: Event
  type: ''
- container: ''
  name: Index
  type: ''
- container: ''
  name: DataInput
  type: ''
- container: ''
  name: MonitorInput
  type: ''
- container: ''
  name: HecToken
  type: ''
- container: ''
  name: SearchResults
  type: ''
- container: ''
  name: owner
  type: string
- container: ''
  name: app
  type: string
- container: ''
  name: sharing
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: id
  type: reference
- container: ''
  name: created
  type: dateTime
- container: ''
  name: modified
  type: dateTime
property_count: 15
provider_name: Splunk
provider_slug: splunk
slug: splunk-context
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
- JSON-LD
- Linked Data
- Semantic Web
---
