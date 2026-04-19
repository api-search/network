---
description: Parameters for creating or updating a host network interface.
layout: schema
name: HostInterfaceCreate
properties_list:
- description: Interface identifier (for updating existing interfaces).
  name: id
  type: integer
- description: MAC address.
  name: mac
  type: string
- description: IPv4 address.
  name: ip
  type: string
- description: IPv6 address.
  name: ip6
  type: string
- description: Interface type.
  name: type
  type: string
- description: DNS name.
  name: name
  type: string
- description: IPv4 subnet identifier.
  name: subnet_id
  type: integer
- description: IPv6 subnet identifier.
  name: subnet6_id
  type: integer
- description: Domain identifier.
  name: domain_id
  type: integer
- description: Device identifier (e.g., eth0).
  name: identifier
  type: string
- description: Whether DNS and DHCP are managed for this interface.
  name: managed
  type: boolean
- description: Whether this is the primary interface for FQDN.
  name: primary
  type: boolean
- description: Whether this interface is used for provisioning.
  name: provision
  type: boolean
- description: Whether this is a virtual interface (alias or VLAN).
  name: virtual
  type: boolean
- description: VLAN tag.
  name: tag
  type: string
- description: Maximum transmission unit.
  name: mtu
  type: integer
- description: Parent interface identifier.
  name: attached_to
  type: string
- description: BMC username (BMC interfaces only).
  name: username
  type: string
- description: BMC password (BMC interfaces only).
  name: password
  type: string
- description: BMC provider (BMC interfaces only).
  name: provider
  type: string
- description: Bond mode (bond interfaces only).
  name: mode
  type: string
- description: Slave or bridge member interface identifiers.
  name: attached_devices
  type: array
- description: Additional bond options (space-separated).
  name: bond_options
  type: string
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-host-interface-create-schema.json
slug: red-hat-satellite-host-interface-create
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: HostInterfaceCreate
---
