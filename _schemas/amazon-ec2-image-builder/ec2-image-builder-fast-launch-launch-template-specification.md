---
description: <p>Identifies the launch template that the associated Windows AMI uses for launching an instance when faster launching is enabled.</p> <note> <p>You can specify either the <code>launchTemplateName</code> or the <code>launchTemplateId</code>, but not both.</p> </note>
layout: schema
name: FastLaunchLaunchTemplateSpecification
properties_list:
- description: ''
  name: launchTemplateId
  type: object
- description: ''
  name: launchTemplateName
  type: object
- description: ''
  name: launchTemplateVersion
  type: object
provider_name: Amazon EC2 Image Builder
provider_slug: amazon-ec2-image-builder
schema_file: json-schema/ec2-image-builder-fast-launch-launch-template-specification-schema.json
slug: ec2-image-builder-fast-launch-launch-template-specification
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
title: FastLaunchLaunchTemplateSpecification
---
