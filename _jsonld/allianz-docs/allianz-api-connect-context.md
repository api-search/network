---
class_count: 21
classes:
- CertificateOfCurrency
- EmailSentResponse
- RatingFactor
- SelfServiceSessionResponse
- LeadReferralRequest
- PolicyDetailsResponse
- PriceEstimateAssistedRequest
- PriceEstimateResponse
- PolicyDetailsAssistedRequest
- LeadReferralResponse
- PolicyDetailsSelfServiceRequest
- Vehicle
- Address
- PriceEstimateEmailRequest
- RatingFactorsResponse
- PriceEstimateSelfServiceRequest
- PriceEstimateSummary
- SelfServiceEstimateResponse
- name
- description
- createdAt
context_file: json-ld/allianz-api-connect-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/allianz-docs/refs/heads/main/json-ld/allianz-api-connect-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Allianz Api Connect from Allianz.
layout: jsonld
name: Allianz Api Connect Context
namespaces:
- prefix: allianz
  uri: https://api.allianz.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: certificateId
  type: string
- container: ''
  name: policyNumber
  type: string
- container: ''
  name: insuredName
  type: string
- container: ''
  name: productType
  type: string
- container: ''
  name: coverageStart
  type: date
- container: ''
  name: coverageEnd
  type: date
- container: ''
  name: sumInsured
  type: double
- container: ''
  name: currency
  type: string
- container: ''
  name: issuedAt
  type: dateTime
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: messageId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: sentAt
  type: dateTime
- container: ''
  name: value
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: sessionUrl
  type: reference
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: customerName
  type: string
- container: ''
  name: customerEmail
  type: string
- container: ''
  name: customerPhone
  type: string
- container: ''
  name: notes
  type: string
- container: ''
  name: quoteId
  type: string
- container: ''
  name: annualPremium
  type: double
- container: ''
  name: customerId
  type: string
- container: ''
  name: propertyAddress
  type: string
- container: ''
  name: estimateId
  type: string
- container: ''
  name: monthlyPremium
  type: double
- container: ''
  name: validUntil
  type: date
- container: ''
  name: paymentFrequency
  type: string
- container: ''
  name: leadId
  type: string
- container: ''
  name: assignedTo
  type: string
- container: ''
  name: redirectUrl
  type: reference
- container: ''
  name: make
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: year
  type: integer
- container: ''
  name: registration
  type: string
- container: ''
  name: street
  type: string
- container: ''
  name: suburb
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: postcode
  type: string
- container: ''
  name: basePremium
  type: double
- container: ''
  name: riskLoading
  type: double
- container: ''
  name: discounts
  type: double
- container: ''
  name: stampDuty
  type: double
- container: set
  name: factors
  type: string
- container: ''
  name: vehicle
  type: string
- container: ''
  name: driverAge
  type: integer
- container: ''
  name: estimateUrl
  type: reference
property_count: 48
provider_name: Allianz
provider_slug: allianz-docs
slug: allianz-api-connect-context
tags:
- Financial Services
- Insurance
- Asset Management
- JSON-LD
- Linked Data
- Semantic Web
---
