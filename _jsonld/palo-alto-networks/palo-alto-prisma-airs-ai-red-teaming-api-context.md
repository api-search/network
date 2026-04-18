---
class_count: 7
classes:
- AttackCategory
- Scan
- ScanReport
- ScanRequest
- ScanTarget
- ScanTargetRequest
- VulnerabilityFinding
context_file: json-ld/palo-alto-prisma-airs-ai-red-teaming-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-airs-ai-red-teaming-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Airs Ai Red Teaming Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Airs Ai Red Teaming Api Context
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
- container: set
  name: attackCategories
  type: string
- container: ''
  name: attackCount
  type: integer
- container: ''
  name: attackPrompt
  type: string
- container: ''
  name: attacksExecuted
  type: integer
- container: ''
  name: authConfig
  type: reference
- container: ''
  name: categoryId
  type: string
- container: ''
  name: categoryName
  type: string
- container: set
  name: categorySummaries
  type: reference
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: completedAttacks
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: credential
  type: string
- container: set
  name: customPrompts
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: endpointUrl
  type: reference
- container: ''
  name: errorMessage
  type: string
- container: set
  name: examples
  type: string
- container: ''
  name: findingId
  type: string
- container: set
  name: findings
  type: reference
- container: ''
  name: generatedAt
  type: dateTime
- container: ''
  name: headerName
  type: string
- container: ''
  name: max
  type: string
- container: ''
  name: maxAttacksPerCategory
  type: integer
- container: ''
  name: min
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: modelResponse
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: overallRiskScore
  type: float
- container: ''
  name: progress
  type: float
- container: ''
  name: remediation
  type: string
- container: ''
  name: riskScore
  type: float
- container: ''
  name: scanId
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: severityRange
  type: reference
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: systemPrompt
  type: string
- container: ''
  name: targetId
  type: string
- container: ''
  name: targetName
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: totalAttacks
  type: integer
- container: ''
  name: totalAttacksExecuted
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: vulnerabilitiesFound
  type: integer
property_count: 45
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-airs-ai-red-teaming-api-context
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
