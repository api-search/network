---
description: Configure image tests for your pipeline build. Tests run after building the image, to verify that the AMI or container image is valid before distributing it.
layout: schema
name: ImageTestsConfiguration
properties_list:
- description: ''
  name: imageTestsEnabled
  type: object
- description: ''
  name: timeoutMinutes
  type: object
provider_name: Amazon EC2 Image Builder
provider_slug: amazon-ec2-image-builder
schema_file: json-schema/ec2-image-builder-image-tests-configuration-schema.json
slug: ec2-image-builder-image-tests-configuration
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
title: ImageTestsConfiguration
---
