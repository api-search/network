---
description: Describes parameters for how a Flink-based Kinesis Data Analytics application executes multiple tasks simultaneously. For more information about parallelism, see <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/parallel.html">Parallel Execution</a> in the <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.8/">Apache Flink Documentation</a>.
layout: schema
name: ParallelismConfiguration
properties_list:
- description: ''
  name: ConfigurationType
  type: object
- description: ''
  name: Parallelism
  type: object
- description: ''
  name: ParallelismPerKPU
  type: object
- description: ''
  name: AutoScalingEnabled
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-parallelism-configuration-schema.json
slug: amazon-managed-apache-flink-parallelism-configuration
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: ParallelismConfiguration
---
