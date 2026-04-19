---
description: Summary of an ESXi host in the vCenter inventory
layout: schema
name: HostSummary
properties_list:
- description: Unique identifier of the host (e.g., host-10)
  name: host
  type: string
- description: Display name or hostname of the ESXi host
  name: name
  type: string
- description: Connection state of the host
  name: connection_state
  type: string
- description: Power state of the host
  name: power_state
  type: string
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-host-summary-schema.json
slug: vmware-vsphere-host-summary
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: HostSummary
---
