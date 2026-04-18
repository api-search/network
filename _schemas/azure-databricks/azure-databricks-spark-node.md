---
description: ''
layout: schema
name: SparkNode
properties_list:
- description: Private IP address of the node
  name: private_ip
  type: string
- description: Public DNS name of the node
  name: public_dns
  type: string
- description: Unique identifier for the node
  name: node_id
  type: string
- description: Azure instance identifier
  name: instance_id
  type: string
- description: Start time of the node (epoch milliseconds)
  name: start_timestamp
  type: integer
- description: Private IP address of the host
  name: host_private_ip
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-spark-node-schema.json
slug: azure-databricks-spark-node
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: SparkNode
---
