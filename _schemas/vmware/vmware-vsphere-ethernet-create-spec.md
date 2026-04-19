---
description: Specification for creating a virtual network adapter
layout: schema
name: EthernetCreateSpec
properties_list:
- description: Adapter emulation type
  name: type
  type: string
- description: ''
  name: mac_type
  type: string
- description: MAC address (required when mac_type is MANUAL)
  name: mac_address
  type: string
- description: ''
  name: backing
  type: object
- description: ''
  name: start_connected
  type: boolean
- description: ''
  name: allow_guest_control
  type: boolean
- description: ''
  name: wake_on_lan_enabled
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-ethernet-create-spec-schema.json
slug: vmware-vsphere-ethernet-create-spec
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: EthernetCreateSpec
---
