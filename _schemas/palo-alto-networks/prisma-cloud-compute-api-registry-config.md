---
description: RegistryConfig schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: RegistryConfig
properties_list:
- description: Registry type identifier.
  name: version
  type: string
- description: Registry URL or hostname.
  name: registry
  type: string
- description: Registry namespace or organization name.
  name: namespace
  type: string
- description: Credential store identifier for registry authentication.
  name: credentialID
  type: string
- description: Base OS for scanned images.
  name: os
  type: string
- description: Maximum number of images to scan from this registry.
  name: cap
  type: integer
- description: Number of scanner instances to use.
  name: scanners
  type: integer
- description: Specific tag to scan. Scans all tags if omitted.
  name: tag
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-registry-config-schema.json
slug: prisma-cloud-compute-api-registry-config
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: RegistryConfig
---
