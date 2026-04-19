---
description: Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection. Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags.
layout: schema
name: MatchAttributes
properties_list:
- description: ''
  name: Sources
  type: object
- description: ''
  name: Destinations
  type: object
- description: ''
  name: SourcePorts
  type: object
- description: ''
  name: DestinationPorts
  type: object
- description: ''
  name: Protocols
  type: object
- description: ''
  name: TCPFlags
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-match-attributes-schema.json
slug: openapi-match-attributes
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: MatchAttributes
---
