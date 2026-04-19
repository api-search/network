---
description: Detailed virtual disk configuration
layout: schema
name: DiskInfo
properties_list:
- description: Display label of the virtual disk
  name: label
  type: string
- description: Type of host bus adapter
  name: type
  type: string
- description: Capacity of the virtual disk in bytes
  name: capacity
  type: integer
- description: Disk backing information
  name: backing
  type: object
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-disk-info-schema.json
slug: vmware-vsphere-disk-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: DiskInfo
---
