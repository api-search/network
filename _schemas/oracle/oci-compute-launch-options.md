---
description: Options for tuning the compatibility and performance of VM shapes
layout: schema
name: LaunchOptions
properties_list:
- description: Emulation type for the boot volume. PARAVIRTUALIZED is recommended for best performance.
  name: bootVolumeType
  type: string
- description: Firmware used to boot the VM
  name: firmware
  type: string
- description: Emulation type for the physical network interface card (NIC). PARAVIRTUALIZED or VFIO is recommended.
  name: networkType
  type: string
- description: Emulation type for attached block volume data disks
  name: remoteDataVolumeType
  type: string
- description: Whether to enable in-transit encryption for the data volume's paravirtualized attachment
  name: isPvEncryptionInTransitEnabled
  type: boolean
- description: Whether to enable consistent volume naming
  name: isConsistentVolumeNamingEnabled
  type: boolean
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-launch-options-schema.json
slug: oci-compute-launch-options
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: LaunchOptions
---
