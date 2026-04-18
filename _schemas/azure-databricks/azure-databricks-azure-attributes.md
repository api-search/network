---
description: Attributes specific to Azure Databricks clusters
layout: schema
name: AzureAttributes
properties_list:
- description: The first nodes provisioned as on-demand instances. Remaining nodes will be spot instances.
  name: first_on_demand
  type: integer
- description: Azure availability type for cluster nodes
  name: availability
  type: string
- description: Max price for Azure spot instances. Set to -1 (default) to indicate that the instance should not be evicted based on price.
  name: spot_bid_max_price
  type: number
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-azure-attributes-schema.json
slug: azure-databricks-azure-attributes
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: AzureAttributes
---
