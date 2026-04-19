---
description: Detailed datastore configuration and status
layout: schema
name: DatastoreInfo
properties_list:
- description: Display name of the datastore
  name: name
  type: string
- description: ''
  name: type
  type: string
- description: Whether the datastore is currently accessible
  name: accessible
  type: boolean
- description: Available free space in bytes
  name: free_space
  type: integer
- description: Maximum capacity in bytes
  name: capacity
  type: integer
- description: Whether thin provisioning is supported
  name: thin_provisioning_supported
  type: boolean
- description: Whether the datastore is accessible by multiple hosts
  name: multiple_host_access
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-datastore-info-schema.json
slug: vmware-vsphere-datastore-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: DatastoreInfo
---
