---
description: Configuration for profile jobs. Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.
layout: schema
name: ProfileConfiguration
properties_list:
- description: ''
  name: DatasetStatisticsConfiguration
  type: object
- description: ''
  name: ProfileColumns
  type: object
- description: ''
  name: ColumnStatisticsConfigurations
  type: object
- description: ''
  name: EntityDetectorConfiguration
  type: object
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
schema_file: json-schema/glue-databrew-profile-configuration-schema.json
slug: glue-databrew-profile-configuration
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
title: ProfileConfiguration
---
