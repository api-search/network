---
description: A notification channel used to watch for resource changes.
layout: schema
name: Channel
properties_list:
- description: Identifies this as a notification channel.
  name: kind
  type: string
- description: A UUID or similar unique string that identifies this channel.
  name: id
  type: string
- description: An opaque value that identifies the watched resource.
  name: resourceId
  type: string
- description: A version-specific identifier for the watched resource.
  name: resourceUri
  type: string
- description: An arbitrary string delivered to the target address with each notification.
  name: token
  type: string
- description: Date and time of notification channel expiration, expressed in milliseconds since the epoch.
  name: expiration
  type: string
- description: The type of delivery mechanism used for this channel.
  name: type
  type: string
- description: The address where notifications are delivered for this channel.
  name: address
  type: string
- description: Additional parameters controlling delivery channel behavior.
  name: params
  type: object
- description: Whether the payload of each notification event is expected.
  name: payload
  type: boolean
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-channel-schema.json
slug: gcp-cloud-storage-json-channel
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Google Cloud
- Object Storage
- Storage
title: Channel
---
