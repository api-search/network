---
description: Represents a data integration mapping definition that specifies data transformation logic between sources and targets.
layout: schema
name: Mapping
properties_list:
- description: The resource type identifier.
  name: '@type'
  type: string
- description: The unique identifier for the mapping.
  name: id
  type: string
- description: The organization ID that owns the mapping.
  name: orgId
  type: string
- description: The name of the mapping.
  name: name
  type: string
- description: A description of the mapping.
  name: description
  type: string
- description: The time the mapping was created.
  name: createTime
  type: string
- description: The time the mapping was last updated.
  name: updateTime
  type: string
- description: The user who created the mapping.
  name: createdBy
  type: string
- description: The user who last updated the mapping.
  name: updatedBy
  type: string
- description: The associated bundle ID if applicable.
  name: bundleObjectId
  type: string
- description: The associated bundle version.
  name: bundleVersion
  type: string
- description: The internal template identifier.
  name: templateId
  type: string
- description: The time the mapping was deployed.
  name: deployTime
  type: string
- description: Whether the mapping includes parameters.
  name: hasParameters
  type: boolean
- description: Whether the mapping is in a valid state.
  name: valid
  type: boolean
- description: Whether the mapping uses fixed connections.
  name: fixedConnection
  type: boolean
- description: Whether parameters are deployed.
  name: hasParametersDeployed
  type: boolean
- description: Whether fixed connections are deployed.
  name: fixedConnectionDeployed
  type: boolean
- description: The internal deployed template identifier.
  name: deployedTemplateId
  type: string
- description: The count of tasks using this mapping.
  name: tasks
  type: integer
- description: The collection of mapping parameters.
  name: parameters
  type: array
- description: The collection of in-out parameters.
  name: inOutParameters
  type: array
- description: References to related objects.
  name: references
  type: array
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-mapping-schema.json
slug: informatica-platform-rest-mapping
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: Mapping
---
