---
description: If this object is provided, the settings given here will override the default settings of the job for the job run (settings will only be used temporarily and no changes will be made to the default PRB job). Only certain objects can be used for certain job types.
layout: schema
name: jobOverrides
properties_list:
- description: An array of date account combinations
  name: combinations
  type: array
- description: Used only for jobs where type is ADF. If using dates override, please provide both start date and end date.
  name: dates
  type: object
- description: PUB
  name: runAsOfDate
  type: string
- description: The FactSet serial number which has the credentials wanted to run the job
  name: runAsSerialNumber
  type: string
- description: Used only for jobs where type is PA
  name: tasks
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-portfolio-reporting-batcher-job-overrides-schema.json
slug: factset-portfolio-reporting-batcher-job-overrides
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: jobOverrides
---
