---
description: The platform configuration for the instance. Includes settings for Secure Boot, measured boot, and trusted platform module.
layout: schema
name: PlatformConfig
properties_list:
- description: The type of platform configuration
  name: type
  type: string
- description: Whether Secure Boot is enabled on the instance
  name: isSecureBootEnabled
  type: boolean
- description: Whether the Trusted Platform Module (TPM) is enabled
  name: isTrustedPlatformModuleEnabled
  type: boolean
- description: Whether the Measured Boot feature is enabled
  name: isMeasuredBootEnabled
  type: boolean
- description: Whether AMD memory encryption is enabled
  name: isMemoryEncryptionEnabled
  type: boolean
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-platform-config-schema.json
slug: oci-compute-platform-config
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: PlatformConfig
---
