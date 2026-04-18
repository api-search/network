---
description: A virtual cloud network in Oracle Cloud Infrastructure.
layout: schema
name: Vcn
properties_list:
- description: The OCID of the VCN.
  name: id
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: A user-friendly name.
  name: displayName
  type: string
- description: The CIDR block of the VCN.
  name: cidrBlock
  type: string
- description: List of CIDR blocks.
  name: cidrBlocks
  type: array
- description: The OCID of the default DHCP options.
  name: defaultDhcpOptionsId
  type: string
- description: The OCID of the default route table.
  name: defaultRouteTableId
  type: string
- description: The OCID of the default security list.
  name: defaultSecurityListId
  type: string
- description: The DNS label for the VCN.
  name: dnsLabel
  type: string
- description: ''
  name: lifecycleState
  type: string
- description: ''
  name: timeCreated
  type: string
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/networking-vcn-schema.json
slug: networking-vcn
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Vcn
---
