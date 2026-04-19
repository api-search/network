---
description: A Snowflake cortex search service object.
layout: schema
name: CortexSearchService
properties_list:
- description: Specifies the name for the cortex search service, must be unique for the schema in which the cortex search service is created
  name: name
  type: string
- description: Specifies the name of the search column for the cortex search service.
  name: search_column
  type: string
- description: Specifies all columns included in the cortex search service and that can be returned in search queries.
  name: columns
  type: array
- description: Specifies the attribute columns, which can be referenced in filters in search queries to the cortex search service.
  name: attribute_columns
  type: array
- description: Specifies the name of the warehouse that provides the compute resources for refreshing the cortex search service
  name: warehouse
  type: string
- description: Specifies the definition (source query) used to create the cortex search service
  name: definition
  type: string
- description: Specifies a comment for the cortex search service
  name: comment
  type: string
- description: Date and time when the cortex search service was created.
  name: created_on
  type: string
- description: Database in which the cortex search service is stored
  name: database_name
  type: string
- description: Schema in which the cortex search service is stored
  name: schema_name
  type: string
- description: Number of rows in the materialized source data feeding into the cortex search service.
  name: source_data_num_rows
  type: integer
- description: Date and time as of which data existent in base tables is now serving.
  name: data_timestamp
  type: string
- description: Error encountered during the latest indexing pipeline of the cortex search service, if any.
  name: indexing_error
  type: string
- description: Size of the serving index, in bytes.
  name: serving_data_bytes
  type: integer
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-cortex-search-service-schema.json
slug: cortex-search-service-cortex-search-service
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: CortexSearchService
---
