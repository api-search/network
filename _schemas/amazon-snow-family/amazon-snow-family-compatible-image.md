---
description: A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including the ID and name for a Snow device AMI. This AMI is compatible with the device's physical hardware requirements, and it should be able to be run in an SBE1 instance on the device.
layout: schema
name: CompatibleImage
properties_list:
- description: ''
  name: AmiId
  type: object
- description: ''
  name: Name
  type: object
provider_name: Amazon Snow Family
provider_slug: amazon-snow-family
schema_file: json-schema/amazon-snow-family-compatible-image-schema.json
slug: amazon-snow-family-compatible-image
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
title: CompatibleImage
---
