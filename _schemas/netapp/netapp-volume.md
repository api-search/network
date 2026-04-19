---
description: Schema for a NetApp ONTAP storage volume. A volume is a logical container for data within a storage virtual machine (SVM), provisioned from an aggregate (local tier). Volumes support NAS (NFS/CIFS) and SAN (iSCSI/FCP) protocols and provide features such as snapshots, cloning, tiering, encryption, and quality of service.
layout: schema
name: NetApp ONTAP Volume
properties_list:
- description: Unique identifier for the volume, assigned by ONTAP upon creation
  name: uuid
  type: string
- description: Volume name, unique within the SVM. Must begin with a letter or underscore and contain only letters, digits, underscores, and hyphens.
  name: name
  type: string
- description: 'Volume type: rw (read-write, default), dp (data-protection for SnapMirror destinations), ls (load-sharing mirror)'
  name: type
  type: string
- description: Current operational state of the volume
  name: state
  type: string
- description: Volume style indicating the underlying architecture
  name: style
  type: string
- description: Total provisioned size of the volume in bytes
  name: size
  type: integer
- description: Optional comment or description for the volume
  name: comment
  type:
  - string
  - 'null'
- description: Language encoding setting for the volume, controlling character set and case-folding behavior
  name: language
  type: string
- description: Timestamp when the volume was created
  name: create_time
  type: string
- description: Storage virtual machine (SVM) that owns the volume
  name: svm
  type: object
- description: Aggregates hosting the volume. A FlexVol volume resides on a single aggregate; a FlexGroup volume can span multiple aggregates.
  name: aggregates
  type: array
- description: Space utilization and configuration for the volume
  name: space
  type: object
- description: NAS-specific configuration including junction path, security style, and export policy
  name: nas
  type: object
- description: Space guarantee configuration determining how space is reserved
  name: guarantee
  type: object
- description: Snapshot policy governing automatic snapshot creation and retention
  name: snapshot_policy
  type: object
- description: Quality of service settings controlling throughput and IOPS limits
  name: qos
  type: object
- description: FabricPool tiering policy controlling data movement to cloud storage
  name: tiering
  type: object
- description: Volume encryption configuration and state
  name: encryption
  type: object
- description: Volume autosize settings for automatic grow and shrink behavior
  name: autosize
  type: object
- description: Clone information if this volume is a FlexClone
  name: clone
  type: object
- description: ''
  name: _links
  type: object
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-volume-schema.json
slug: netapp-volume
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: NetApp ONTAP Volume
---
