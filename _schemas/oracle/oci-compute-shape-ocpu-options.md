---
description: Options for configuring OCPUs on a flexible shape
layout: schema
name: ShapeOcpuOptions
properties_list:
- description: The minimum number of OCPUs
  name: min
  type: number
- description: The maximum number of OCPUs
  name: max
  type: number
- description: The maximum number of OCPUs per NUMA node
  name: maxPerNumaNode
  type: number
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-shape-ocpu-options-schema.json
slug: oci-compute-shape-ocpu-options
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: ShapeOcpuOptions
---
