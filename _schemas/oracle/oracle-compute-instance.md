---
description: Schema for an Oracle Cloud Infrastructure compute instance. Defines the structure of a virtual machine or bare metal instance including its shape configuration, source image details, networking, lifecycle state, and metadata.
layout: schema
name: OCI Compute Instance
properties_list:
- description: The OCID of the instance. Oracle Cloud Identifier (OCID) is a unique identifier assigned to every OCI resource.
  name: id
  type: string
- description: The OCID of the compartment that contains the instance. Compartments are the primary building blocks for organizing cloud resources.
  name: compartmentId
  type: string
- description: The availability domain the instance is running in. An availability domain is one or more data centers within a region.
  name: availabilityDomain
  type: string
- description: The fault domain the instance is running in. Fault domains provide anti-affinity within an availability domain.
  name: faultDomain
  type: string
- description: A user-friendly name for the instance. Does not have to be unique and is changeable. Avoid entering confidential information.
  name: displayName
  type: string
- description: The shape of the instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.
  name: shape
  type: string
- description: ''
  name: shapeConfig
  type: object
- description: The region that contains the availability domain the instance is running in.
  name: region
  type: string
- description: Deprecated. Use sourceDetails instead. The OCID of the image used to boot the instance.
  name: imageId
  type: string
- description: ''
  name: sourceDetails
  type: object
- description: ''
  name: lifecycleState
  type: object
- description: The date and time the instance was created, in RFC 3339 format.
  name: timeCreated
  type: string
- description: Custom metadata key/value pairs provided for the instance. Common keys include ssh_authorized_keys for providing SSH public keys and user_data for cloud-init scripts (base64-encoded).
  name: metadata
  type: object
- description: Additional metadata key/value pairs that can contain nested JSON objects.
  name: extendedMetadata
  type: object
- description: Specifies the configuration mode for launching VM instances.
  name: launchMode
  type: string
- description: ''
  name: launchOptions
  type: object
- description: ''
  name: agentConfig
  type: object
- description: ''
  name: availabilityConfig
  type: object
- description: ''
  name: platformConfig
  type: object
- description: The date and time the instance is expected to be stopped or migrated for infrastructure maintenance, if applicable.
  name: timeMaintenanceRebootDue
  type: string
- description: The OCID of the compute capacity reservation this instance is launched under.
  name: capacityReservationId
  type: string
- description: The OCID of the dedicated virtual machine host the instance is placed on.
  name: dedicatedVmHostId
  type: string
- description: Whether the instance spans multiple NUMA nodes.
  name: isCrossNumaNode
  type: boolean
- description: ''
  name: definedTags
  type: object
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oracle-compute-instance-schema.json
slug: oracle-compute-instance
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: OCI Compute Instance
---
