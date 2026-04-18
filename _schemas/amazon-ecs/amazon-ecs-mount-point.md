---
description: ''
layout: schema
name: MountPoint
properties_list:
- description: The name of the volume to mount.
  name: sourceVolume
  type: string
- description: The path on the container to mount the volume at.
  name: containerPath
  type: string
- description: If this value is true, the container has read-only access to the volume.
  name: readOnly
  type: boolean
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-mount-point-schema.json
slug: amazon-ecs-mount-point
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: MountPoint
---
