---
description: A point-in-time copy of a volume
layout: schema
name: Snapshot
properties_list:
- description: Snapshot UUID
  name: uuid
  type: string
- description: Snapshot name
  name: name
  type: string
- description: Time when the snapshot was created
  name: create_time
  type: string
- description: Time when the snapshot expires and can be automatically deleted
  name: expiry_time
  type: string
- description: Optional comment for the snapshot
  name: comment
  type: string
- description: Amount of space consumed by the snapshot in bytes
  name: size
  type: integer
- description: Snapshot state
  name: state
  type: string
- description: SnapMirror label used for policy-based selection
  name: snapmirror_label
  type: string
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-snapshot-schema.json
slug: netapp-ontap-snapshot
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: Snapshot
---
