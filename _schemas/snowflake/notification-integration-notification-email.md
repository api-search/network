---
description: ''
layout: schema
name: NotificationEmail
properties_list:
- description: A comma-separated list of quoted email addresses that can receive notification emails from this integration.
  name: allowed_recipients
  type: array
- description: A comma-separated list of default recipients for messages sent with this integration.
  name: default_recipients
  type: array
- description: the default subject line for messages sent with this integration.
  name: default_subject
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notification-integration-notification-email-schema.json
slug: notification-integration-notification-email
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NotificationEmail
---
