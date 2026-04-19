---
description: Schema for a monitored target in Oracle Enterprise Manager Cloud Control. A target represents any managed entity such as an Oracle Database, host server, middleware instance, application, or composite system monitored through the Enterprise Manager platform.
layout: schema
name: Oracle Enterprise Manager Target
properties_list:
- description: Unique identifier assigned by Enterprise Manager when the target is registered.
  name: targetId
  type: string
- description: Display name of the target. Must be unique within the combination of target name and target type.
  name: targetName
  type: string
- description: The type of the target, defining its monitoring template, available metrics, and configuration properties.
  name: targetType
  type: string
- description: Human-readable display name for the target type.
  name: targetDisplayType
  type: string
- description: Fully qualified hostname or IP address where the target resides.
  name: hostName
  type: string
- description: Current lifecycle management status of the target within Enterprise Manager.
  name: lifecycleStatus
  type: string
- description: Current availability status as reported by the monitoring agent. Indicates whether the target is reachable and operational.
  name: availabilityStatus
  type: string
- description: URL of the Oracle Management Agent responsible for monitoring this target.
  name: agentUrl
  type: string
- description: Oracle home directory path on the target host. Applicable to Oracle software targets such as databases and middleware.
  name: oracleHome
  type: string
- description: Machine name where the target is deployed, which may differ from the hostname.
  name: machineName
  type: string
- description: Installation directory path for the target software.
  name: installLocation
  type: string
- description: Time zone of the target in standard timezone identifier format.
  name: timezone
  type: string
- description: Enterprise Manager username that owns this target and is responsible for its management.
  name: owner
  type: string
- description: ISO 8601 timestamp when the target was first added to Enterprise Manager.
  name: timeCreated
  type: string
- description: ISO 8601 timestamp of the most recent target configuration change.
  name: timeUpdated
  type: string
- description: Target-type-specific configuration and instance properties. The available properties vary based on the target type. Common examples include SID, port, service name, and version.
  name: properties
  type: object
- description: Global target properties used for classification, grouping, and organizational metadata.
  name: globalProperties
  type: object
- description: List of associations linking this target to other targets, such as cluster membership or composite relationships.
  name: associations
  type: array
- description: Canonical REST API URI for accessing this target resource.
  name: canonicalLink
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-target-schema.json
slug: oracle-enterprise-manager-target
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: Oracle Enterprise Manager Target
---
