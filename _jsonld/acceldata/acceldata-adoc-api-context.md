---
class_count: 55
classes:
- schema
- Alert
- DataQualityRule
- Dataset
- LineageNode
- LineageGraph
- PipelineJob
- User
- Role
- id
- name
- description
- severity
- status
- message
- datasetId
- ruleId
- ruleType
- columnName
- threshold
- enabled
- databaseName
- schemaName
- dataSourceType
- rowCount
- columnCount
- qualityScore
- type
- platform
- database
- nodes
- edges
- rootNodeId
- sourceId
- targetId
- transformationType
- durationSeconds
- recordsProcessed
- username
- email
- firstName
- lastName
- active
- permissions
- total
- page
- pageSize
- alerts
- rules
- datasets
- jobs
- users
- roles
- code
- details
context_file: json-ld/acceldata-adoc-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/json-ld/acceldata-adoc-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acceldata Adoc Api from Acceldata.
layout: jsonld
name: Acceldata Adoc Api Context
namespaces:
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: adoc
  uri: https://acceldata.io/vocab/
properties:
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: lastProfiledAt
  type: dateTime
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: endTime
  type: dateTime
property_count: 5
provider_name: Acceldata
provider_slug: acceldata
slug: acceldata-adoc-api-context
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
- JSON-LD
- Linked Data
- Semantic Web
---
