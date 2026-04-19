---
description: Request body for creating a new target.
layout: schema
name: TargetCreateRequest
properties_list:
- description: Display name for the target.
  name: targetName
  type: string
- description: Target type identifier defining the monitoring template.
  name: targetType
  type: string
- description: The hostname where the target resides.
  name: hostName
  type: string
- description: Target-type-specific properties required for monitoring.
  name: properties
  type: object
- description: Monitoring credentials for the target.
  name: credentials
  type: object
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-target-create-request-schema.json
slug: oracle-enterprise-manager-cloud-control-target-create-request
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: TargetCreateRequest
---
