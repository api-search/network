---
description: The identity configuration for the application pool worker process.
layout: schema
name: Identity
properties_list:
- description: The type of identity used by the application pool.
  name: identity_type
  type: string
- description: The username for the identity when using SpecificUser identity type.
  name: username
  type: string
- description: Whether to load the user profile for the worker process.
  name: load_user_profile
  type: boolean
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-identity-schema.json
slug: iis-administration-identity
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: Identity
---
