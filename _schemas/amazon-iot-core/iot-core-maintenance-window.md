---
description: An optional configuration within the <code>SchedulingConfig</code> to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.
layout: schema
name: MaintenanceWindow
properties_list:
- description: ''
  name: startTime
  type: object
- description: ''
  name: durationInMinutes
  type: object
provider_name: Amazon IoT Core
provider_slug: amazon-iot-core
schema_file: json-schema/iot-core-maintenance-window-schema.json
slug: iot-core-maintenance-window
tags:
- AWS
- Device Management
- IoT
- MQTT
- Message Routing
title: MaintenanceWindow
---
