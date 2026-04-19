---
description: Virtual hardware configuration
layout: schema
name: HardwareInfo
properties_list:
- description: Virtual hardware version (e.g., VMX_21)
  name: version
  type: string
- description: Hardware upgrade policy
  name: upgrade_policy
  type: string
- description: Target hardware version for upgrade
  name: upgrade_version
  type: string
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-hardware-info-schema.json
slug: vmware-vsphere-hardware-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: HardwareInfo
---
