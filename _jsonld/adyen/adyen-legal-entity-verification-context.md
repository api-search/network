---
class_count: 4
classes:
- VerificationDeadline
- VerificationError-recursive
- VerificationError
- VerificationErrors
context_file: json-ld/adyen-legal-entity-verification-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-verification-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Verification from Adyen.
layout: jsonld
name: Adyen Legal Entity Verification Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: capabilities
  type: string
- container: set
  name: entityIds
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: code
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: type
  type: string
- container: set
  name: remediatingActions
  type: string
- container: set
  name: subErrors
  type: string
- container: set
  name: problems
  type: string
property_count: 9
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-verification-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
