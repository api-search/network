---
description: CreateVcnDetails schema from oracle-cloud-networking-openapi.yaml
layout: schema
name: CreateVcnDetails
properties_list:
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: List of CIDR blocks for the VCN.
  name: cidrBlocks
  type: array
- description: A user-friendly name.
  name: displayName
  type: string
- description: DNS label for the VCN.
  name: dnsLabel
  type: string
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/networking-create-vcn-details-schema.json
slug: networking-create-vcn-details
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: CreateVcnDetails
---
