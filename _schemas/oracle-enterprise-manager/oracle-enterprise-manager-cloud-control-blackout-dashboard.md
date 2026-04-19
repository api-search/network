---
description: Summary statistics for blackouts.
layout: schema
name: BlackoutDashboard
properties_list:
- description: Total number of blackouts.
  name: totalBlackouts
  type: integer
- description: Number of currently active blackouts.
  name: activeBlackouts
  type: integer
- description: Number of scheduled future blackouts.
  name: scheduledBlackouts
  type: integer
- description: Number of ended blackouts.
  name: endedBlackouts
  type: integer
- description: Total number of targets currently in blackout.
  name: targetsInBlackout
  type: integer
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-blackout-dashboard-schema.json
slug: oracle-enterprise-manager-cloud-control-blackout-dashboard
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: BlackoutDashboard
---
