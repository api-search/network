---
description: ''
layout: schema
name: NotificationQueueAzureEventGridOutbound
properties_list:
- description: Event Grid topic endpoint to which Snowpipe pushes notifications.
  name: azure_event_grid_topic_endpoint
  type: string
- description: ID of the Azure Active Directory tenant used for identity management.
  name: azure_tenant_id
  type: string
- description: URL to the Microsoft permissions request page.
  name: azure_consent_url
  type: string
- description: Name of the Snowflake client application created for your account.
  name: azure_multi_tenant_app_name
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notification-integration-notification-queue-azure-event-grid-outbound-schema.json
slug: notification-integration-notification-queue-azure-event-grid-outbound
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NotificationQueueAzureEventGridOutbound
---
