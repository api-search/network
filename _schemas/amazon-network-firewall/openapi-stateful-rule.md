---
description: A single Suricata rules specification, for use in a stateful rule group. Use this option to specify a simple Suricata rule with protocol, source and destination, ports, direction, and rule options. For information about the Suricata <code>Rules</code> format, see <a href="https://suricata.readthedocs.iorules/intro.html#">Rules Format</a>.
layout: schema
name: StatefulRule
properties_list:
- description: ''
  name: Action
  type: object
- description: ''
  name: Header
  type: object
- description: ''
  name: RuleOptions
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-stateful-rule-schema.json
slug: openapi-stateful-rule
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: StatefulRule
---
