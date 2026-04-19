---
description: GetNotificationConfigurationListResponse schema from Adyen API
layout: schema
name: GetNotificationConfigurationListResponse
properties_list:
- description: Details of the notification subscription configurations.
  name: configurations
  type: array
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-configurations-get-notification-configuration-list-response-schema.json
slug: notification-configurations-get-notification-configuration-list-response
tags:
- Payments
- Financial Services
- Fintech
title: GetNotificationConfigurationListResponse
---
