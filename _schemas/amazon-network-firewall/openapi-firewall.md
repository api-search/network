---
description: <p>The firewall defines the configuration settings for an Network Firewall firewall. These settings include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall Amazon Web Services resource. </p> <p>The status of the firewall, for example whether it's ready to filter network traffic, is provided in the corresponding <a>FirewallStatus</a>. You can retrieve both objects by calling <a>DescribeFirewall</a>.</p>
layout: schema
name: Firewall
properties_list:
- description: ''
  name: FirewallName
  type: object
- description: ''
  name: FirewallArn
  type: object
- description: ''
  name: FirewallPolicyArn
  type: object
- description: ''
  name: VpcId
  type: object
- description: ''
  name: SubnetMappings
  type: object
- description: ''
  name: DeleteProtection
  type: object
- description: ''
  name: SubnetChangeProtection
  type: object
- description: ''
  name: FirewallPolicyChangeProtection
  type: object
- description: ''
  name: Description
  type: object
- description: ''
  name: FirewallId
  type: object
- description: ''
  name: Tags
  type: object
- description: ''
  name: EncryptionConfiguration
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-firewall-schema.json
slug: openapi-firewall
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: Firewall
---
