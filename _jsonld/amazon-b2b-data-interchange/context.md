---
class_count: 36
classes:
- Profile
- profileId
- profileArn
- businessName
- phone
- email
- logging
- logGroupName
- Partnership
- partnershipId
- partnershipArn
- tradingPartnerId
- capabilities
- Capability
- capabilityId
- capabilityArn
- capabilityDirection
- configuration
- inputLocation
- outputLocation
- instructionsDocuments
- Transformer
- transformerId
- transformerArn
- mappingTemplate
- fileFormat
- ediType
- status
- S3Location
- bucketName
- key
- X12Details
- transactionSet
- version
- name
- description
context_file: json-ld/context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-b2b-data-interchange/refs/heads/main/json-ld/context.jsonld
description: JSON-LD context defining the semantic vocabulary for context from Amazon B2B Data Interchange.
layout: jsonld
name: context Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: b2bi
  uri: https://aws.amazon.com/b2b-data-interchange/vocab#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
property_count: 2
provider_name: Amazon B2B Data Interchange
provider_slug: amazon-b2b-data-interchange
slug: context
tags:
- EDI
- B2B
- Data Interchange
- Supply Chain
- Healthcare
- Financial Services
- Amazon Web Services
- AWS
- JSON-LD
- Linked Data
- Semantic Web
---
