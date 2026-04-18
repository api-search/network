---
description: A host managed by Red Hat Satellite.
layout: schema
name: Host
properties_list:
- description: The unique identifier of the host.
  name: id
  type: integer
- description: The fully qualified domain name of the host.
  name: name
  type: string
- description: The IP address of the host.
  name: ip
  type: string
- description: The MAC address of the primary interface.
  name: mac
  type: string
- description: The operating system name and version.
  name: operatingsystem_name
  type: string
- description: The Puppet environment name.
  name: environment_name
  type: string
- description: The host group name.
  name: hostgroup_name
  type: string
- description: The organization name.
  name: organization_name
  type: string
- description: The location name.
  name: location_name
  type: string
- description: The global host status (0=OK, 1=Warning, 2=Error).
  name: global_status
  type: integer
- description: Content-related attributes of the host.
  name: content_facet_attributes
  type: object
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-satellite-host-schema.json
slug: red-hat-satellite-host
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Host
---
