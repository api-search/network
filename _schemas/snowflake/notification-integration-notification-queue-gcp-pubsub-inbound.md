---
description: ''
layout: schema
name: NotificationQueueGcpPubsubInbound
properties_list:
- description: Pub/Sub topic subscription ID used to allow Snowflake access to event messages.
  name: gcp_pubsub_subscription_name
  type: string
- description: Google Cloud Platform (GCP) service account created for your account.
  name: gcp_pubsub_service_account
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notification-integration-notification-queue-gcp-pubsub-inbound-schema.json
slug: notification-integration-notification-queue-gcp-pubsub-inbound
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NotificationQueueGcpPubsubInbound
---
