---
class_count: 6
classes:
- EdgarCompanySubmission
- GaapAccountingStandard
- XbrlFinancialFact
- description
- name
- url
context_file: json-ld/accounting-standards-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/json-ld/accounting-standards-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Accounting Standards from Accounting Standards.
layout: jsonld
name: Accounting Standards Context
namespaces:
- prefix: acct
  uri: https://xbrl.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: accessionNumber
  type: string
- container: ''
  name: accn
  type: string
- container: ''
  name: applicability
  type: string
- container: ''
  name: cik
  type: string
- container: ''
  name: concept
  type: string
- container: ''
  name: effectiveDate
  type: date
- container: ''
  name: end
  type: date
- container: ''
  name: entityName
  type: string
- container: ''
  name: entityType
  type: string
- container: set
  name: exchanges
  type: string
- container: set
  name: facts
  type: string
- container: ''
  name: filed
  type: date
- container: set
  name: filingDate
  type: date
- container: ''
  name: filings
  type: string
- container: ''
  name: fiscalYearEnd
  type: string
- container: set
  name: form
  type: string
- container: ''
  name: fp
  type: string
- container: ''
  name: frame
  type: string
- container: ''
  name: fy
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: issuedDate
  type: date
- container: ''
  name: label
  type: string
- container: set
  name: primaryDocument
  type: string
- container: ''
  name: recent
  type: string
- container: set
  name: relatedTopics
  type: string
- container: ''
  name: sic
  type: string
- container: ''
  name: sicDescription
  type: string
- container: ''
  name: start
  type: date
- container: ''
  name: stateOfIncorporation
  type: string
- container: ''
  name: summary
  type: string
- container: ''
  name: taxonomy
  type: string
- container: set
  name: tickers
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: topic
  type: string
- container: ''
  name: topicName
  type: string
- container: ''
  name: unit
  type: string
- container: set
  name: units
  type: string
- container: ''
  name: val
  type: decimal
- container: ''
  name: website
  type: reference
property_count: 39
provider_name: Accounting Standards
provider_slug: accounting-standards
slug: accounting-standards-context
tags:
- Accounting Standards
- Finance
- GAAP
- IFRS
- XBRL
- Financial Reporting
- SEC
- FASB
- JSON-LD
- Linked Data
- Semantic Web
---
