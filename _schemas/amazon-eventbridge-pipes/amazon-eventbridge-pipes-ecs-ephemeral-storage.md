---
description: <p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/userguide/using_data_volumes.html">Fargate task storage</a> in the <i>Amazon ECS User Guide for Fargate</i>.</p> <note> <p>This parameter is only supported for tasks hosted on Fargate using Linux platform version <code>1.4.0</code> or later. This parameter is not supported for Windows containers on Fargate.</p> </note>
layout: schema
name: EcsEphemeralStorage
properties_list:
- description: ''
  name: sizeInGiB
  type: object
provider_name: Amazon EventBridge Pipes
provider_slug: amazon-eventbridge-pipes
schema_file: json-schema/amazon-eventbridge-pipes-ecs-ephemeral-storage-schema.json
slug: amazon-eventbridge-pipes-ecs-ephemeral-storage
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
title: EcsEphemeralStorage
---
