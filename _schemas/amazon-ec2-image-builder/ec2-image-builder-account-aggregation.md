---
description: Contains counts of vulnerability findings from image scans that run when you create new Image Builder images, or build new versions of existing images. The vulnerability counts are grouped by severity level. The counts are aggregated across resources to create the final tally for the account that owns them.
layout: schema
name: AccountAggregation
properties_list:
- description: ''
  name: accountId
  type: object
- description: ''
  name: severityCounts
  type: object
provider_name: Amazon EC2 Image Builder
provider_slug: amazon-ec2-image-builder
schema_file: json-schema/ec2-image-builder-account-aggregation-schema.json
slug: ec2-image-builder-account-aggregation
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
title: AccountAggregation
---
