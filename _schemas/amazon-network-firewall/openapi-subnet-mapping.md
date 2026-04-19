---
description: The ID for a subnet that you want to associate with the firewall. This is used with <a>CreateFirewall</a> and <a>AssociateSubnets</a>. Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.
layout: schema
name: SubnetMapping
properties_list:
- description: ''
  name: SubnetId
  type: object
- description: ''
  name: IPAddressType
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-subnet-mapping-schema.json
slug: openapi-subnet-mapping
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: SubnetMapping
---
