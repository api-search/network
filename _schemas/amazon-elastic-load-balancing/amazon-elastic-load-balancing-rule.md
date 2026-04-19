---
description: Describes a rule
layout: schema
name: Rule
properties_list:
- description: The Amazon Resource Name (ARN) of the rule
  name: ruleArn
  type: string
- description: The priority of the rule
  name: priority
  type: string
- description: The conditions for the rule
  name: conditions
  type: array
- description: The actions for the rule
  name: actions
  type: array
- description: Whether this is the default rule
  name: isDefault
  type: boolean
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
schema_file: json-schema/amazon-elastic-load-balancing-rule-schema.json
slug: amazon-elastic-load-balancing-rule
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
title: Rule
---
