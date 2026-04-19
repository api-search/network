---
description: AuthorisationNotificationRequest schema from Adyen API
layout: schema
name: AuthorisationNotificationRequest
properties_list:
- description: Informs about the origin of the notification. The value is **true** when originating from the live environment, **false** for the test environment.
  name: live
  type: string
- description: A container object for the details included in the notification.
  name: notificationItems
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-authorisation-notification-request-schema.json
slug: webhooks-authorisation-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: AuthorisationNotificationRequest
---
