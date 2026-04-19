---
description: A database in the AWS Glue Data Catalog managed by Lake Formation.
layout: schema
name: Database
properties_list:
- description: The name of the database.
  name: Name
  type: string
- description: The ID of the Data Catalog.
  name: CatalogId
  type: string
- description: A description of the database.
  name: Description
  type: string
- description: The location of the database (for example, an HDFS path).
  name: LocationUri
  type: string
- description: The time at which the metadata database was created.
  name: CreateTime
  type: string
provider_name: AWS Lake Formation
provider_slug: amazon-lakeformation
schema_file: json-schema/amazon-lakeformation-database-schema.json
slug: amazon-lakeformation-database
tags:
- Analytics
- AWS
- Data Lake
- Governance
title: Database
---
