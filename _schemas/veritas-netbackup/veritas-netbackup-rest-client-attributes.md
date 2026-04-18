---
description: Attributes of a NetBackup client host
layout: schema
name: ClientAttributes
properties_list:
- description: Fully qualified hostname of the client
  name: hostName
  type: string
- description: Type of host in the NetBackup environment
  name: hostType
  type: string
- description: Operating system of the client
  name: os
  type: string
- description: Hardware platform of the client
  name: platform
  type: string
- description: NetBackup client software version
  name: version
  type: string
- description: SHA-256 fingerprint of the client certificate
  name: fingerprintSha256
  type: string
- description: Trust level established with the primary server
  name: trustLevel
  type: string
- description: Current communication status
  name: communicationStatus
  type: string
- description: Timestamp of the last successful communication
  name: lastConnectedTime
  type: string
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-client-attributes-schema.json
slug: veritas-netbackup-rest-client-attributes
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: ClientAttributes
---
