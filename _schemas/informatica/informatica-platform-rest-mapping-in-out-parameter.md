---
description: An in-out parameter defined within a mapping.
layout: schema
name: MappingInOutParameter
properties_list:
- description: The parameter ID.
  name: id
  type: integer
- description: The parameter name.
  name: name
  type: string
- description: A description of the parameter.
  name: description
  type: string
- description: The starting value for the parameter.
  name: initialValue
  type: string
- description: The data type of the parameter.
  name: datatype
  type: string
- description: The numeric precision.
  name: precision
  type: string
- description: The decimal scale.
  name: scale
  type: string
- description: The value retention policy.
  name: retentionPolicy
  type: string
- description: The method for determining the final value.
  name: aggregationType
  type: string
- description: The current parameter value.
  name: currentValue
  type: string
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-mapping-in-out-parameter-schema.json
slug: informatica-platform-rest-mapping-in-out-parameter
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
title: MappingInOutParameter
---
