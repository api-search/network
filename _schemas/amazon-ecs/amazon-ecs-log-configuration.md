---
description: ''
layout: schema
name: LogConfiguration
properties_list:
- description: The log driver to use for the container.
  name: logDriver
  type: string
- description: The configuration options to send to the log driver.
  name: options
  type: object
- description: The secrets to pass to the log driver configuration.
  name: secretOptions
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-log-configuration-schema.json
slug: amazon-ecs-log-configuration
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: LogConfiguration
---
