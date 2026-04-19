---
description: Represents a copy of an entire cluster.
layout: schema
name: Snapshot
properties_list:
- description: The ARN of the snapshot.
  name: ARN
  type: string
- description: The configuration of the cluster from which the snapshot was taken.
  name: ClusterConfiguration
  type: object
- description: The ID of the KMS key used to encrypt the snapshot.
  name: KmsKeyId
  type: string
- description: The name of the snapshot.
  name: Name
  type: string
- description: The status of the snapshot.
  name: Status
  type: string
provider_name: Amazon MemoryDB
provider_slug: amazon-memorydb
schema_file: json-schema/memorydb-api-snapshot-schema.json
slug: memorydb-api-snapshot
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Snapshot
---
