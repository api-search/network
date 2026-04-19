---
description: Schema representing an Amazon Elastic File System, which provides a simple, serverless, set-and-forget elastic file system for use with AWS cloud services and on-premises resources.
layout: schema
name: Amazon EFS FileSystem
properties_list:
- description: The ID of the file system, assigned by Amazon EFS.
  name: FileSystemId
  type: string
- description: The Amazon Resource Name (ARN) of the EFS file system.
  name: FileSystemArn
  type: string
- description: The opaque string specified in the request to ensure idempotent creation.
  name: CreationToken
  type: string
- description: The AWS account that created the file system.
  name: OwnerId
  type: string
- description: The time that the file system was created, in seconds since epoch.
  name: CreationTime
  type: string
- description: The lifecycle phase of the file system.
  name: LifeCycleState
  type: string
- description: You can add tags to a file system, including a Name tag. If the file system has a Name tag, Amazon EFS returns the value in this field.
  name: Name
  type:
  - string
  - 'null'
- description: The current number of mount targets that the file system has.
  name: NumberOfMountTargets
  type: integer
- description: The latest known metered size (in bytes) of data stored in the file system.
  name: SizeInBytes
  type: object
- description: The performance mode of the file system.
  name: PerformanceMode
  type: string
- description: A Boolean value that, if true, indicates that the file system is encrypted.
  name: Encrypted
  type: boolean
- description: The ID of an AWS KMS key used to protect the encrypted file system.
  name: KmsKeyId
  type: string
- description: Displays the file system's throughput mode.
  name: ThroughputMode
  type: string
- description: The amount of provisioned throughput, measured in MiB/s, for the file system.
  name: ProvisionedThroughputInMibps
  type: number
- description: The unique and consistent identifier of the Availability Zone in which the file system is located.
  name: AvailabilityZoneId
  type:
  - string
  - 'null'
- description: Describes the AWS Availability Zone in which the file system is located.
  name: AvailabilityZoneName
  type:
  - string
  - 'null'
- description: The tags associated with the file system.
  name: Tags
  type: array
provider_name: Amazon EFS
provider_slug: amazon-efs
schema_file: json-schema/amazon-efs-filesystem-schema.json
slug: amazon-efs-filesystem
tags:
- Amazon Web Services
- AWS
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
title: Amazon EFS FileSystem
---
