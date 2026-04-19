---
class_count: 9
classes:
- CreateDomainRequest
- CreateDomainResponse
- DescribeDomainsResponse
- DeleteDomainResponse
- DomainStatus
- DefineIndexFieldRequest
- DefineIndexFieldResponse
- DescribeIndexFieldsResponse
- IndexDocumentsResponse
context_file: json-ld/amazon-cloudsearch-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudsearch/refs/heads/main/json-ld/amazon-cloudsearch-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloudsearch from Amazon CloudSearch.
layout: jsonld
name: Amazon Cloudsearch Context
namespaces:
- prefix: cloudsearch
  uri: https://aws.amazon.com/cloudsearch/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: domainName
  type: string
- container: ''
  name: domainStatus
  type: string
- container: set
  name: domainStatusList
  type: string
- container: ''
  name: domainId
  type: string
- container: ''
  name: aRN
  type: string
- container: ''
  name: created
  type: boolean
- container: ''
  name: deleted
  type: boolean
- container: ''
  name: processing
  type: boolean
- container: ''
  name: requiresIndexDocuments
  type: boolean
- container: ''
  name: searchInstanceCount
  type: integer
- container: ''
  name: searchInstanceType
  type: string
- container: ''
  name: docService
  type: string
- container: ''
  name: searchService
  type: string
- container: ''
  name: indexField
  type: string
- container: set
  name: indexFields
  type: string
- container: set
  name: fieldNames
  type: string
property_count: 16
provider_name: Amazon CloudSearch
provider_slug: amazon-cloudsearch
slug: amazon-cloudsearch-context
tags:
- AWS
- CloudSearch
- Search
- Full-Text Search
- Managed
- JSON-LD
- Linked Data
- Semantic Web
---
