---
class_count: 3
classes:
- CreatePolicyDetails
- CreateUserDetails
- CreateGroupDetails
context_file: json-ld/oracle-cloud-iam-create-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-iam-create-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Iam Create from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Iam Create Context
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
  name: description
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: name
  type: string
- container: set
  name: statements
  type: string
property_count: 5
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-iam-create-context
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
