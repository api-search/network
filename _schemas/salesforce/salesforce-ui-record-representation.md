---
description: A Salesforce record with field values and UI metadata
layout: schema
name: RecordRepresentation
properties_list:
- description: The 18-character Salesforce record ID
  name: id
  type: string
- description: The API name of the object type
  name: apiName
  type: string
- description: Child relationship data indexed by relationship name
  name: childRelationships
  type: object
- description: ETag for optimistic concurrency control
  name: eTag
  type: string
- description: Field values indexed by field API name
  name: fields
  type: object
- description: The record type ID
  name: recordTypeId
  type: string
- description: Record type metadata
  name: recordTypeInfo
  type: object
- description: ''
  name: systemModstamp
  type: string
- description: ''
  name: lastModifiedById
  type: string
- description: ''
  name: lastModifiedDate
  type: string
- description: ''
  name: createdById
  type: string
- description: ''
  name: createdDate
  type: string
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-ui-record-representation-schema.json
slug: salesforce-ui-record-representation
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
title: RecordRepresentation
---
