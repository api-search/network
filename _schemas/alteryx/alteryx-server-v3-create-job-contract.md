---
description: Contract for creating a new execution job
layout: schema
name: CreateJobContract
properties_list:
- description: Worker tag for routing
  name: workerTag
  type: string
- description: Credential to use for execution
  name: credentialId
  type: string
- description: Analytic app question values
  name: questions
  type: array
- description: Job priority
  name: priority
  type: string
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-create-job-contract-schema.json
slug: alteryx-server-v3-create-job-contract
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: CreateJobContract
---
