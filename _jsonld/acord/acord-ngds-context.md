---
class_count: 19
classes:
- Party
- PolicyList
- CoverageRequest
- Address
- ACORD Policy
- UnderwritingSubmissionResponse
- PolicyRequest
- PolicyUpdate
- Contact
- PartyRequest
- ClaimRequest
- Coverage
- PartyList
- ClaimList
- UnderwritingSubmission
- ACORD Claim
- createdAt
- updatedAt
- description
context_file: json-ld/acord-ngds-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-ld/acord-ngds-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acord Ngds from ACORD.
layout: jsonld
name: Acord Ngds Context
namespaces:
- prefix: acord
  uri: https://www.acord.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: partyId
  type: string
- container: ''
  name: partyType
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: organizationName
  type: string
- container: ''
  name: taxId
  type: string
- container: ''
  name: address
  type: string
- container: set
  name: contacts
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: pagination
  type: string
- container: ''
  name: coverageType
  type: string
- container: ''
  name: limit
  type: decimal
- container: ''
  name: deductible
  type: decimal
- container: ''
  name: premium
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: street1
  type: string
- container: ''
  name: street2
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: policyNumber
  type: string
- container: ''
  name: lineOfBusiness
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: effectiveDate
  type: date
- container: ''
  name: expirationDate
  type: date
- container: ''
  name: premiumAmount
  type: decimal
- container: ''
  name: insuredParty
  type: string
- container: set
  name: coverages
  type: string
- container: set
  name: endorsements
  type: string
- container: ''
  name: submissionId
  type: string
- container: ''
  name: submittedAt
  type: dateTime
- container: ''
  name: notes
  type: string
- container: ''
  name: endorsementNumber
  type: string
- container: ''
  name: contactType
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: lossDate
  type: date
- container: ''
  name: lossDescription
  type: string
- container: ''
  name: lossLocation
  type: string
- container: ''
  name: claimant
  type: string
- container: ''
  name: estimatedLossAmount
  type: decimal
- container: ''
  name: coverageId
  type: string
- container: ''
  name: applicant
  type: string
- container: ''
  name: requestedEffectiveDate
  type: date
- container: ''
  name: requestedExpirationDate
  type: date
- container: ''
  name: riskDetails
  type: string
- container: ''
  name: claimId
  type: string
- container: ''
  name: claimNumber
  type: string
- container: ''
  name: reportedDate
  type: date
- container: ''
  name: lossType
  type: string
- container: ''
  name: adjuster
  type: string
- container: ''
  name: reserveAmount
  type: decimal
- container: ''
  name: paidAmount
  type: decimal
- container: set
  name: payments
  type: string
property_count: 55
provider_name: ACORD
provider_slug: acord
slug: acord-ngds-context
tags:
- Claims
- Insurance
- Policy
- Standards
- Underwriting
- JSON-LD
- Linked Data
- Semantic Web
---
