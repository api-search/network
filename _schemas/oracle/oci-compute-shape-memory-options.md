---
description: Options for configuring memory on a flexible shape
layout: schema
name: ShapeMemoryOptions
properties_list:
- description: The minimum amount of memory, in GB
  name: minInGBs
  type: number
- description: The maximum amount of memory, in GB
  name: maxInGBs
  type: number
- description: The default amount of memory per OCPU, in GB
  name: defaultPerOcpuInGBs
  type: number
- description: The minimum amount of memory per OCPU, in GB
  name: minPerOcpuInGBs
  type: number
- description: The maximum amount of memory per OCPU, in GB
  name: maxPerOcpuInGBs
  type: number
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-shape-memory-options-schema.json
slug: oci-compute-shape-memory-options
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: ShapeMemoryOptions
---
