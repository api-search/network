---
description: ''
layout: schema
name: NotificationWebhook
properties_list:
- description: The URL for the webhook. The URL must use the https:// protocol.
  name: webhook_url
  type: string
- description: A template for the body of the HTTP request to send for the notification.
  name: webhook_body_template
  type: string
- description: A list of HTTP headers and values to include in the HTTP request for the webhook.
  name: webhook_headers
  type: object
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notification-integration-notification-webhook-schema.json
slug: notification-integration-notification-webhook
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NotificationWebhook
---
