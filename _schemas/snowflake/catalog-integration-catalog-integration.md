---
description: Catalog integration
layout: schema
name: CatalogIntegration
properties_list:
- description: Name of the catalog integration.
  name: name
  type: string
- description: Table format of the catalog.
  name: table_format
  type: string
- description: whether this catalog integration is available to use for Iceberg tables.
  name: enabled
  type: boolean
- description: Comment.
  name: comment
  type: string
- description: Type of the integration. Always CATALOG.
  name: type
  type: string
- description: Category of the integration. Always CATALOG.
  name: category
  type: string
- description: Date and time when the catalog integration was created.
  name: created_on
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/catalog-integration-catalog-integration-schema.json
slug: catalog-integration-catalog-integration
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: CatalogIntegration
---
