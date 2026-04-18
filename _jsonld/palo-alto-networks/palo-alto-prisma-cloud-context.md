---
class_count: 3
classes:
- Prisma Cloud Policy
- remediation
- rule
context_file: json-ld/palo-alto-prisma-cloud-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-cloud-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Cloud from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Cloud Context
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
  name: cliScriptTemplate
  type: string
- container: ''
  name: cloudType
  type: string
- container: set
  name: complianceMetadata
  type: ''
- container: ''
  name: createdBy
  type: string
- container: ''
  name: createdOn
  type: integer
- container: ''
  name: criteria
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: enabled
  type: boolean
- container: set
  name: labels
  type: string
- container: ''
  name: lastModifiedBy
  type: string
- container: ''
  name: lastModifiedOn
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: parameters
  type: reference
- container: ''
  name: policyId
  type: string
- container: ''
  name: policyType
  type: string
- container: ''
  name: recommendation
  type: string
- container: ''
  name: remediable
  type: boolean
- container: ''
  name: requirementId
  type: string
- container: ''
  name: requirementName
  type: string
- container: ''
  name: rollbackCLIScriptTemplate
  type: string
- container: ''
  name: savedSearch
  type: boolean
- container: ''
  name: sectionDescription
  type: string
- container: ''
  name: sectionId
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: standardName
  type: string
- container: ''
  name: systemDefault
  type: boolean
- container: ''
  name: type
  type: string
- container: ''
  name: withIac
  type: boolean
property_count: 28
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-cloud-context
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
