---
description: Describes an action for a listener or rule
layout: schema
name: Action
properties_list:
- description: The type of action
  name: type
  type: string
- description: The ARN of the target group for forward actions
  name: targetGroupArn
  type: string
- description: The order for the action
  name: order
  type: integer
- description: Configuration for redirect actions
  name: redirectConfig
  type: object
- description: Configuration for fixed-response actions
  name: fixedResponseConfig
  type: object
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
schema_file: json-schema/amazon-elastic-load-balancing-action-schema.json
slug: amazon-elastic-load-balancing-action
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
title: Action
---
