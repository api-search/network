---
description: Schema for a virtual machine managed by VMware vCenter Server via the vSphere Automation REST API. Represents the full configuration and runtime state of a VM including hardware, guest OS, power state, and placement within the vSphere inventory hierarchy.
layout: schema
name: VMware vSphere Virtual Machine
properties_list:
- description: Unique identifier of the virtual machine assigned by vCenter Server (e.g., vm-123)
  name: vm
  type: string
- description: Display name of the virtual machine as shown in the vSphere inventory
  name: name
  type: string
- description: Current power state of the virtual machine
  name: power_state
  type: string
- description: Configured guest operating system identifier that determines default hardware settings and VMware Tools compatibility
  name: guest_OS
  type: string
- description: Unique identity attributes for the virtual machine
  name: identity
  type: object
- description: Virtual hardware configuration
  name: hardware
  type: object
- description: Virtual CPU configuration
  name: cpu
  type: object
- description: Virtual memory configuration
  name: memory
  type: object
- description: Boot configuration for the virtual machine
  name: boot
  type: object
- description: Map of virtual disk identifiers to disk configurations
  name: disks
  type: object
- description: Map of virtual network adapter identifiers to NIC configurations
  name: nics
  type: object
- description: Map of CD-ROM identifiers to CD-ROM configurations
  name: cdroms
  type: object
- description: Current placement of the virtual machine within the vSphere inventory
  name: placement
  type: object
- description: Guest operating system information reported by VMware Tools
  name: guest
  type: object
- description: Tags attached to this virtual machine for classification and organization
  name: tags
  type: array
- description: Storage consumption information
  name: storage
  type: object
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-virtual-machine-schema.json
slug: vmware-virtual-machine
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: VMware vSphere Virtual Machine
---
