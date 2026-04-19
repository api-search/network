---
class_count: 39
classes:
- SelectRequest
- InvalidNumberPredicates
- InvalidQueryExpression
- SelectResult
- MissingParameter
- AttributeDoesNotExist
- BatchPutAttributesRequest
- InvalidNumberValueTests
- ReplaceableItem
- Item
- InvalidParameterValue
- NumberSubmittedAttributesExceeded
- DuplicateItemName
- NumberDomainsExceeded
- DomainMetadataResult
- DeletableAttribute
- NoSuchDomain
- RequestTimeout
- PutAttributesRequest
- UpdateCondition
- CreateDomainRequest
- InvalidNextToken
- ListDomainsResult
- BatchDeleteAttributesRequest
- NumberDomainAttributesExceeded
- NumberItemAttributesExceeded
- DeleteDomainRequest
- ListDomainsRequest
- DeleteAttributesRequest
- NumberDomainBytesExceeded
- DomainMetadataRequest
- DeletableItem
- GetAttributesRequest
- ReplaceableAttribute
- NumberSubmittedItemsExceeded
- GetAttributesResult
- TooManyRequestedAttributes
- Attribute
- Name
context_file: json-ld/amazon-simpledb-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-simpledb/refs/heads/main/json-ld/amazon-simpledb-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Simpledb from Amazon SimpleDB.
layout: jsonld
name: Amazon Simpledb Context
namespaces:
- prefix: aws
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: SelectExpression
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: ConsistentRead
  type: string
- container: ''
  name: BoxUsage
  type: string
- container: ''
  name: Items
  type: string
- container: ''
  name: DomainName
  type: string
- container: ''
  name: Attributes
  type: string
- container: ''
  name: AlternateNameEncoding
  type: string
- container: ''
  name: ItemCount
  type: string
- container: ''
  name: ItemNamesSizeBytes
  type: string
- container: ''
  name: AttributeNameCount
  type: string
- container: ''
  name: AttributeNamesSizeBytes
  type: string
- container: ''
  name: AttributeValueCount
  type: string
- container: ''
  name: AttributeValuesSizeBytes
  type: string
- container: ''
  name: Timestamp
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: ItemName
  type: string
- container: ''
  name: Expected
  type: string
- container: ''
  name: Exists
  type: string
- container: ''
  name: DomainNames
  type: string
- container: ''
  name: MaxNumberOfDomains
  type: string
- container: ''
  name: AttributeNames
  type: string
- container: ''
  name: Replace
  type: string
- container: ''
  name: AlternateValueEncoding
  type: string
property_count: 24
provider_name: Amazon SimpleDB
provider_slug: amazon-simpledb
slug: amazon-simpledb-context
tags:
- AWS
- Cloud Storage
- Data Storage
- Database
- NoSQL
- JSON-LD
- Linked Data
- Semantic Web
---
