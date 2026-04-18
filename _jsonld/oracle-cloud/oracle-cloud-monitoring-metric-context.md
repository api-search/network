---
class_count: 1
classes:
- MetricData
context_file: json-ld/oracle-cloud-monitoring-metric-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-monitoring-metric-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Monitoring Metric from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Monitoring Metric Context
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
- container: set
  name: aggregatedDatapoints
  type: reference
- container: ''
  name: compartmentId
  type: string
- container: ''
  name: dimensions
  type: ''
- container: ''
  name: name
  type: string
- container: ''
  name: namespace
  type: string
property_count: 5
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-monitoring-metric-context
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
