---
class_count: 7
classes:
- BreachInfo
- Deliverability
- DomainInfo
- EmailQuality
- EmailReputationResponse
- RiskInfo
- SenderInfo
context_file: json-ld/abstract-api-email-reputation-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/json-ld/abstract-api-email-reputation-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Abstract Api Email Reputation from Abstract API.
layout: jsonld
name: Abstract Api Email Reputation Context
namespaces:
- prefix: abstract
  uri: https://abstractapi.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: totalBreaches
  type: integer
- container: ''
  name: dateFirstBreached
  type: date
- container: ''
  name: dateLastBreached
  type: date
- container: set
  name: breachedDomains
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusDetail
  type: string
- container: ''
  name: isFormatValid
  type: boolean
- container: ''
  name: isSmtpValid
  type: boolean
- container: ''
  name: isMxValid
  type: boolean
- container: set
  name: mxRecords
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: domainAge
  type: integer
- container: ''
  name: isLiveSite
  type: boolean
- container: ''
  name: registrar
  type: string
- container: ''
  name: registrarUrl
  type: reference
- container: ''
  name: dateRegistered
  type: date
- container: ''
  name: dateLastRenewed
  type: date
- container: ''
  name: dateExpires
  type: date
- container: ''
  name: isRiskyTld
  type: boolean
- container: ''
  name: score
  type: decimal
- container: ''
  name: isFreeEmail
  type: boolean
- container: ''
  name: isUsernameSuspicious
  type: boolean
- container: ''
  name: isDisposable
  type: boolean
- container: ''
  name: isCatchall
  type: boolean
- container: ''
  name: isSubaddress
  type: boolean
- container: ''
  name: isRole
  type: boolean
- container: ''
  name: isDmarcEnforced
  type: boolean
- container: ''
  name: isSpfStrict
  type: boolean
- container: ''
  name: minimumAge
  type: integer
- container: ''
  name: email
  type: ''
- container: ''
  name: deliverability
  type: string
- container: ''
  name: quality
  type: string
- container: ''
  name: sender
  type: string
- container: ''
  name: risk
  type: string
- container: ''
  name: breaches
  type: string
- container: ''
  name: addressRiskStatus
  type: string
- container: ''
  name: domainRiskStatus
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: emailProviderName
  type: string
- container: ''
  name: organizationName
  type: string
- container: ''
  name: organizationType
  type: string
property_count: 42
provider_name: Abstract API
provider_slug: abstract-api
slug: abstract-api-email-reputation-context
tags:
- Avatars
- Company Enrichment
- Contacts
- Currencies
- Email Validation
- Exchange Rates
- IBAN Validation
- Image Processing
- IP Geolocation
- IP Intelligence
- Phone Validation
- Public Holidays
- Screenshots
- Timezones
- VAT Validation
- Web Scraping
- JSON-LD
- Linked Data
- Semantic Web
---
