---
description: Summary of a datastore in the vCenter inventory
layout: schema
name: DatastoreSummary
properties_list:
- description: Unique identifier of the datastore (e.g., datastore-15)
  name: datastore
  type: string
- description: Display name of the datastore
  name: name
  type: string
- description: Type of the datastore
  name: type
  type: string
- description: Free space in bytes
  name: free_space
  type: integer
- description: Total capacity in bytes
  name: capacity
  type: integer
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-datastore-summary-schema.json
slug: vmware-vsphere-datastore-summary
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: DatastoreSummary
---
