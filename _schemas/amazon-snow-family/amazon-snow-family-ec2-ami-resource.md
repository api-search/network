---
description: A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2-compatible AMI ID and the Snow device AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the Amazon Web Services Cloud and on the device.
layout: schema
name: Ec2AmiResource
properties_list:
- description: ''
  name: AmiId
  type: object
- description: ''
  name: SnowballAmiId
  type: object
provider_name: Amazon Snow Family
provider_slug: amazon-snow-family
schema_file: json-schema/amazon-snow-family-ec2-ami-resource-schema.json
slug: amazon-snow-family-ec2-ami-resource
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
title: Ec2AmiResource
---
