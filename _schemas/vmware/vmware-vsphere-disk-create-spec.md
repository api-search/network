---
description: Specification for creating a virtual disk
layout: schema
name: DiskCreateSpec
properties_list:
- description: Host bus adapter type
  name: type
  type: string
- description: Specification for a new VMDK file
  name: new_vmdk
  type: object
- description: Existing disk backing
  name: backing
  type: object
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-disk-create-spec-schema.json
slug: vmware-vsphere-disk-create-spec
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: DiskCreateSpec
---
