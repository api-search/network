---
description: TestNotificationConfigurationResponse schema from Adyen API
layout: schema
name: TestNotificationConfigurationResponse
properties_list:
- description: Any error messages encountered.
  name: errorMessages
  type: array
- description: 'The event types that were tested. >Permitted values: `ACCOUNT_HOLDER_CREATED`, `ACCOUNT_CREATED`, `ACCOUNT_UPDATED`, `ACCOUNT_HOLDER_UPDATED`, `ACCOUNT_HOLDER_STATUS_CHANGE`, `ACCOUNT_HOLDER_STORE_STA'
  name: eventTypes
  type: array
- description: The notification message and related response messages.
  name: exchangeMessages
  type: array
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The ID of the notification subscription configuration.
  name: notificationId
  type: integer
- description: A list of messages describing the testing steps.
  name: okMessages
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-configurations-test-notification-configuration-response-schema.json
slug: notification-configurations-test-notification-configuration-response
tags:
- Payments
- Financial Services
- Fintech
title: TestNotificationConfigurationResponse
---
