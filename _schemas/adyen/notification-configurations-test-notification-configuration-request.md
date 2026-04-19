---
description: TestNotificationConfigurationRequest schema from Adyen API
layout: schema
name: TestNotificationConfigurationRequest
properties_list:
- description: 'The event types to test. If left blank, then all of the configured event types will be tested. >Permitted values: `ACCOUNT_HOLDER_CREATED`, `ACCOUNT_CREATED`, `ACCOUNT_UPDATED`, `ACCOUNT_HOLDER_UPDATE'
  name: eventTypes
  type: array
- description: The ID of the notification subscription configuration to be tested.
  name: notificationId
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-configurations-test-notification-configuration-request-schema.json
slug: notification-configurations-test-notification-configuration-request
tags:
- Payments
- Financial Services
- Fintech
title: TestNotificationConfigurationRequest
---
