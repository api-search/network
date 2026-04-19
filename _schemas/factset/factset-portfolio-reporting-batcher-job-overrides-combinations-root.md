---
description: Used for Vault job type only. This creates a matrix of given accounts and dates. When the job is run, it will only run for the accounts and dates within this object. (Settings will only be used temporarily and no changes will be made to the default PRB job.)
layout: schema
name: jobOverridesCombinationsRoot
properties_list:
- description: An array of accounts
  name: accounts
  type: array
- description: An array of dates
  name: dates
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-portfolio-reporting-batcher-job-overrides-combinations-root-schema.json
slug: factset-portfolio-reporting-batcher-job-overrides-combinations-root
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: jobOverridesCombinationsRoot
---
