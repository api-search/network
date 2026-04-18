---
class_count: 9
classes:
- Alert
- AlertFilter
- CloudAccount
- ComplianceStandard
- Policy
- PolicyInput
- Report
- SearchResult
- TimeRange
context_file: json-ld/palo-alto-prisma-cloud-cspm-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-cloud-cspm-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Cloud Cspm Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Cloud Cspm Api Context
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
  name: accountId
  type: string
- container: ''
  name: accountName
  type: string
- container: ''
  name: alertTime
  type: integer
- container: ''
  name: amount
  type: integer
- container: ''
  name: cloudType
  type: string
- container: set
  name: complianceMetadata
  type: reference
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
  name: data
  type: reference
- container: ''
  name: description
  type: string
- container: ''
  name: downloadUrl
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: firstSeen
  type: integer
- container: ''
  name: id
  type: string
- container: set
  name: items
  type: reference
- container: ''
  name: lastModifiedOn
  type: integer
- container: ''
  name: lastModifiedTs
  type: integer
- container: ''
  name: lastSeen
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: numberOfPolicies
  type: integer
- container: ''
  name: operator
  type: string
- container: ''
  name: overallPassed
  type: boolean
- container: ''
  name: policiesAssigned
  type: integer
- container: ''
  name: policy
  type: reference
- container: ''
  name: policyId
  type: string
- container: ''
  name: policyType
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: rating
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: recommendation
  type: string
- container: ''
  name: regionId
  type: string
- container: ''
  name: requirementId
  type: string
- container: ''
  name: requirementName
  type: string
- container: ''
  name: resource
  type: reference
- container: ''
  name: resourceType
  type: string
- container: ''
  name: riskDetail
  type: reference
- container: ''
  name: rrn
  type: string
- container: ''
  name: rule
  type: reference
- container: ''
  name: score
  type: integer
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
  name: status
  type: string
- container: ''
  name: systemDefault
  type: boolean
- container: ''
  name: totalRows
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: value
  type: string
property_count: 49
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-cloud-cspm-api-context
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
