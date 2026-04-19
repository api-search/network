---
description: An active user session
layout: schema
name: Session
properties_list:
- description: Unique session identifier
  name: id
  type: integer
- description: IP address of the session
  name: ip_address
  type: string
- description: Browser used for this session
  name: browser
  type: string
- description: Operating system used for this session
  name: operating_system
  type: string
- description: City from which the session originates
  name: city
  type: string
- description: State from which the session originates
  name: state
  type: string
- description: Country from which the session originates
  name: country
  type: string
- description: Type of credentials used
  name: credentials_type
  type: string
- description: Timestamp when the session was last extended
  name: extended_at
  type: string
- description: Number of times the session has been extended
  name: extended_count
  type: integer
- description: ID of the user being sudo'd as
  name: sudo_user_id
  type: integer
- description: Timestamp when the session was created
  name: created_at
  type: string
- description: Timestamp when the session expires
  name: expires_at
  type: string
- description: Relative URL
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-session-schema.json
slug: looker-session
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: Session
---
