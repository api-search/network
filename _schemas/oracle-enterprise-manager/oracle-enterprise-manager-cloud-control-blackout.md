---
description: Represents a blackout (maintenance window) in Enterprise Manager. Blackouts suppress alerting and notifications for specified targets during scheduled maintenance periods.
layout: schema
name: Blackout
properties_list:
- description: Unique identifier of the blackout.
  name: blackoutId
  type: string
- description: Display name of the blackout.
  name: blackoutName
  type: string
- description: Description of the blackout purpose.
  name: description
  type: string
- description: Current status of the blackout.
  name: status
  type: string
- description: Reason for the blackout.
  name: reason
  type: string
- description: Username of the blackout creator.
  name: createdBy
  type: string
- description: List of targets included in the blackout.
  name: targets
  type: array
- description: Timestamp when the blackout was created.
  name: timeCreated
  type: string
- description: Timestamp of the last blackout update.
  name: timeUpdated
  type: string
- description: Canonical URI for this blackout resource.
  name: canonicalLink
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-blackout-schema.json
slug: oracle-enterprise-manager-cloud-control-blackout
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: Blackout
---
