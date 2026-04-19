---
description: Cluster feature license
layout: schema
name: License
properties_list:
- description: License name
  name: name
  type: string
- description: License scope
  name: scope
  type: string
- description: License compliance state
  name: state
  type: string
- description: Individual license entries
  name: licenses
  type: array
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-license-schema.json
slug: netapp-ontap-license
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: License
---
