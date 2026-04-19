---
description: Request to update launch configuration
layout: schema
name: UpdateLaunchConfigurationRequest
properties_list:
- description: Source server ID
  name: sourceServerID
  type: string
- description: Configuration name
  name: name
  type: string
- description: Launch disposition
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
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-update-launch-configuration-request-schema.json
slug: application-migration-service-update-launch-configuration-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: UpdateLaunchConfigurationRequest
---
