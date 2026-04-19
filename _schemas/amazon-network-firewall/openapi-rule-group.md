---
description: <p>The object that defines the rules in a rule group. This, along with <a>RuleGroupResponse</a>, define the rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>. </p> <p>Network Firewall uses a rule group to inspect and control network traffic. You define stateless rule groups to inspect individual packets and you define stateful rule groups to inspect packets in the context of their traffic flow. </p> <p>To use a rule group, you include it by reference in an Network Firewall firewall policy, then you use the policy in a firewall. You can reference a rule group from more than one firewall policy, and you can use a firewall policy in more than one firewall. </p>
layout: schema
name: RuleGroup
properties_list:
- description: ''
  name: RuleVariables
  type: object
- description: ''
  name: ReferenceSets
  type: object
- description: ''
  name: RulesSource
  type: object
- description: ''
  name: StatefulRuleOptions
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-rule-group-schema.json
slug: openapi-rule-group
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: RuleGroup
---
