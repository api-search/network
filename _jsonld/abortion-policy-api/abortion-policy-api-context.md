---
class_count: 4
classes:
- WaitingPeriods
- MinorsRestrictions
- InsuranceCoverage
- GestationalLimits
context_file: json-ld/abortion-policy-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/abortion-policy-api/refs/heads/main/json-ld/abortion-policy-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Abortion Policy Api from Abortion Policy API.
layout: jsonld
name: Abortion Policy Api Context
namespaces:
- prefix: abortion
  uri: https://abortionpolicyapi.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: waitingPeriodHours
  type: integer
- container: ''
  name: counselingVisits
  type: integer
- container: ''
  name: exceptionHealth
  type: string
- container: ''
  name: waitingPeriodNotes
  type: string
- container: ''
  name: counselingWaivedCondition
  type: string
- container: ''
  name: LastUpdated
  type: string
- container: ''
  name: belowAge
  type: integer
- container: ''
  name: parentsRequired
  type: integer
- container: ''
  name: parentalConsentRequired
  type: boolean
- container: ''
  name: parentalNotificationRequired
  type: boolean
- container: ''
  name: judicialBypassAvailable
  type: boolean
- container: ''
  name: allowsMinorToConsent
  type: boolean
- container: ''
  name: requiresCoverage
  type: boolean
- container: ''
  name: privateCoverageNoRestrictions
  type: boolean
- container: ''
  name: privateExceptionLife
  type: boolean
- container: ''
  name: privateExceptionHealth
  type: string
- container: ''
  name: privateExceptionFetal
  type: string
- container: ''
  name: privateExceptionRapeOrIncest
  type: boolean
- container: ''
  name: exchangeCoverageNoRestrictions
  type: boolean
- container: ''
  name: exchangeExceptionLife
  type: boolean
- container: ''
  name: exchangeExceptionHealth
  type: string
- container: ''
  name: exchangeExceptionFetal
  type: string
- container: ''
  name: exchangeExceptionRapeOrIncest
  type: boolean
- container: ''
  name: exchangeForbidsCoverage
  type: boolean
- container: ''
  name: medicaidCoverageProviderPatientDecision
  type: boolean
- container: ''
  name: medicaidExceptionLife
  type: boolean
- container: ''
  name: medicaidExceptionHealth
  type: string
- container: ''
  name: medicaidExceptionFetal
  type: string
- container: ''
  name: medicaidExceptionRapeOrIncest
  type: boolean
- container: ''
  name: bannedAfterWeeksSinceLmp
  type: integer
- container: ''
  name: exceptionLife
  type: boolean
- container: ''
  name: exceptionFetal
  type: string
- container: ''
  name: exceptionRapeOrIncest
  type: boolean
property_count: 33
provider_name: Abortion Policy API
provider_slug: abortion-policy-api
slug: abortion-policy-api-context
tags:
- Abortion
- Policies
- Healthcare
- Government
- JSON-LD
- Linked Data
- Semantic Web
---
