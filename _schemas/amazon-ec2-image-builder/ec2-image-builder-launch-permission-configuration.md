---
description: Describes the configuration for a launch permission. The launch permission modification request is sent to the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html">Amazon EC2 ModifyImageAttribute</a> API on behalf of the user for each Region they have selected to distribute the AMI. To make an AMI public, set the launch permission authorized accounts to <code>all</code>. See the examples for making an AMI public at <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html">Amazon EC2 ModifyImageAttribute</a>.
layout: schema
name: LaunchPermissionConfiguration
properties_list:
- description: ''
  name: userIds
  type: object
- description: ''
  name: userGroups
  type: object
- description: ''
  name: organizationArns
  type: object
- description: ''
  name: organizationalUnitArns
  type: object
provider_name: Amazon EC2 Image Builder
provider_slug: amazon-ec2-image-builder
schema_file: json-schema/ec2-image-builder-launch-permission-configuration-schema.json
slug: ec2-image-builder-launch-permission-configuration
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
title: LaunchPermissionConfiguration
---
