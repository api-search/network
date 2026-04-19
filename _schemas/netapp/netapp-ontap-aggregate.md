---
description: An aggregate (local tier) is a collection of physical disks that provides a pool of storage from which FlexVol volumes are provisioned.
layout: schema
name: Aggregate
properties_list:
- description: Aggregate UUID
  name: uuid
  type: string
- description: Aggregate name
  name: name
  type: string
- description: Aggregate operational state
  name: state
  type: string
- description: Aggregate space usage
  name: space
  type: object
- description: Block storage configuration
  name: block_storage
  type: object
- description: Aggregate encryption configuration
  name: data_encryption
  type: object
- description: FabricPool configuration
  name: cloud_storage
  type: object
- description: Time when the aggregate was created
  name: create_time
  type: string
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-aggregate-schema.json
slug: netapp-ontap-aggregate
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: Aggregate
---
