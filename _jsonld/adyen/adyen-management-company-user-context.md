---
class_count: 3
classes:
- CompanyUser
- email
- name
context_file: json-ld/adyen-management-company-user-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-company-user-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Company User from Adyen.
layout: jsonld
name: Adyen Management Company User Context
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
- container: ''
  name: Links
  type: string
- container: set
  name: accountGroups
  type: string
- container: ''
  name: active
  type: boolean
- container: set
  name: apps
  type: string
- container: set
  name: associatedMerchantAccounts
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: roles
  type: string
- container: ''
  name: timeZoneCode
  type: string
- container: ''
  name: username
  type: string
property_count: 9
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-company-user-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
