---
description: Specification for creating a tag category
layout: schema
name: TagCategoryCreateSpec
properties_list:
- description: Name for the new category
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Cardinality of the category
  name: cardinality
  type: string
- description: Object types that can be tagged with tags in this category
  name: associable_types
  type: array
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-tag-category-create-spec-schema.json
slug: vmware-vsphere-tag-category-create-spec
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: TagCategoryCreateSpec
---
