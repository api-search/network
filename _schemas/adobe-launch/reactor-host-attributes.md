---
description: ''
layout: schema
name: HostAttributes
properties_list:
- description: The human-readable name of the host.
  name: name
  type: string
- description: The hosting type.
  name: type_of
  type: string
- description: The host URL for SFTP hosts.
  name: server
  type: string
- description: The server port for SFTP hosts.
  name: port
  type: integer
- description: The URL path suffix for SFTP hosts.
  name: path
  type: string
- description: The authentication username for SFTP hosts.
  name: username
  type: string
- description: The encrypted private key for SFTP hosts.
  name: encrypted_private_key
  type: string
- description: Whether to use file copying instead of symbolic links for SFTP hosts.
  name: skip_symlinks
  type: boolean
- description: The current status of the host.
  name: status
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/reactor-host-attributes-schema.json
slug: reactor-host-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: HostAttributes
---
