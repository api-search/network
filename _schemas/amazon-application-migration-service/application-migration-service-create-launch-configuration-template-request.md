---
description: Request to create a launch configuration template
layout: schema
name: CreateLaunchConfigurationTemplateRequest
properties_list:
- description: Default launch disposition
  name: launchDisposition
  type: string
- description: Right-sizing method
  name: targetInstanceTypeRightSizingMethod
  type: string
- description: copyPrivateIp
  name: copyPrivateIp
  type: boolean
- description: copyTags
  name: copyTags
  type: boolean
- description: licensing
  name: licensing
  type: string
- description: tags
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-create-launch-configuration-template-request-schema.json
slug: application-migration-service-create-launch-configuration-template-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: CreateLaunchConfigurationTemplateRequest
---
