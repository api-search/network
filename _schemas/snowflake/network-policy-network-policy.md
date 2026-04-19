---
description: A Snowflake network policy
layout: schema
name: NetworkPolicy
properties_list:
- description: Name of the network policy
  name: name
  type: string
- description: List of names of allowed network rules in a network policy
  name: allowed_network_rule_list
  type: array
- description: List of names of blocked network rules in a network policy
  name: blocked_network_rule_list
  type: array
- description: List of allowed IPs in a network policy
  name: allowed_ip_list
  type: array
- description: List of blocked IPs in a network policy
  name: blocked_ip_list
  type: array
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: Date and time when the network policy was created.
  name: created_on
  type: string
- description: Role that owns the network policy
  name: owner
  type: string
- description: The type of role that owns the network policy
  name: owner_role_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/network-policy-network-policy-schema.json
slug: network-policy-network-policy
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NetworkPolicy
---
