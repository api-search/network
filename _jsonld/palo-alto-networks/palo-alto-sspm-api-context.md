---
class_count: 6
classes:
- CatalogApp
- JiraIntegration
- JiraIntegrationRequest
- OnboardAppRequest
- OnboardedApp
- PostureCheck
context_file: json-ld/palo-alto-sspm-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sspm-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sspm Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sspm Api Context
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
  name: apiToken
  type: string
- container: ''
  name: appId
  type: string
- container: ''
  name: appType
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: checkCount
  type: integer
- container: ''
  name: checkId
  type: string
- container: ''
  name: checkName
  type: string
- container: ''
  name: checkSummary
  type: reference
- container: ''
  name: checkType
  type: string
- container: set
  name: complianceFrameworks
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: credentials
  type: reference
- container: ''
  name: critical
  type: integer
- container: ''
  name: description
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: high
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: issueType
  type: string
- container: ''
  name: jiraUrl
  type: reference
- container: ''
  name: lastEvaluatedAt
  type: dateTime
- container: ''
  name: lastScannedAt
  type: dateTime
- container: ''
  name: logoUrl
  type: reference
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
  name: onboardedAt
  type: dateTime
- container: ''
  name: pass
  type: integer
- container: ''
  name: projectKey
  type: string
- container: ''
  name: remediation
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: severityMapping
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: suppressionJustification
  type: string
- container: ''
  name: tenantId
  type: string
property_count: 36
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sspm-api-context
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
