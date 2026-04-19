---
description: <p>The firewall policy defines the behavior of a firewall using a collection of stateless and stateful rule groups and other settings. You can use one firewall policy for multiple firewalls. </p> <p>This, along with <a>FirewallPolicyResponse</a>, define the policy. You can retrieve all objects for a firewall policy by calling <a>DescribeFirewallPolicy</a>.</p>
layout: schema
name: FirewallPolicy
properties_list:
- description: ''
  name: StatelessRuleGroupReferences
  type: object
- description: ''
  name: StatelessDefaultActions
  type: object
- description: ''
  name: StatelessFragmentDefaultActions
  type: object
- description: ''
  name: StatelessCustomActions
  type: object
- description: ''
  name: StatefulRuleGroupReferences
  type: object
- description: ''
  name: StatefulDefaultActions
  type: object
- description: ''
  name: StatefulEngineOptions
  type: object
- description: ''
  name: TLSInspectionConfigurationArn
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-firewall-policy-schema.json
slug: openapi-firewall-policy
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: FirewallPolicy
---
