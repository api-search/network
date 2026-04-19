---
description: ''
layout: schema
name: AwsAttributes
properties_list:
- description: Number of on-demand instances to place first.
  name: first_on_demand
  type: integer
- description: ''
  name: availability
  type: string
- description: The availability zone identifier (e.g., us-west-2a).
  name: zone_id
  type: string
- description: IAM instance profile ARN for the cluster instances.
  name: instance_profile_arn
  type: string
- description: Max bid price as percentage of on-demand price.
  name: spot_bid_price_percent
  type: integer
- description: ''
  name: ebs_volume_type
  type: string
- description: ''
  name: ebs_volume_count
  type: integer
- description: ''
  name: ebs_volume_size
  type: integer
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-aws-attributes-schema.json
slug: databricks-aws-attributes
tags:
- AI
- Analytics
- Apache Spark
- Big Data
- Clean Rooms
- Cloud Computing
- Data
- Data Analytics
- Data Engineering
- Data Governance
- Delta Lake
- Delta Sharing
- ETL
- Identity Management
- Lakehouse
- Machine Learning
- MLflow
- Model Serving
- Security
- SQL
- Unity Catalog
- Vector Search
- Visualize
title: AwsAttributes
---
