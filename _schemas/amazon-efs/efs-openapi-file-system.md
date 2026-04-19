---
description: FileSystem schema from Amazon EFS Amazon Elastic File System (EFS) API
layout: schema
name: FileSystem
properties_list:
- description: The ID of the file system.
  name: FileSystemId
  type: string
- description: The Amazon Resource Name (ARN) of the file system.
  name: FileSystemArn
  type: string
- description: The opaque string specified in the request.
  name: CreationToken
  type: string
- description: The AWS account that created the file system.
  name: OwnerId
  type: string
- description: The time that the file system was created.
  name: CreationTime
  type: string
- description: The lifecycle phase of the file system.
  name: LifeCycleState
  type: string
- description: The value of the Name tag if set.
  name: Name
  type: string
- description: The current number of mount targets that the file system has.
  name: NumberOfMountTargets
  type: integer
- description: The latest known metered size of data stored in the file system.
  name: SizeInBytes
  type: object
- description: The performance mode of the file system.
  name: PerformanceMode
  type: string
- description: A Boolean value that, if true, indicates that the file system is encrypted.
  name: Encrypted
  type: boolean
- description: The ID of the KMS key used for encryption.
  name: KmsKeyId
  type: string
- description: Displays the throughput mode for the file system.
  name: ThroughputMode
  type: string
- description: The amount of provisioned throughput, in MiB/s.
  name: ProvisionedThroughputInMibps
  type: number
- description: The tags associated with the file system.
  name: Tags
  type: array
provider_name: Amazon EFS
provider_slug: amazon-efs
schema_file: json-schema/efs-openapi-file-system-schema.json
slug: efs-openapi-file-system
tags:
- Amazon Web Services
- AWS
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
title: FileSystem
---
