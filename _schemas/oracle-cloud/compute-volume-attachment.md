---
description: A volume attached to a compute instance.
layout: schema
name: VolumeAttachment
properties_list:
- description: The OCID of the volume attachment.
  name: id
  type: string
- description: The OCID of the instance.
  name: instanceId
  type: string
- description: The OCID of the volume.
  name: volumeId
  type: string
- description: A user-friendly name.
  name: displayName
  type: string
- description: ''
  name: lifecycleState
  type: string
- description: ''
  name: timeCreated
  type: string
- description: The type of volume attachment.
  name: attachmentType
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/compute-volume-attachment-schema.json
slug: compute-volume-attachment
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: VolumeAttachment
---
