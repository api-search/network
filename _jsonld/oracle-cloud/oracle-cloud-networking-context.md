---
class_count: 2
classes:
- Vcn
- Subnet
context_file: json-ld/oracle-cloud-networking-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-networking-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Networking from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Networking Context
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
  name: availabilityDomain
  type: string
- container: ''
  name: cidrBlock
  type: string
- container: set
  name: cidrBlocks
  type: string
- container: ''
  name: compartmentId
  type: string
- container: ''
  name: defaultDhcpOptionsId
  type: string
- container: ''
  name: defaultRouteTableId
  type: string
- container: ''
  name: defaultSecurityListId
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: dnsLabel
  type: string
- container: ''
  name: freeformTags
  type: ''
- container: ''
  name: id
  type: string
- container: ''
  name: lifecycleState
  type: string
- container: ''
  name: prohibitPublicIpOnVnic
  type: boolean
- container: ''
  name: routeTableId
  type: string
- container: set
  name: securityListIds
  type: string
- container: ''
  name: timeCreated
  type: dateTime
- container: ''
  name: vcnId
  type: string
property_count: 17
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-networking-context
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
