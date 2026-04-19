---
description: An Amazon FSx fully managed file system (Lustre, Windows File Server, NetApp ONTAP, or OpenZFS).
layout: schema
name: FileSystem
properties_list:
- description: Unique identifier for the file system.
  name: FileSystemId
  type: string
- description: Type of the file system.
  name: FileSystemType
  type: string
- description: Current lifecycle state.
  name: Lifecycle
  type: string
- description: Storage capacity in GiB.
  name: StorageCapacity
  type: integer
- description: Type of storage media.
  name: StorageType
  type: string
- description: ID of the VPC containing the file system.
  name: VpcId
  type: string
- description: IDs of the subnets.
  name: SubnetIds
  type: array
- description: DNS name for the file system.
  name: DNSName
  type: string
- description: ID of the KMS key for encryption.
  name: KmsKeyId
  type: string
- description: ARN of the file system.
  name: ResourceARN
  type: string
- description: ''
  name: Tags
  type: array
- description: ''
  name: CreationTime
  type: string
- description: AWS account ID of the file system owner.
  name: OwnerId
  type: string
provider_name: Amazon FSx
provider_slug: amazon-fsx
schema_file: json-schema/amazon-fsx-file-system-schema.json
slug: amazon-fsx-file-system
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
title: FileSystem
---
