---
description: A subnet in a virtual cloud network.
layout: schema
name: Subnet
properties_list:
- description: The OCID of the subnet.
  name: id
  type: string
- description: ''
  name: compartmentId
  type: string
- description: The OCID of the VCN.
  name: vcnId
  type: string
- description: ''
  name: displayName
  type: string
- description: The CIDR block of the subnet.
  name: cidrBlock
  type: string
- description: The availability domain.
  name: availabilityDomain
  type: string
- description: ''
  name: dnsLabel
  type: string
- description: Whether VNICs can have public IPs.
  name: prohibitPublicIpOnVnic
  type: boolean
- description: ''
  name: routeTableId
  type: string
- description: ''
  name: securityListIds
  type: array
- description: ''
  name: lifecycleState
  type: string
- description: ''
  name: timeCreated
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/networking-subnet-schema.json
slug: networking-subnet
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Subnet
---
