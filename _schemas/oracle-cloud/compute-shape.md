---
description: A compute shape defining the resources available for an instance.
layout: schema
name: Shape
properties_list:
- description: The name of the shape.
  name: shape
  type: string
- description: Description of the processor.
  name: processorDescription
  type: string
- description: Default number of OCPUs.
  name: ocpus
  type: number
- description: Default amount of memory in gigabytes.
  name: memoryInGBs
  type: number
- description: Number of GPUs.
  name: gpus
  type: integer
- description: Networking bandwidth in Gbps.
  name: networkingBandwidthInGbps
  type: number
- description: Whether the shape is flexible.
  name: isFlexible
  type: boolean
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/compute-shape-schema.json
slug: compute-shape
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Shape
---
