---
description: A set of rules governing the network accessibility.
layout: schema
name: NetworkRuleSet
properties_list:
- description: The default action when no rule matches.
  name: defaultAction
  type: string
- description: The list of IP address rules.
  name: ipRules
  type: array
- description: The list of virtual network rules.
  name: virtualNetworkRules
  type: array
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cognitive-services-network-rule-set-schema.json
slug: azure-cognitive-services-network-rule-set
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: NetworkRuleSet
---
