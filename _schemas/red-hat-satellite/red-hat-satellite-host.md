---
description: A host registered with Red Hat Satellite representing a physical, virtual, or cloud system.
layout: schema
name: Host
properties_list:
- description: Unique identifier for the host.
  name: id
  type: integer
- description: Fully qualified domain name (FQDN) of the host.
  name: name
  type: string
- description: Primary IPv4 address of the host.
  name: ip
  type: '[''string'', ''null'']'
- description: Primary IPv6 address of the host.
  name: ip6
  type: '[''string'', ''null'']'
- description: Primary MAC address of the host.
  name: mac
  type: '[''string'', ''null'']'
- description: Puppet environment identifier.
  name: environment_id
  type: '[''integer'', ''null'']'
- description: Host group identifier.
  name: hostgroup_id
  type: '[''integer'', ''null'']'
- description: Host group name.
  name: hostgroup_name
  type: '[''string'', ''null'']'
- description: Full host group title including parent groups.
  name: hostgroup_title
  type: '[''string'', ''null'']'
- description: Operating system identifier.
  name: operatingsystem_id
  type: '[''integer'', ''null'']'
- description: Operating system name and version.
  name: operatingsystem_name
  type: '[''string'', ''null'']'
- description: Architecture identifier.
  name: architecture_id
  type: '[''integer'', ''null'']'
- description: Architecture name (e.g., x86_64).
  name: architecture_name
  type: '[''string'', ''null'']'
- description: DNS domain identifier.
  name: domain_id
  type: '[''integer'', ''null'']'
- description: DNS domain name.
  name: domain_name
  type: '[''string'', ''null'']'
- description: IPv4 subnet identifier.
  name: subnet_id
  type: '[''integer'', ''null'']'
- description: IPv4 subnet name.
  name: subnet_name
  type: '[''string'', ''null'']'
- description: IPv6 subnet identifier.
  name: subnet6_id
  type: '[''integer'', ''null'']'
- description: Compute resource identifier. Null for bare metal hosts.
  name: compute_resource_id
  type: '[''integer'', ''null'']'
- description: Compute resource name.
  name: compute_resource_name
  type: '[''string'', ''null'']'
- description: Compute profile identifier.
  name: compute_profile_id
  type: '[''integer'', ''null'']'
- description: Installation medium identifier.
  name: medium_id
  type: '[''integer'', ''null'']'
- description: Partition table identifier.
  name: ptable_id
  type: '[''integer'', ''null'']'
- description: Hardware model identifier.
  name: model_id
  type: '[''integer'', ''null'']'
- description: Hardware model name.
  name: model_name
  type: '[''string'', ''null'']'
- description: Location identifier.
  name: location_id
  type: integer
- description: Location name.
  name: location_name
  type: string
- description: Organization identifier.
  name: organization_id
  type: integer
- description: Organization name.
  name: organization_name
  type: string
- description: Owner identifier.
  name: owner_id
  type: '[''integer'', ''null'']'
- description: Owner type (User or Usergroup).
  name: owner_type
  type: '[''string'', ''null'']'
- description: Whether the host is managed by Satellite for provisioning and configuration.
  name: managed
  type: boolean
- description: Whether the host is in build mode.
  name: build
  type: boolean
- description: Whether configuration management reports are evaluated for this host.
  name: enabled
  type: boolean
- description: Additional information about the host.
  name: comment
  type: '[''string'', ''null'']'
- description: Unique identifier from compute resource.
  name: uuid
  type: '[''string'', ''null'']'
- description: Global status of the host (0=OK, 1=Warning, 2=Error).
  name: global_status
  type: integer
- description: Human-readable global status label.
  name: global_status_label
  type: string
- description: Content-related attributes from the Katello content facet.
  name: content_facet_attributes
  type: object
- description: Subscription-related attributes from the Katello subscription facet.
  name: subscription_facet_attributes
  type: object
- description: Network interfaces associated with the host.
  name: interfaces
  type: array
- description: ''
  name: puppetclasses
  type: array
- description: ''
  name: all_puppetclasses
  type: array
- description: Timestamp when the host was created.
  name: created_at
  type: string
- description: Timestamp when the host was last updated.
  name: updated_at
  type: string
- description: Timestamp when the host OS was installed.
  name: installed_at
  type: '[''string'', ''null'']'
- description: Timestamp of the last configuration management report.
  name: last_report
  type: '[''string'', ''null'']'
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-host-schema.json
slug: red-hat-satellite-host
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: Host
---
