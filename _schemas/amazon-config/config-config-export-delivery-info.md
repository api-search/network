---
description: Provides status of the delivery of the snapshot or the configuration history to the specified Amazon S3 bucket. Also provides the status of notifications about the Amazon S3 delivery to the specified Amazon SNS topic.
layout: schema
name: ConfigExportDeliveryInfo
properties_list:
- description: ''
  name: lastStatus
  type: object
- description: ''
  name: lastErrorCode
  type: object
- description: ''
  name: lastErrorMessage
  type: object
- description: ''
  name: lastAttemptTime
  type: object
- description: ''
  name: lastSuccessfulTime
  type: object
- description: ''
  name: nextDeliveryTime
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-config-export-delivery-info-schema.json
slug: config-config-export-delivery-info
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: ConfigExportDeliveryInfo
---
