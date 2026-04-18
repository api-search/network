---
description: Options for configuring networking bandwidth on a flexible shape
layout: schema
name: ShapeNetworkingBandwidthOptions
properties_list:
- description: The minimum networking bandwidth, in Gbps
  name: minInGbps
  type: number
- description: The maximum networking bandwidth, in Gbps
  name: maxInGbps
  type: number
- description: The default networking bandwidth per OCPU, in Gbps
  name: defaultPerOcpuInGbps
  type: number
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-shape-networking-bandwidth-options-schema.json
slug: oci-compute-shape-networking-bandwidth-options
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: ShapeNetworkingBandwidthOptions
---
