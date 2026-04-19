---
description: Parameters for creating a new host.
layout: schema
name: HostCreate
properties_list:
- description: Hostname or FQDN.
  name: name
  type: string
- description: Location identifier.
  name: location_id
  type: integer
- description: Organization identifier.
  name: organization_id
  type: integer
- description: IPv4 address (not required when using DHCP proxy).
  name: ip
  type: string
- description: MAC address (required for managed bare metal hosts).
  name: mac
  type: string
- description: Architecture identifier (required if managed).
  name: architecture_id
  type: integer
- description: Domain identifier (required if managed).
  name: domain_id
  type: integer
- description: Subnet identifier (required if managed).
  name: subnet_id
  type: integer
- description: Operating system identifier (required if managed).
  name: operatingsystem_id
  type: integer
- description: Installation medium identifier (required for non-image provisioning if managed).
  name: medium_id
  type: integer
- description: Partition table identifier (required if managed and no custom partition layout).
  name: ptable_id
  type: integer
- description: Compute resource identifier. Null indicates bare metal.
  name: compute_resource_id
  type: integer
- description: Compute profile identifier.
  name: compute_profile_id
  type: integer
- description: Host group identifier.
  name: hostgroup_id
  type: integer
- description: Root password (required if managed unless inherited).
  name: root_pass
  type: string
- description: Owner identifier.
  name: owner_id
  type: integer
- description: Owner type.
  name: owner_type
  type: string
- description: Enable build mode for provisioning.
  name: build
  type: boolean
- description: Whether the host should be managed by Satellite.
  name: managed
  type: boolean
- description: Additional information about the host.
  name: comment
  type: string
- description: ''
  name: content_facet_attributes
  type: object
- description: Network interface configurations.
  name: interfaces_attributes
  type: array
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-host-create-schema.json
slug: red-hat-satellite-host-create
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: HostCreate
---
