---
description: Binding between a content switching virtual server and a content switching policy. Defines how requests are evaluated and routed to target load balancing virtual servers.
layout: schema
name: CsVserverCsPolicyBinding
properties_list:
- description: Name of the content switching virtual server.
  name: name
  type: string
- description: Name of the content switching policy to bind.
  name: policyname
  type: string
- description: Name of the target load balancing virtual server to which matching traffic is directed.
  name: targetlbvserver
  type: string
- description: Priority of the policy binding. Lower values indicate higher priority.
  name: priority
  type: integer
- description: Expression specifying the priority of the next policy to evaluate if the current policy matches.
  name: gotopriorityexpression
  type: string
- description: The bind point at which the policy is bound.
  name: bindpoint
  type: string
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-cs-vserver-cs-policy-binding-schema.json
slug: citrix-netscaler-nitro-cs-vserver-cs-policy-binding
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: CsVserverCsPolicyBinding
---
