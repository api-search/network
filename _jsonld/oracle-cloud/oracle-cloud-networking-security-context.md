---
class_count: 1
classes:
- SecurityList
context_file: json-ld/oracle-cloud-networking-security-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-networking-security-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Networking Security from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Networking Security Context
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
- container: ''
  name: displayName
  type: string
- container: set
  name: egressSecurityRules
  type: reference
- container: ''
  name: id
  type: string
- container: set
  name: ingressSecurityRules
  type: reference
- container: ''
  name: lifecycleState
  type: string
- container: ''
  name: timeCreated
  type: dateTime
- container: ''
  name: vcnId
  type: string
property_count: 8
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-networking-security-context
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
