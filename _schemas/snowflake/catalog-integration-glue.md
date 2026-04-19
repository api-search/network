---
description: ''
layout: schema
name: Glue
properties_list:
- description: ARN for AWS role to assume
  name: glue_aws_role_arn
  type: string
- description: Glue catalog id
  name: glue_catalog_id
  type: string
- description: AWS region of the Glue catalog. Must be specified if the Snowflake account is not hosted on AWS.
  name: glue_region
  type: string
- description: default AWS Glue catalog namespace for all Iceberg table that use this catalog integration
  name: catalog_namespace
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/catalog-integration-glue-schema.json
slug: catalog-integration-glue
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Glue
---
