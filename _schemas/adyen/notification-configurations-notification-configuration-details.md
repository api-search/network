---
description: NotificationConfigurationDetails schema from Adyen API
layout: schema
name: NotificationConfigurationDetails
properties_list:
- description: Indicates whether the notification subscription is active.
  name: active
  type: boolean
- description: The version of the notification to which you are subscribing. To make sure that your integration can properly process the notification, subscribe to the same version as the API that you're using.
  name: apiVersion
  type: integer
- description: A description of the notification subscription configuration.
  name: description
  type: string
- description: Contains objects that define event types and their subscription settings.
  name: eventConfigs
  type: array
- description: A string with which to salt the notification(s) before hashing. If this field is provided, a hash value will be included under the notification header `HmacSignature` and the hash protocol will be inc
  name: hmacSignatureKey
  type: string
- description: Adyen-generated ID for the entry, returned in the response when you create a notification configuration. Required when updating an existing configuration using [`/updateNotificationConfiguration`](htt
  name: notificationId
  type: integer
- description: The password to use when accessing the notifyURL with the specified username.
  name: notifyPassword
  type: string
- description: The URL to which the notifications are to be sent.
  name: notifyURL
  type: string
- description: The username to use when accessing the notifyURL.
  name: notifyUsername
  type: string
- description: 'The SSL protocol employed by the endpoint. >Permitted values: `TLSv12`, `TLSv13`.'
  name: sslProtocol
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-configurations-notification-configuration-details-schema.json
slug: notification-configurations-notification-configuration-details
tags:
- Payments
- Financial Services
- Fintech
title: NotificationConfigurationDetails
---
