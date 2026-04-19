---
description: Describes a lifecycle hook. A lifecycle hook lets you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.
layout: schema
name: LifecycleHook
properties_list:
- description: ''
  name: LifecycleHookName
  type: object
- description: ''
  name: AutoScalingGroupName
  type: object
- description: ''
  name: LifecycleTransition
  type: object
- description: ''
  name: NotificationTargetARN
  type: object
- description: ''
  name: RoleARN
  type: object
- description: ''
  name: NotificationMetadata
  type: object
- description: ''
  name: HeartbeatTimeout
  type: object
- description: ''
  name: GlobalTimeout
  type: object
- description: ''
  name: DefaultResult
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-lifecycle-hook-schema.json
slug: ec2-auto-scaling-lifecycle-hook
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: LifecycleHook
---
