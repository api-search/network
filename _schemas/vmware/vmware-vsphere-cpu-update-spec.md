---
description: Specification for CPU configuration
layout: schema
name: CpuUpdateSpec
properties_list:
- description: Number of virtual CPU cores
  name: count
  type: integer
- description: Number of cores per socket
  name: cores_per_socket
  type: integer
- description: ''
  name: hot_add_enabled
  type: boolean
- description: ''
  name: hot_remove_enabled
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-cpu-update-spec-schema.json
slug: vmware-vsphere-cpu-update-spec
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: CpuUpdateSpec
---
