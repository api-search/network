---
description: Summary of a virtual machine in the vCenter inventory
layout: schema
name: VMSummary
properties_list:
- description: Unique identifier of the virtual machine (e.g., vm-123)
  name: vm
  type: string
- description: Display name of the virtual machine
  name: name
  type: string
- description: Current power state of the VM
  name: power_state
  type: string
- description: Number of virtual CPUs
  name: cpu_count
  type: integer
- description: Memory size in mebibytes
  name: memory_size_MiB
  type: integer
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-vm-summary-schema.json
slug: vmware-vsphere-vm-summary
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: VMSummary
---
