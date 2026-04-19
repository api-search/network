---
description: Volume schema from Amazon EBS Amazon Elastic Block Store (EBS) API
layout: schema
name: Volume
properties_list:
- description: The ID of the volume.
  name: volumeId
  type: string
- description: The size of the volume, in GiBs.
  name: size
  type: integer
- description: The volume type.
  name: volumeType
  type: string
- description: The volume state.
  name: state
  type: string
- description: The Availability Zone for the volume.
  name: availabilityZone
  type: string
- description: The time stamp when volume creation was initiated.
  name: createTime
  type: string
- description: Indicates whether the volume is encrypted.
  name: encrypted
  type: boolean
- description: The Amazon Resource Name (ARN) of the KMS key.
  name: kmsKeyId
  type: string
- description: The number of I/O operations per second.
  name: iops
  type: integer
- description: The throughput that the volume supports, in MiB/s.
  name: throughput
  type: integer
- description: The snapshot from which the volume was created.
  name: snapshotId
  type: string
- description: Information about the volume attachments.
  name: attachments
  type: array
- description: Any tags assigned to the volume.
  name: tags
  type: array
provider_name: Amazon EBS
provider_slug: amazon-ebs
schema_file: json-schema/ebs-openapi-volume-schema.json
slug: ebs-openapi-volume
tags:
- Amazon Web Services
- AWS
- Block Storage
- EBS
- EC2
- Snapshots
- Storage
- Volumes
title: Volume
---
