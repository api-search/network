---
description: An AWS License Manager license configuration.
layout: schema
name: LicenseConfiguration
properties_list:
- description: Unique ID of the license configuration.
  name: LicenseConfigurationId
  type: string
- description: Amazon Resource Name (ARN) of the license configuration.
  name: LicenseConfigurationArn
  type: string
- description: Name of the license configuration.
  name: Name
  type: string
- description: Dimension for which the licenses are counted.
  name: LicenseCountingType
  type: string
- description: Number of licenses managed by the license configuration.
  name: LicenseCount
  type: integer
- description: Number of available licenses as a hard limit.
  name: LicenseCountHardLimit
  type: boolean
- description: Number of licenses consumed by the license configuration.
  name: ConsumedLicenses
  type: integer
- description: Status of the license configuration.
  name: Status
  type: string
provider_name: Amazon License Manager
provider_slug: amazon-license-manager
schema_file: json-schema/amazon-license-manager-license-configuration-schema.json
slug: amazon-license-manager-license-configuration
tags:
- AWS
- Compliance
- Cost Management
- License Management
- Software Licensing
title: LicenseConfiguration
---
