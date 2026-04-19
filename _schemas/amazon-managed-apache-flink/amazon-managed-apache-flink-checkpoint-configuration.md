---
description: Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance"> Checkpoints for Fault Tolerance</a> in the <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.8/">Apache Flink Documentation</a>.
layout: schema
name: CheckpointConfiguration
properties_list:
- description: ''
  name: ConfigurationType
  type: object
- description: ''
  name: CheckpointingEnabled
  type: object
- description: ''
  name: CheckpointInterval
  type: object
- description: ''
  name: MinPauseBetweenCheckpoints
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-checkpoint-configuration-schema.json
slug: amazon-managed-apache-flink-checkpoint-configuration
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: CheckpointConfiguration
---
