---
description: Specification for creating a new virtual machine
layout: schema
name: VMCreateSpec
properties_list:
- description: Display name for the new VM
  name: name
  type: string
- description: Guest operating system identifier
  name: guest_OS
  type: string
- description: Placement specification for the VM
  name: placement
  type: object
- description: Virtual hardware version
  name: hardware_version
  type: string
- description: Virtual disks to create with the VM
  name: disks
  type: array
- description: Network adapters to create with the VM
  name: nics
  type: array
- description: Boot configuration
  name: boot
  type: object
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-vm-create-spec-schema.json
slug: vmware-vsphere-vm-create-spec
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: VMCreateSpec
---
