---
description: Details for attaching a volume.
layout: schema
name: AttachVolumeDetails
properties_list:
- description: The OCID of the instance.
  name: instanceId
  type: string
- description: The OCID of the volume.
  name: volumeId
  type: string
- description: The type of volume attachment.
  name: type
  type: string
- description: A user-friendly name.
  name: displayName
  type: string
- description: Whether the attachment is read-only.
  name: isReadOnly
  type: boolean
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/compute-attach-volume-details-schema.json
slug: compute-attach-volume-details
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: AttachVolumeDetails
---
