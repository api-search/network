---
description: A Lake Formation data cells filter for row-level and column-level security.
layout: schema
name: DataCellsFilter
properties_list:
- description: The ID of the Data Catalog.
  name: TableCatalogId
  type: string
- description: A database in the Data Catalog.
  name: DatabaseName
  type: string
- description: The name of the table.
  name: TableName
  type: string
- description: The name given by the user to the data filter cell.
  name: Name
  type: string
- description: A list of column names.
  name: ColumnNames
  type: array
- description: A PartiQL predicate for row-level filtering.
  name: RowFilter
  type: object
provider_name: AWS Lake Formation
provider_slug: amazon-lakeformation
schema_file: json-schema/amazon-lakeformation-data-cells-filter-schema.json
slug: amazon-lakeformation-data-cells-filter
tags:
- Analytics
- AWS
- Data Lake
- Governance
title: DataCellsFilter
---
