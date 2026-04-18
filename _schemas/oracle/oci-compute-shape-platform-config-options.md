---
description: Platform configuration options available for the shape
layout: schema
name: ShapePlatformConfigOptions
properties_list:
- description: The type of platform configuration
  name: type
  type: string
- description: Whether Secure Boot is supported
  name: isSecureBootEnabled
  type: boolean
- description: Whether the Trusted Platform Module is supported
  name: isTrustedPlatformModuleEnabled
  type: boolean
- description: Whether Measured Boot is supported
  name: isMeasuredBootEnabled
  type: boolean
- description: Whether memory encryption is supported
  name: isMemoryEncryptionEnabled
  type: boolean
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-shape-platform-config-options-schema.json
slug: oci-compute-shape-platform-config-options
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: ShapePlatformConfigOptions
---
