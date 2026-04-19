---
description: The properties for a private VPC Output When this property is specified, the output egress addresses will be created in a user specified VPC
layout: schema
name: VpcOutputSettings
properties_list:
- description: ''
  name: PublicAddressAllocationIds
  type: object
- description: ''
  name: SecurityGroupIds
  type: object
- description: ''
  name: SubnetIds
  type: object
provider_name: Amazon MediaLive
provider_slug: amazon-medialive
schema_file: json-schema/medialive-api-vpc-output-settings-schema.json
slug: medialive-api-vpc-output-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: VpcOutputSettings
---
