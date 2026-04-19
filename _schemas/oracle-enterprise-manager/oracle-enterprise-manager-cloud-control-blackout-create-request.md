---
description: Request body for creating a new blackout.
layout: schema
name: BlackoutCreateRequest
properties_list:
- description: Display name for the blackout.
  name: blackoutName
  type: string
- description: Description of the blackout purpose.
  name: description
  type: string
- description: Reason for the blackout.
  name: reason
  type: string
- description: List of targets to include in the blackout.
  name: targets
  type: array
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-blackout-create-request-schema.json
slug: oracle-enterprise-manager-cloud-control-blackout-create-request
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: BlackoutCreateRequest
---
