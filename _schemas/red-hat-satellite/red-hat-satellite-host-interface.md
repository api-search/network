---
description: A network interface associated with a host.
layout: schema
name: HostInterface
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: mac
  type: '[''string'', ''null'']'
- description: ''
  name: ip
  type: '[''string'', ''null'']'
- description: ''
  name: ip6
  type: '[''string'', ''null'']'
- description: ''
  name: type
  type: string
- description: ''
  name: name
  type: '[''string'', ''null'']'
- description: ''
  name: subnet_id
  type: '[''integer'', ''null'']'
- description: ''
  name: subnet6_id
  type: '[''integer'', ''null'']'
- description: ''
  name: domain_id
  type: '[''integer'', ''null'']'
- description: Device identifier (e.g., eth0, ens192).
  name: identifier
  type: '[''string'', ''null'']'
- description: ''
  name: managed
  type: boolean
- description: ''
  name: primary
  type: boolean
- description: ''
  name: provision
  type: boolean
- description: ''
  name: virtual
  type: boolean
- description: VLAN tag.
  name: tag
  type: '[''string'', ''null'']'
- description: Maximum transmission unit.
  name: mtu
  type: '[''integer'', ''null'']'
- description: Parent interface identifier.
  name: attached_to
  type: '[''string'', ''null'']'
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-host-interface-schema.json
slug: red-hat-satellite-host-interface
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: HostInterface
---
