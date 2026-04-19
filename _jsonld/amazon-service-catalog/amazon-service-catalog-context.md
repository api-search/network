---
class_count: 3
classes:
- Portfolio
- ProductViewSummary
- ProvisionedProduct
context_file: json-ld/amazon-service-catalog-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-service-catalog/refs/heads/main/json-ld/amazon-service-catalog-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Service Catalog from Amazon Service Catalog.
layout: jsonld
name: Amazon Service Catalog Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Id
  type: string
- container: ''
  name: ARN
  type: string
- container: ''
  name: DisplayName
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: CreatedTime
  type: dateTime
- container: ''
  name: ProviderName
  type: string
- container: ''
  name: ProductId
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Owner
  type: string
- container: ''
  name: ShortDescription
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: RecordDetail
  type: reference
property_count: 12
provider_name: Amazon Service Catalog
provider_slug: amazon-service-catalog
slug: amazon-service-catalog-context
tags:
- AWS
- Cloud Governance
- Compliance
- IT Governance
- Service Catalog
- JSON-LD
- Linked Data
- Semantic Web
---
