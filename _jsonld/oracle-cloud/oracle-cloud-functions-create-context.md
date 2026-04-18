---
class_count: 2
classes:
- CreateFunctionDetails
- CreateApplicationDetails
context_file: json-ld/oracle-cloud-functions-create-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-functions-create-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Functions Create from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Functions Create Context
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
  name: applicationId
  type: string
- container: ''
  name: compartmentId
  type: string
- container: ''
  name: config
  type: ''
- container: ''
  name: displayName
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: memoryInMBs
  type: integer
- container: set
  name: subnetIds
  type: string
- container: ''
  name: timeoutInSeconds
  type: integer
property_count: 8
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-functions-create-context
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
