---
description: Detailed virtual machine configuration and state
layout: schema
name: VMInfo
properties_list:
- description: Display name of the virtual machine
  name: name
  type: string
- description: VM identity information
  name: identity
  type: object
- description: ''
  name: power_state
  type: string
- description: Configured guest operating system
  name: guest_OS
  type: string
- description: ''
  name: boot
  type: object
- description: Map of disk identifier to disk configuration
  name: disks
  type: object
- description: Map of NIC identifier to NIC configuration
  name: nics
  type: object
- description: Map of CD-ROM identifier to CD-ROM configuration
  name: cdroms
  type: object
- description: ''
  name: parallel_ports
  type: object
- description: ''
  name: serial_ports
  type: object
- description: ''
  name: floppy_drives
  type: object
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-vm-info-schema.json
slug: vmware-vsphere-vm-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: VMInfo
---
