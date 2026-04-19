---
description: DescribeJobTemplateResponse schema
layout: schema
name: DescribeJobTemplateResponse
properties_list:
- description: ''
  name: jobTemplateArn
  type: object
- description: ''
  name: jobTemplateId
  type: object
- description: ''
  name: description
  type: object
- description: ''
  name: documentSource
  type: object
- description: ''
  name: document
  type: object
- description: ''
  name: createdAt
  type: object
- description: Configuration for pre-signed S3 URLs.
  name: presignedUrlConfig
  type: object
- description: Allows you to create a staged rollout of a job.
  name: jobExecutionsRolloutConfig
  type: object
- description: The criteria that determine when and how a job abort takes place.
  name: abortConfig
  type: object
- description: Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to <code>IN_PROGRESS</code>. If the job execution status is not
  name: timeoutConfig
  type: object
- description: ''
  name: jobExecutionsRetryConfig
  type: object
- description: ''
  name: maintenanceWindows
  type: object
provider_name: Amazon IoT Device Management
provider_slug: amazon-iot-device-management
schema_file: json-schema/iot-device-management-describe-job-template-response-schema.json
slug: iot-device-management-describe-job-template-response
tags:
- AWS
- Device Management
- Fleet Management
- IoT
- OTA Updates
title: DescribeJobTemplateResponse
---
