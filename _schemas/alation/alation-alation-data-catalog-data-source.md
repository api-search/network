---
description: A data source connection configured in Alation
layout: schema
name: DataSource
properties_list:
- description: Unique identifier
  name: id
  type: integer
- description: Display title
  name: title
  type: string
- description: Data source description
  name: description
  type: string
- description: Database type
  name: dbtype
  type: string
- description: Database host
  name: host
  type: string
- description: Database port
  name: port
  type: integer
- description: Virtual data source flag
  name: is_virtual
  type: boolean
- description: Catalog URL
  name: url
  type: string
provider_name: Alation
provider_slug: alation
schema_file: json-schema/alation-alation-data-catalog-data-source-schema.json
slug: alation-alation-data-catalog-data-source
tags:
- Data Catalog
- Data Governance
- Data Intelligence
- Data Lineage
- Data Quality
- Business Glossary
- Metadata Management
- AI
title: DataSource
---
