---
description: ''
layout: schema
name: ClusterEvent
properties_list:
- description: Cluster ID associated with the event
  name: cluster_id
  type: string
- description: Timestamp of the event in epoch milliseconds
  name: timestamp
  type: integer
- description: Type of event
  name: type
  type: string
- description: Event-specific details
  name: details
  type: object
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-cluster-event-schema.json
slug: azure-databricks-cluster-event
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: ClusterEvent
---
