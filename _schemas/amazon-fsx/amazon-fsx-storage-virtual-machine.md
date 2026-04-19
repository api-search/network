---
description: A storage virtual machine (SVM) in an Amazon FSx for NetApp ONTAP file system.
layout: schema
name: StorageVirtualMachine
properties_list:
- description: Active Directory configuration for the SVM.
  name: ActiveDirectoryConfiguration
  type: object
- description: ''
  name: CreationTime
  type: string
- description: Endpoints for accessing the SVM via different protocols.
  name: Endpoints
  type: object
- description: ''
  name: FileSystemId
  type: string
- description: ''
  name: Lifecycle
  type: string
- description: Name of the SVM.
  name: Name
  type: string
- description: ''
  name: ResourceARN
  type: string
- description: ''
  name: StorageVirtualMachineId
  type: string
- description: ''
  name: Subtype
  type: string
- description: ''
  name: Tags
  type: array
- description: ''
  name: UUID
  type: string
provider_name: Amazon FSx
provider_slug: amazon-fsx
schema_file: json-schema/amazon-fsx-storage-virtual-machine-schema.json
slug: amazon-fsx-storage-virtual-machine
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
title: StorageVirtualMachine
---
