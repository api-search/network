---
class_count: 6
classes:
- CodeError
- Fix
- Repository
- ScanIntegration
- ScanStatus
- Suppression
context_file: json-ld/palo-alto-prisma-cloud-code-security-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-cloud-code-security-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Cloud Code Security Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Cloud Code Security Api Context
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
  name: branch
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: createdBy
  type: string
- container: ''
  name: critical
  type: integer
- container: ''
  name: defaultBranch
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: errorCounts
  type: reference
- container: ''
  name: errorId
  type: string
- container: ''
  name: errorsBySeverity
  type: reference
- container: ''
  name: expirationDate
  type: dateTime
- container: set
  name: fileLineRange
  type: integer
- container: ''
  name: filePath
  type: string
- container: ''
  name: filesScanned
  type: integer
- container: ''
  name: firstDetected
  type: dateTime
- container: ''
  name: fixId
  type: string
- container: ''
  name: framework
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: guideline
  type: string
- container: ''
  name: high
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: info
  type: integer
- container: ''
  name: isPublic
  type: boolean
- container: ''
  name: justification
  type: string
- container: ''
  name: lastDetected
  type: dateTime
- container: ''
  name: lastScanDate
  type: dateTime
- container: ''
  name: lastScanStatus
  type: string
- container: set
  name: lineRange
  type: integer
- container: ''
  name: low
  type: integer
- container: ''
  name: medium
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: originalCode
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: policyName
  type: string
- container: ''
  name: repositoryId
  type: string
- container: ''
  name: resourceName
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: resourcesScanned
  type: integer
- container: set
  name: scanTypes
  type: string
- container: ''
  name: scanId
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: sourceType
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: suggestedCode
  type: string
- container: ''
  name: summary
  type: reference
- container: ''
  name: suppressedErrorCount
  type: integer
- container: ''
  name: suppressionId
  type: string
- container: ''
  name: suppressionType
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: url
  type: string
property_count: 53
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-cloud-code-security-api-context
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
