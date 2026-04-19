---
description: A user associated with the broker. For RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.
layout: schema
name: User
properties_list:
- description: ''
  name: ConsoleAccess
  type: object
- description: ''
  name: Groups
  type: object
- description: ''
  name: Password
  type: object
- description: ''
  name: Username
  type: object
provider_name: Amazon MQ
provider_slug: amazon-mq
schema_file: json-schema/mq-api-user-schema.json
slug: mq-api-user
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: User
---
