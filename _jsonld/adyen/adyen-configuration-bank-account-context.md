---
class_count: 5
classes:
- BankAccountIdentificationTypeRequirement
- BankAccountIdentificationValidationRequest
- BankAccountModel
- BankAccount
- description
context_file: json-ld/adyen-configuration-bank-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-bank-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Bank Account from Adyen.
layout: jsonld
name: Adyen Configuration Bank Account Context
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
  name: bankAccountIdentificationTypes
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: accountIdentification
  type: string
- container: ''
  name: formFactor
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-bank-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
