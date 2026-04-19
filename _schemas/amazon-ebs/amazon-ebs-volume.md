---
description: Schema representing an Amazon Elastic Block Store volume, which provides persistent block-level storage for use with Amazon EC2 instances.
layout: schema
name: Amazon EBS Volume
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
- description: The Amazon Resource Name (ARN) of the AWS KMS key that was used to protect the volume encryption key.
  name: kmsKeyId
  type: string
- description: The number of I/O operations per second (IOPS). For gp3, io1, and io2 volumes only.
  name: iops
  type: integer
- description: The throughput that the volume supports, in MiB/s. For gp3 volumes only.
  name: throughput
  type: integer
- description: The snapshot from which the volume was created, if applicable.
  name: snapshotId
  type: string
- description: Indicates whether Amazon EBS Multi-Attach is enabled. For io1 and io2 volumes only.
  name: multiAttachEnabled
  type: boolean
- description: Information about the volume attachments.
  name: attachments
  type: array
- description: Any tags assigned to the volume.
  name: tags
  type: array
provider_name: Amazon EBS
provider_slug: amazon-ebs
schema_file: json-schema/amazon-ebs-volume-schema.json
slug: amazon-ebs-volume
tags:
- Amazon Web Services
- AWS
- Block Storage
- EBS
- EC2
- Snapshots
- Storage
- Volumes
title: Amazon EBS Volume
---
