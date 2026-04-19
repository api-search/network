---
class_count: 1
classes:
- Finding
context_file: json-ld/amazon-security-hub-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-security-hub/refs/heads/main/json-ld/amazon-security-hub-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Security Hub from Amazon Security Hub.
layout: jsonld
name: Amazon Security Hub Context
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
  name: SchemaVersion
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: ProductArn
  type: string
- container: ''
  name: GeneratorId
  type: string
- container: ''
  name: AwsAccountId
  type: string
- container: set
  name: Types
  type: string
- container: ''
  name: CreatedAt
  type: dateTime
- container: ''
  name: UpdatedAt
  type: dateTime
- container: ''
  name: Severity
  type: string
- container: ''
  name: Title
  type: string
- container: ''
  name: Description
  type: string
- container: set
  name: Resources
  type: string
- container: ''
  name: Compliance
  type: string
- container: ''
  name: Workflow
  type: string
- container: ''
  name: RecordState
  type: string
property_count: 15
provider_name: Amazon Security Hub
provider_slug: amazon-security-hub
slug: amazon-security-hub-context
tags:
- AWS
- Compliance
- Monitoring
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
