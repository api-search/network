---
description: CPU configuration of a virtual machine
layout: schema
name: CpuInfo
properties_list:
- description: Number of virtual CPU cores
  name: count
  type: integer
- description: Number of cores per CPU socket
  name: cores_per_socket
  type: integer
- description: Whether CPU hot-add is enabled
  name: hot_add_enabled
  type: boolean
- description: Whether CPU hot-remove is enabled
  name: hot_remove_enabled
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-cpu-info-schema.json
slug: vmware-vsphere-cpu-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: CpuInfo
---
