---
description: A base object for all types of volume attachments. Represents the attachment between a compute instance and a block volume.
layout: schema
name: VolumeAttachment
properties_list:
- description: The OCID of the volume attachment
  name: id
  type: string
- description: The OCID of the instance the volume is attached to
  name: instanceId
  type: string
- description: The OCID of the volume
  name: volumeId
  type: string
- description: The OCID of the compartment
  name: compartmentId
  type: string
- description: The availability domain of an instance
  name: availabilityDomain
  type: string
- description: A user-friendly name for the attachment
  name: displayName
  type: string
- description: The device name (e.g., /dev/oracleoci/oraclevdb)
  name: device
  type: string
- description: The type of volume attachment
  name: attachmentType
  type: string
- description: The lifecycle state of the volume attachment
  name: lifecycleState
  type: string
- description: The date and time the volume was attached
  name: timeCreated
  type: string
- description: Whether the attachment was created in read-only mode
  name: isReadOnly
  type: boolean
- description: Whether the attachment should be created in shareable mode
  name: isShareable
  type: boolean
- description: Whether in-transit encryption is enabled for the attachment
  name: isPvEncryptionInTransitEnabled
  type: boolean
- description: Whether the attachment is multipath
  name: isMultipath
  type: boolean
- description: The iSCSI login state of the volume attachment
  name: iscsiLoginState
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-volume-attachment-schema.json
slug: oci-compute-volume-attachment
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: VolumeAttachment
---
