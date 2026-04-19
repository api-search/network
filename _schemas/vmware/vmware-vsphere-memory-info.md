---
description: Memory configuration of a virtual machine
layout: schema
name: MemoryInfo
properties_list:
- description: Memory size in mebibytes
  name: size_MiB
  type: integer
- description: Whether memory hot-add is enabled
  name: hot_add_enabled
  type: boolean
- description: Granularity for memory hot-add in mebibytes
  name: hot_add_increment_size_MiB
  type: integer
- description: Maximum memory size for hot-add in mebibytes
  name: hot_add_limit_MiB
  type: integer
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-memory-info-schema.json
slug: vmware-vsphere-memory-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: MemoryInfo
---
