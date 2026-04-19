---
description: Paginated collection of targets.
layout: schema
name: TargetCollection
properties_list:
- description: ''
  name: items
  type: array
- description: Total number of targets matching the query.
  name: totalCount
  type: integer
- description: Maximum items per page.
  name: limit
  type: integer
- description: Current offset in the result set.
  name: offset
  type: integer
- description: Whether more results are available.
  name: hasMore
  type: boolean
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-target-collection-schema.json
slug: oracle-enterprise-manager-cloud-control-target-collection
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: TargetCollection
---
