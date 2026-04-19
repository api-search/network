---
description: Provides configuration status for a single policy or rule group that is used for a firewall endpoint. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. This is part of a <a>SyncState</a> for a firewall.
layout: schema
name: PerObjectStatus
properties_list:
- description: ''
  name: SyncStatus
  type: object
- description: ''
  name: UpdateToken
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-per-object-status-schema.json
slug: openapi-per-object-status
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: PerObjectStatus
---
