---
description: The platform configuration for launching an instance
layout: schema
name: LaunchInstancePlatformConfig
properties_list:
- description: The type of platform configuration
  name: type
  type: string
- description: Whether Secure Boot is enabled
  name: isSecureBootEnabled
  type: boolean
- description: Whether the Trusted Platform Module is enabled
  name: isTrustedPlatformModuleEnabled
  type: boolean
- description: Whether Measured Boot is enabled
  name: isMeasuredBootEnabled
  type: boolean
- description: Whether AMD memory encryption is enabled
  name: isMemoryEncryptionEnabled
  type: boolean
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-launch-instance-platform-config-schema.json
slug: oci-compute-launch-instance-platform-config
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: LaunchInstancePlatformConfig
---
