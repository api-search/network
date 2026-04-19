---
description: Template for default launch configuration settings
layout: schema
name: LaunchConfigurationTemplate
properties_list:
- description: Template ID
  name: launchConfigurationTemplateID
  type: string
- description: ARN of the template
  name: arn
  type: string
- description: Default launch disposition
  name: launchDisposition
  type: string
- description: Right-sizing method
  name: targetInstanceTypeRightSizingMethod
  type: string
- description: Whether to copy private IP
  name: copyPrivateIp
  type: boolean
- description: Whether to copy tags
  name: copyTags
  type: boolean
- description: licensing
  name: licensing
  type: string
- description: Boot mode
  name: bootMode
  type: string
- description: Tags on the template
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-launch-configuration-template-schema.json
slug: application-migration-service-launch-configuration-template
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: LaunchConfigurationTemplate
---
