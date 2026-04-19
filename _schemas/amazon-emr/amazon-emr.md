---
description: Represents an Amazon EMR cluster with its associated configuration, state, and metadata.
layout: schema
name: Amazon EMR Cluster
properties_list:
- description: The unique identifier of the cluster
  name: id
  type: string
- description: The name of the cluster
  name: name
  type: string
- description: The current status of the cluster
  name: status
  type: object
- description: The Amazon EMR release label (e.g., emr-6.10.0)
  name: releaseLabel
  type: string
- description: The applications installed on the cluster
  name: applications
  type: array
- description: The instance collection type
  name: instanceCollectionType
  type: string
- description: The S3 path for log storage
  name: logUri
  type: string
- description: Whether the cluster auto-terminates after steps complete
  name: autoTerminate
  type: boolean
- description: Tags associated with the cluster
  name: tags
  type: array
provider_name: Amazon EMR
provider_slug: amazon-emr
schema_file: json-schema/amazon-emr-schema.json
slug: amazon-emr
tags:
- Amazon Web Services
- Analytics
- Apache Spark
- AWS
- Big Data
- Data Processing
- Hadoop
title: Amazon EMR Cluster
---
