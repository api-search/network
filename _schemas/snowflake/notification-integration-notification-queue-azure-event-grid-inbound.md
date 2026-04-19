---
description: ''
layout: schema
name: NotificationQueueAzureEventGridInbound
properties_list:
- description: the queue ID for the Azure Queue Storage queue created for Event Grid notifications.
  name: azure_storage_queue_primary_uri
  type: string
- description: the ID of the Azure Active Directory tenant used for identity management.
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
schema_file: json-schema/notification-integration-notification-queue-azure-event-grid-inbound-schema.json
slug: notification-integration-notification-queue-azure-event-grid-inbound
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NotificationQueueAzureEventGridInbound
---
