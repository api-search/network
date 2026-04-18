---
class_count: 4
classes:
- BPACheck
- BPAReport
- BPARequest
- BPARequestStatus
context_file: json-ld/palo-alto-aiops-ngfw-bpa-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-aiops-ngfw-bpa-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Aiops Ngfw Bpa Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Aiops Ngfw Bpa Api Context
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
  name: category
  type: string
- container: set
  name: categoryScores
  type: reference
- container: ''
  name: checkId
  type: string
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: currentValue
  type: string
- container: ''
  name: deploymentType
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: deviceInfo
  type: reference
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: failed
  type: integer
- container: ''
  name: failedChecks
  type: integer
- container: ''
  name: generatedAt
  type: dateTime
- container: ''
  name: hostname
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: notApplicable
  type: integer
- container: ''
  name: overallScore
  type: float
- container: ''
  name: panOsVersion
  type: string
- container: ''
  name: passed
  type: integer
- container: ''
  name: passedChecks
  type: integer
- container: ''
  name: recommendedValue
  type: string
- container: set
  name: references
  type: reference
- container: ''
  name: remediation
  type: string
- container: ''
  name: reportId
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: score
  type: float
- container: ''
  name: serialNumber
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: submittedAt
  type: dateTime
- container: ''
  name: totalChecks
  type: integer
- container: ''
  name: version
  type: string
property_count: 32
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-aiops-ngfw-bpa-api-context
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
