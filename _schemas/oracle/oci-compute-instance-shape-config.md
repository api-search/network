---
description: The shape configuration for an instance. This includes the number of OCPUs, amount of memory, and networking bandwidth.
layout: schema
name: InstanceShapeConfig
properties_list:
- description: The total number of OCPUs available to the instance
  name: ocpus
  type: number
- description: The total amount of memory available to the instance, in gigabytes
  name: memoryInGBs
  type: number
- description: The baseline OCPU utilization for a subcore burstable instance
  name: baselineOcpuUtilization
  type: string
- description: A short description of the instance processor
  name: processorDescription
  type: string
- description: The networking bandwidth available to the instance, in Gbps
  name: networkingBandwidthInGbps
  type: number
- description: The maximum number of VNIC attachments for the instance
  name: maxVnicAttachments
  type: integer
- description: The number of GPUs available to the instance
  name: gpus
  type: integer
- description: A short description of the instance GPU
  name: gpuDescription
  type: string
- description: The number of local disks available to the instance
  name: localDisks
  type: integer
- description: The aggregate size of all local disks, in gigabytes
  name: localDisksTotalSizeInGBs
  type: number
- description: The total number of VCPUs available to the instance. This is typically 2x the number of OCPUs.
  name: vcpus
  type: integer
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-shape-config-schema.json
slug: oci-compute-instance-shape-config
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: InstanceShapeConfig
---
