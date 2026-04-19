---
description: Filters for describing source servers
layout: schema
name: DescribeSourceServersRequestFilters
properties_list:
- description: Filter by source server IDs
  name: sourceServerIDs
  type: array
- description: Filter by archived status
  name: isArchived
  type: boolean
- description: Filter by replication type
  name: replicationTypes
  type: array
- description: Filter by lifecycle states
  name: lifeCycleStates
  type: array
- description: Filter by application IDs
  name: applicationIDs
  type: array
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-describe-source-servers-request-filters-schema.json
slug: application-migration-service-describe-source-servers-request-filters
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: DescribeSourceServersRequestFilters
---
