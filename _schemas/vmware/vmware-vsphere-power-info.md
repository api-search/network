---
description: Power state information for a virtual machine
layout: schema
name: PowerInfo
properties_list:
- description: Current power state
  name: state
  type: string
- description: Whether the last power-off was clean
  name: clean_power_off
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-power-info-schema.json
slug: vmware-vsphere-power-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: PowerInfo
---
