---
description: Configuration for data quality validation. Used to select the Rulesets and Validation Mode to be used in the profile job. When ValidationConfiguration is null, the profile job will run without data quality validation.
layout: schema
name: ValidationConfiguration
properties_list:
- description: ''
  name: RulesetArn
  type: object
- description: ''
  name: ValidationMode
  type: object
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
schema_file: json-schema/glue-databrew-validation-configuration-schema.json
slug: glue-databrew-validation-configuration
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
title: ValidationConfiguration
---
