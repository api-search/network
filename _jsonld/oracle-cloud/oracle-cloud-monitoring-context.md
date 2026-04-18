---
class_count: 2
classes:
- Metric
- Alarm
context_file: json-ld/oracle-cloud-monitoring-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-monitoring-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Monitoring from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Monitoring Context
namespaces:
- prefix: oci
  uri: https://docs.oracle.com/en-us/iaas/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: compartmentId
  type: string
- container: set
  name: destinations
  type: string
- container: ''
  name: dimensions
  type: ''
- container: ''
  name: displayName
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: isEnabled
  type: boolean
- container: ''
  name: lifecycleState
  type: string
- container: ''
  name: metricCompartmentId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: timeCreated
  type: dateTime
property_count: 13
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-monitoring-context
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
- JSON-LD
- Linked Data
- Semantic Web
---
