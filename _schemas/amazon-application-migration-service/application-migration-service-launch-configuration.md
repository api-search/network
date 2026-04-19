---
description: Launch configuration for a source server
layout: schema
name: LaunchConfiguration
properties_list:
- description: Source server ID
  name: sourceServerID
  type: string
- description: Configuration name
  name: name
  type: string
- description: EC2 launch template ID
  name: ec2LaunchTemplateID
  type: string
- description: Launch disposition for the instance
  name: launchDisposition
  type: string
- description: Right-sizing method for target instance type
  name: targetInstanceTypeRightSizingMethod
  type: string
- description: Whether to copy source server private IP to target
  name: copyPrivateIp
  type: boolean
- description: Whether to copy source server tags to target instance
  name: copyTags
  type: boolean
- description: licensing
  name: licensing
  type: string
- description: Boot mode for the target instance
  name: bootMode
  type: string
- description: postLaunchActions
  name: postLaunchActions
  type: string
- description: Whether to enable MAP auto-tagging
  name: enableMapAutoTagging
  type: boolean
- description: MAP auto-tagging MPE ID
  name: mapAutoTaggingMpeID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-launch-configuration-schema.json
slug: application-migration-service-launch-configuration
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: LaunchConfiguration
---
