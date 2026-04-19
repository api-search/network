---
description: A parameter defined within a mapping.
layout: schema
name: MappingParameter
properties_list:
- description: The parameter identifier.
  name: id
  type: integer
- description: The parameter name.
  name: name
  type: string
- description: The parameter data type.
  name: type
  type: string
- description: A description of the parameter.
  name: description
  type: string
- description: The mapplet ID for mapplet-type parameters.
  name: customFuncId
  type: string
- description: Display configuration including connection type, logical connection, order, visibility, editability, and control type.
  name: uiProperties
  type: string
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-mapping-parameter-schema.json
slug: informatica-platform-rest-mapping-parameter
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
title: MappingParameter
---
