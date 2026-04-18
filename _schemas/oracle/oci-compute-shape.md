---
description: A compute shape that can be used to launch an instance. A shape determines the type of resources allocated, including CPUs, memory, and networking bandwidth.
layout: schema
name: Shape
properties_list:
- description: The name of the shape
  name: shape
  type: string
- description: The availability domain where the shape is available. Null if the shape is available across all availability domains.
  name: availabilityDomain
  type: string
- description: The default number of OCPUs available for this shape. For flexible shapes, this is the default when not specifying a custom value.
  name: ocpus
  type: number
- description: The default amount of memory available for this shape, in GB
  name: memoryInGBs
  type: number
- description: A short description of the processor
  name: processorDescription
  type: string
- description: The networking bandwidth available for this shape, in Gbps
  name: networkingBandwidthInGbps
  type: number
- description: The maximum number of VNICs that can be attached
  name: maxVnicAttachments
  type: integer
- description: The number of GPUs available for this shape
  name: gpus
  type: integer
- description: A short description of the GPU
  name: gpuDescription
  type: string
- description: The number of local disks available for this shape
  name: localDisks
  type: integer
- description: The aggregate size of local disks in GB
  name: localDisksTotalSizeInGBs
  type: number
- description: A short description of the local disks
  name: localDiskDescription
  type: string
- description: Whether the shape supports flexible OCPU and memory configuration
  name: isFlexible
  type: boolean
- description: Whether billing continues when the instance using this shape is stopped
  name: isBilledForStoppedInstance
  type: boolean
- description: The list of quota names associated with this shape
  name: quotaNames
  type: array
- description: The list of shapes recommended as alternatives
  name: recommendedAlternatives
  type: array
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-shape-schema.json
slug: oci-compute-shape
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: Shape
---
