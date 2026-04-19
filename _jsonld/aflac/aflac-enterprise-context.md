---
class_count: 17
classes:
- GroupList
- PolicyList
- EnrollmentList
- Group
- name
- EligibilityResponse
- Claim
- EnrollmentRequest
- EligibilityRequest
- ClaimRequest
- description
- Enrollment
- createdAt
- updatedAt
- Dependent
- Policy
- ClaimList
context_file: json-ld/aflac-enterprise-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aflac/refs/heads/main/json-ld/aflac-enterprise-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aflac Enterprise from aflac.
layout: jsonld
name: Aflac Enterprise Context
namespaces:
- prefix: aflac
  uri: https://aflac.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: items
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: limit
  type: integer
- container: ''
  name: offset
  type: integer
- container: ''
  name: groupId
  type: string
- container: ''
  name: employerName
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: employeeCount
  type: integer
- container: ''
  name: effectiveDate
  type: date
- container: ''
  name: eligible
  type: boolean
- container: ''
  name: employeeId
  type: string
- container: ''
  name: productType
  type: string
- container: ''
  name: ineligibilityReason
  type: string
- container: ''
  name: claimId
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: claimType
  type: string
- container: ''
  name: incidentDate
  type: date
- container: ''
  name: submissionDate
  type: dateTime
- container: ''
  name: benefitAmount
  type: decimal
- container: ''
  name: denialReason
  type: string
- container: ''
  name: coverageLevel
  type: string
- container: set
  name: dependents
  type: string
- container: ''
  name: enrollmentId
  type: string
- container: ''
  name: terminationDate
  type: date
- container: ''
  name: monthlyPremium
  type: decimal
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: relationship
  type: string
- container: ''
  name: faceValue
  type: decimal
property_count: 30
provider_name: aflac
provider_slug: aflac
slug: aflac-enterprise-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
