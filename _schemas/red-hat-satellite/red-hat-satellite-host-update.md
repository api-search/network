---
description: Parameters for updating an existing host.
layout: schema
name: HostUpdate
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: ip
  type: string
- description: ''
  name: mac
  type: string
- description: ''
  name: architecture_id
  type: integer
- description: ''
  name: domain_id
  type: integer
- description: ''
  name: subnet_id
  type: integer
- description: ''
  name: operatingsystem_id
  type: integer
- description: ''
  name: hostgroup_id
  type: integer
- description: ''
  name: location_id
  type: integer
- description: ''
  name: organization_id
  type: integer
- description: ''
  name: owner_id
  type: integer
- description: ''
  name: owner_type
  type: string
- description: ''
  name: build
  type: boolean
- description: ''
  name: managed
  type: boolean
- description: ''
  name: comment
  type: string
- description: ''
  name: content_facet_attributes
  type: object
- description: ''
  name: interfaces_attributes
  type: array
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-host-update-schema.json
slug: red-hat-satellite-host-update
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: HostUpdate
---
