---
description: Clone dynamic table
layout: schema
name: DynamicTableClone
properties_list:
- description: Specifies the name for the dynamic table, must be unique for the schema in which the dynamic table is created
  name: name
  type: string
- description: Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table
  name: warehouse
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/dynamic-table-dynamic-table-clone-schema.json
slug: dynamic-table-dynamic-table-clone
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: DynamicTableClone
---
