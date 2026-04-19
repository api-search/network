---
description: The channel through which Config delivers notifications and updated configuration states.
layout: schema
name: DeliveryChannel
properties_list:
- description: ''
  name: name
  type: object
- description: ''
  name: s3BucketName
  type: object
- description: ''
  name: s3KeyPrefix
  type: object
- description: ''
  name: s3KmsKeyArn
  type: object
- description: ''
  name: snsTopicARN
  type: object
- description: ''
  name: configSnapshotDeliveryProperties
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-delivery-channel-schema.json
slug: config-delivery-channel
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: DeliveryChannel
---
