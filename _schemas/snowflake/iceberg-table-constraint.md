---
description: Constraints define integrity and consistency rules for data stored in tables.
layout: schema
name: Constraint
properties_list:
- description: Name of the Constraint
  name: name
  type: string
- description: ''
  name: column_names
  type: array
- description: Type of the constraint
  name: constraint_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-constraint-schema.json
slug: iceberg-table-constraint
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Constraint
---
