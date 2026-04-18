---
description: ''
layout: schema
name: GitSource
properties_list:
- description: URL of the Git repository
  name: git_url
  type: string
- description: Git provider type
  name: git_provider
  type: string
- description: Branch to check out
  name: git_branch
  type: string
- description: Tag to check out
  name: git_tag
  type: string
- description: Commit hash to check out
  name: git_commit
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-git-source-schema.json
slug: azure-databricks-git-source
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: GitSource
---
