---
description: ''
layout: schema
name: LoginRequest
properties_list:
- description: The authentication domain name (e.g., the NetBackup primary server hostname)
  name: domainName
  type: string
- description: The type of authentication domain
  name: domainType
  type: string
- description: The user account name
  name: userName
  type: string
- description: The user account password
  name: password
  type: string
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-login-request-schema.json
slug: veritas-netbackup-rest-login-request
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: LoginRequest
---
