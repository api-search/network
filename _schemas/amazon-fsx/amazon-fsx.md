---
description: Represents an Amazon FSx file system with its associated configuration, state, and metadata.
layout: schema
name: Amazon FSx File System
properties_list:
- description: The unique identifier of the file system
  name: fileSystemId
  type: string
- description: The type of file system
  name: fileSystemType
  type: string
- description: The lifecycle status of the file system
  name: lifecycle
  type: string
- description: The storage capacity in GiB
  name: storageCapacity
  type: integer
- description: The storage type of the file system
  name: storageType
  type: string
- description: The ID of the VPC
  name: vpcId
  type: string
- description: The IDs of the subnets
  name: subnetIds
  type: array
- description: The DNS name for the file system
  name: dnsName
  type: string
- description: The AWS account that created the file system
  name: ownerId
  type: string
- description: The time the file system was created
  name: creationTime
  type: string
- description: Tags associated with the file system
  name: tags
  type: array
provider_name: Amazon FSx
provider_slug: amazon-fsx
schema_file: json-schema/amazon-fsx-schema.json
slug: amazon-fsx
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
title: Amazon FSx File System
---
