---
description: Attributes of a NetBackup backup image
layout: schema
name: ImageAttributes
properties_list:
- description: Unique identifier for the backup image
  name: backupId
  type: string
- description: Name of the policy that created this image
  name: policyName
  type: string
- description: Type of the policy
  name: policyType
  type: string
- description: Client hostname that was backed up
  name: clientName
  type: string
- description: Schedule name that triggered the backup
  name: scheduleName
  type: string
- description: Type of the schedule
  name: scheduleType
  type: string
- description: Timestamp when the backup was performed
  name: backupTime
  type: string
- description: Timestamp when the image will expire
  name: expirationTime
  type: string
- description: Total size of the backup image in kilobytes
  name: kilobytes
  type: integer
- description: Total number of files in the backup image
  name: numberOfFiles
  type: integer
- description: Primary copy number for the image
  name: primaryCopy
  type: integer
- description: Total number of copies of this image
  name: copyCount
  type: integer
- description: Media server that performed the backup
  name: mediaServer
  type: string
- description: Storage unit where the image is stored
  name: storageUnit
  type: string
- description: Media ID where the image resides
  name: mediaId
  type: string
- description: Whether the image data is compressed
  name: compressed
  type: boolean
- description: Whether the image data is encrypted
  name: encrypted
  type: boolean
- description: Whether the image is multiplexed
  name: multiplexed
  type: boolean
- description: Retention level assigned to the image
  name: retentionLevel
  type: integer
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-image-attributes-schema.json
slug: veritas-netbackup-rest-image-attributes
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: ImageAttributes
---
