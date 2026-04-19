---
description: Defines the real-time status of a Snow device's data transfer while the device is at Amazon Web Services. This data is only available while a job has a <code>JobState</code> value of <code>InProgress</code>, for both import and export jobs.
layout: schema
name: DataTransfer
properties_list:
- description: ''
  name: BytesTransferred
  type: object
- description: ''
  name: ObjectsTransferred
  type: object
- description: ''
  name: TotalBytes
  type: object
- description: ''
  name: TotalObjects
  type: object
provider_name: Amazon Snow Family
provider_slug: amazon-snow-family
schema_file: json-schema/amazon-snow-family-data-transfer-schema.json
slug: amazon-snow-family-data-transfer
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
title: DataTransfer
---
