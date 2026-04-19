---
description: Specification for creating a content library
layout: schema
name: LibraryCreateSpec
properties_list:
- description: Name for the new content library
  name: name
  type: string
- description: Description of the content library
  name: description
  type: string
- description: Library type
  name: type
  type: string
- description: Storage backings for the library content
  name: storage_backings
  type: array
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-library-create-spec-schema.json
slug: vmware-vsphere-library-create-spec
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: LibraryCreateSpec
---
