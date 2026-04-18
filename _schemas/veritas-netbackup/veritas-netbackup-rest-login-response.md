---
description: ''
layout: schema
name: LoginResponse
properties_list:
- description: JSON Web Token for authenticating subsequent API requests
  name: token
  type: string
- description: The token type
  name: tokenType
  type: string
- description: Token validity period in seconds
  name: validity
  type: integer
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-login-response-schema.json
slug: veritas-netbackup-rest-login-response
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: LoginResponse
---
