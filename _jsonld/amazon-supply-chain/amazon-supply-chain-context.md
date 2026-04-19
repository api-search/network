---
class_count: 8
classes:
- DataLakeDataset
- BillOfMaterialsImportJob
- Instance
- DataIntegrationEvent
- DataIntegrationFlow
- DataLakeNamespace
- name
- description
context_file: json-ld/amazon-supply-chain-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/json-ld/amazon-supply-chain-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Supply Chain from Amazon Supply Chain.
layout: jsonld
name: Amazon Supply Chain Context
namespaces:
- prefix: aws
  uri: https://amazonaws.com/schema/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: schema
  type: reference
- container: ''
  name: instanceId
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: partitionSpec
  type: reference
- container: ''
  name: createdTime
  type: dateTime
- container: ''
  name: lastModifiedTime
  type: dateTime
- container: ''
  name: jobId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: s3uri
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: instanceName
  type: string
- container: ''
  name: instanceDescription
  type: string
- container: ''
  name: instanceState
  type: string
- container: ''
  name: kmsKeyArn
  type: string
- container: ''
  name: webAppDnsDomain
  type: string
- container: ''
  name: eventId
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: eventGroupId
  type: string
- container: ''
  name: eventTimestamp
  type: dateTime
- container: ''
  name: data
  type: string
- container: set
  name: sources
  type: reference
- container: ''
  name: transformation
  type: reference
- container: ''
  name: target
  type: reference
property_count: 23
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
slug: amazon-supply-chain-context
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
- JSON-LD
- Linked Data
- Semantic Web
---
