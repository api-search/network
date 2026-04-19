---
class_count: 4
classes:
- InsurancePolicy
- InsuranceClaim
- RiskProfile
- CyberRiskProfile
context_file: json-ld/aig-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aig/refs/heads/main/json-ld/aig-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aig from AIG.
layout: jsonld
name: Aig Context
namespaces:
- prefix: aig
  uri: https://aig.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: policyNumber
  type: string
- container: ''
  name: policyType
  type: string
- container: ''
  name: insuredName
  type: string
- container: ''
  name: effectiveDate
  type: date
- container: ''
  name: expirationDate
  type: date
- container: ''
  name: premium
  type: decimal
- container: ''
  name: coverageLimit
  type: decimal
- container: ''
  name: deductible
  type: decimal
- container: ''
  name: claimNumber
  type: string
- container: ''
  name: lossDate
  type: date
- container: ''
  name: lossAmount
  type: decimal
- container: ''
  name: claimStatus
  type: string
- container: ''
  name: naicsCode
  type: string
- container: ''
  name: annualRevenue
  type: decimal
- container: ''
  name: employeeCount
  type: integer
- container: ''
  name: mfaEnabled
  type: boolean
- container: ''
  name: incidentResponsePlan
  type: boolean
property_count: 17
provider_name: AIG
provider_slug: aig
slug: aig-context
tags:
- Insurance
- Financial Services
- Property Casualty
- Cyber Insurance
- Enterprise
- JSON-LD
- Linked Data
- Semantic Web
---
