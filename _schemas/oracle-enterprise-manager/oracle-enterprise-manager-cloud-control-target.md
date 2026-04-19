---
description: Represents a monitored target in Enterprise Manager. A target is any managed entity such as a database, host, middleware instance, or application.
layout: schema
name: Target
properties_list:
- description: Unique identifier of the target.
  name: targetId
  type: string
- description: Display name of the target.
  name: targetName
  type: string
- description: The type of the target, defining its monitoring template and available metrics.
  name: targetType
  type: string
- description: Human-readable target type display name.
  name: targetDisplayType
  type: string
- description: The hostname where the target resides.
  name: hostName
  type: string
- description: Current lifecycle status of the target.
  name: lifecycleStatus
  type: string
- description: Current availability status reported by monitoring.
  name: availabilityStatus
  type: string
- description: URL of the management agent monitoring this target.
  name: agentUrl
  type: string
- description: Oracle home directory path, applicable to Oracle targets.
  name: oracleHome
  type: string
- description: Machine name where the target is deployed.
  name: machineName
  type: string
- description: Installation directory path for the target software.
  name: installLocation
  type: string
- description: Time zone of the target.
  name: timezone
  type: string
- description: Enterprise Manager user who owns this target.
  name: owner
  type: string
- description: Timestamp when the target was added to Enterprise Manager.
  name: timeCreated
  type: string
- description: Timestamp of the last target configuration update.
  name: timeUpdated
  type: string
- description: Additional target-type-specific configuration properties.
  name: properties
  type: object
- description: Canonical URI for this target resource.
  name: canonicalLink
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-target-schema.json
slug: oracle-enterprise-manager-cloud-control-target
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: Target
---
