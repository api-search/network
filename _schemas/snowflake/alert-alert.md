---
description: A Snowflake alert
layout: schema
name: Alert
properties_list:
- description: Name of the alert
  name: name
  type: string
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: The warehouse the alert runs in
  name: warehouse
  type: string
- description: The SQL statement that must be evaluated to determine whether to trigger the alert
  name: condition
  type: string
- description: The SQL statement to execute when the alert is triggered
  name: action
  type: string
- description: Date and time when the alert was created.
  name: created_on
  type: string
- description: Database in which the alert is stored
  name: database_name
  type: string
- description: Schema in which the alert is stored
  name: schema_name
  type: string
- description: Role that owns the alert
  name: owner
  type: string
- description: The type of role that owns the alert
  name: owner_role_type
  type: string
- description: The current state of the alert
  name: state
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/alert-alert-schema.json
slug: alert-alert
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Alert
---
