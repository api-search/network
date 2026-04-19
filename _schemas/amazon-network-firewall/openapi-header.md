---
description: The basic rule criteria for Network Firewall to use to inspect packet headers in stateful traffic flow inspection. Traffic flows that match the criteria are a match for the corresponding <a>StatefulRule</a>.
layout: schema
name: Header
properties_list:
- description: ''
  name: Protocol
  type: object
- description: ''
  name: Source
  type: object
- description: ''
  name: SourcePort
  type: object
- description: ''
  name: Direction
  type: object
- description: ''
  name: Destination
  type: object
- description: ''
  name: DestinationPort
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-header-schema.json
slug: openapi-header
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: Header
---
