---
description: LogForwardingProfile schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: LogForwardingProfile
properties_list:
- description: Unique identifier of the profile.
  name: profile_id
  type: string
- description: Display name of the profile.
  name: name
  type: string
- description: Description of the profile's purpose.
  name: description
  type: string
- description: Log types included in this forwarding profile.
  name: log_types
  type: array
- description: Whether this profile is actively forwarding logs.
  name: enabled
  type: boolean
- description: Total number of configured destinations.
  name: destination_count
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-log-forwarding-profile-schema.json
slug: strata-logging-service-api-log-forwarding-profile
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: LogForwardingProfile
---
