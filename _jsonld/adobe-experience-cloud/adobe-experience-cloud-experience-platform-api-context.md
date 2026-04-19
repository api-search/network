---
class_count: 20
classes:
- DatasetInput
- SandboxList
- Batch
- QueryList
- SchemaInput
- Sandbox
- IdentityNamespace
- ClassList
- Schema
- SegmentDefinitionList
- IdentityNamespaceInput
- Dataset
- SchemaList
- SegmentDefinition
- SegmentDefinitionInput
- Query
- ProfileEntity
- name
- description
- version
context_file: json-ld/adobe-experience-cloud-experience-platform-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/json-ld/adobe-experience-cloud-experience-platform-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Experience Cloud Experience Platform Api from Adobe Experience Cloud.
layout: jsonld
name: Adobe Experience Cloud Experience Platform Api Context
namespaces:
- prefix: aec
  uri: https://developer.adobe.com/schema/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: schema
  type: reference
- container: ''
  name: schemaRef
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: contentType
  type: string
- container: set
  name: sandboxes
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: completed
  type: dateTime
- container: set
  name: queries
  type: string
- container: ''
  name: dbName
  type: string
- container: ''
  name: sql
  type: string
- container: ''
  name: updated
  type: dateTime
- container: ''
  name: rowCount
  type: integer
- container: ''
  name: Page
  type: reference
- container: ''
  name: totalCount
  type: integer
- container: set
  name: allOf
  type: string
- container: ''
  name: $ref
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: idType
  type: string
- container: ''
  name: standard
  type: boolean
- container: set
  name: results
  type: string
- container: ''
  name: meta:altId
  type: string
- container: set
  name: segments
  type: string
- container: ''
  name: expression
  type: reference
- container: ''
  name: value
  type: string
- container: ''
  name: mergePolicyId
  type: string
- container: ''
  name: evaluationInfo
  type: reference
- container: ''
  name: page
  type: reference
- container: ''
  name: fileDescription
  type: reference
- container: ''
  name: format
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: entity
  type: reference
- container: ''
  name: lastModifiedAt
  type: dateTime
property_count: 37
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
slug: adobe-experience-cloud-experience-platform-api-context
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
- JSON-LD
- Linked Data
- Semantic Web
---
