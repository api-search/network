---
description: Detailed virtual network adapter configuration
layout: schema
name: EthernetInfo
properties_list:
- description: Display label of the adapter
  name: label
  type: string
- description: Adapter emulation type
  name: type
  type: string
- description: MAC address type
  name: mac_type
  type: string
- description: MAC address of the adapter
  name: mac_address
  type: string
- description: Connection state
  name: state
  type: string
- description: Whether the adapter connects at power on
  name: start_connected
  type: boolean
- description: Network backing information
  name: backing
  type: object
- description: Whether guest OS can change adapter settings
  name: allow_guest_control
  type: boolean
- description: ''
  name: wake_on_lan_enabled
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-ethernet-info-schema.json
slug: vmware-vsphere-ethernet-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: EthernetInfo
---
