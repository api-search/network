---
description: Operation result from a zone management command
layout: schema
name: Result
properties_list:
- description: Error code if the operation failed
  name: code
  type: string
- description: Human-readable error or status message
  name: message
  type: string
- description: Standard output from the zone administration command
  name: stdout
  type: string
- description: Standard error output from the zone administration command
  name: stderr
  type: string
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-result-schema.json
slug: solaris-rad-zonemgr-result
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
title: Result
---
