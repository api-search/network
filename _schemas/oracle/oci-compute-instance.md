---
description: A compute instance is a virtual machine (VM) or bare metal host running in Oracle Cloud Infrastructure. It includes information about the shape, image, networking, and lifecycle state.
layout: schema
name: Instance
properties_list:
- description: The OCID of the instance
  name: id
  type: string
- description: The OCID of the compartment containing the instance
  name: compartmentId
  type: string
- description: The availability domain the instance is running in (e.g., Uocm:PHX-AD-1)
  name: availabilityDomain
  type: string
- description: The fault domain the instance is running in. A fault domain is a grouping of hardware and infrastructure within an availability domain.
  name: faultDomain
  type: string
- description: A user-friendly name. Does not have to be unique, and it is changeable. Avoid entering confidential information.
  name: displayName
  type: string
- description: The shape of the instance. The shape determines the number of CPUs, amount of memory, and other resources allocated.
  name: shape
  type: string
- description: The region that contains the availability domain the instance is running in
  name: region
  type: string
- description: Deprecated. Use sourceDetails instead. The OCID of the image used to boot the instance.
  name: imageId
  type: string
- description: The date and time the instance was created, in the format defined by RFC 3339.
  name: timeCreated
  type: string
- description: Custom metadata key/value pairs. The metadata can include ssh_authorized_keys and user_data for cloud-init.
  name: metadata
  type: object
- description: Additional metadata key/value pairs that can contain nested JSON objects.
  name: extendedMetadata
  type: object
- description: Specifies the configuration mode for launching VM instances.
  name: launchMode
  type: string
- description: The date and time the instance is expected to be stopped or migrated for infrastructure maintenance, if applicable.
  name: timeMaintenanceRebootDue
  type: string
- description: The OCID of the compute capacity reservation this instance is launched under, if applicable.
  name: capacityReservationId
  type: string
- description: The OCID of the dedicated virtual machine host that the instance is placed on, if applicable.
  name: dedicatedVmHostId
  type: string
- description: Whether the instance spans multiple NUMA nodes
  name: isCrossNumaNode
  type: boolean
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-schema.json
slug: oci-compute-instance
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: Instance
---
