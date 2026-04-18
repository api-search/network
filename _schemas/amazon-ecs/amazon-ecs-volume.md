---
description: ''
layout: schema
name: Volume
properties_list:
- description: The name of the volume (up to 255 characters).
  name: name
  type: string
- description: The contents of the host parameter determine whether your data volume persists on the host container instance.
  name: host
  type: object
- description: ''
  name: dockerVolumeConfiguration
  type: object
- description: ''
  name: efsVolumeConfiguration
  type: object
- description: ''
  name: fsxWindowsFileServerVolumeConfiguration
  type: object
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-volume-schema.json
slug: amazon-ecs-volume
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: Volume
---
