---
description: Describes a listener
layout: schema
name: Listener
properties_list:
- description: The Amazon Resource Name (ARN) of the listener
  name: listenerArn
  type: string
- description: The ARN of the load balancer
  name: loadBalancerArn
  type: string
- description: The port on which the load balancer is listening
  name: port
  type: integer
- description: The protocol for connections from clients to the load balancer
  name: protocol
  type: string
- description: The default SSL server certificate
  name: certificates
  type: array
- description: The security policy that defines supported protocols and ciphers
  name: sslPolicy
  type: string
- description: The default actions for the listener
  name: defaultActions
  type: array
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
schema_file: json-schema/amazon-elastic-load-balancing-listener-schema.json
slug: amazon-elastic-load-balancing-listener
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
title: Listener
---
