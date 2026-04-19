---
description: MountTarget schema from Amazon EFS Amazon Elastic File System (EFS) API
layout: schema
name: MountTarget
properties_list:
- description: System-assigned mount target ID.
  name: MountTargetId
  type: string
- description: The ID of the file system for which the mount target is intended.
  name: FileSystemId
  type: string
- description: The ID of the subnet.
  name: SubnetId
  type: string
- description: Lifecycle state of the mount target.
  name: LifeCycleState
  type: string
- description: Address at which the file system is mountable.
  name: IpAddress
  type: string
- description: The ID of the network interface.
  name: NetworkInterfaceId
  type: string
- description: The unique and consistent identifier of the Availability Zone.
  name: AvailabilityZoneId
  type: string
- description: The name of the Availability Zone.
  name: AvailabilityZoneName
  type: string
- description: The Virtual Private Cloud ID.
  name: VpcId
  type: string
provider_name: Amazon EFS
provider_slug: amazon-efs
schema_file: json-schema/efs-openapi-mount-target-schema.json
slug: efs-openapi-mount-target
tags:
- Amazon Web Services
- AWS
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
title: MountTarget
---
