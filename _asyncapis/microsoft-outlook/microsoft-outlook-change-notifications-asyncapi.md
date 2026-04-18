---
channels:
- description: Receives notifications when messages in the signed-in user's mailbox are created, updated, or deleted. Subscribe to this resource path via POST /subscriptions on the Microsoft Graph API.
  name: messageChanged
- description: Receives notifications when mail folders in the user's mailbox are created, updated, or deleted.
  name: mailFolderChanged
- description: Receives notifications when messages in a specific user's mailbox are created, updated, or deleted. Requires application permissions (Mail.Read) rather than delegated permissions.
  name: userMailChanged
- description: Receives lifecycle events for subscriptions including missed notifications, subscription removal, and reauthorization requirements. Configure via the lifecycleNotificationUrl property on the subscription.
  name: subscriptionLifecycle
description: AsyncAPI specification for Microsoft Graph change notifications (webhooks) for Outlook mail resources. Enables real-time event-driven architecture by subscribing to changes in messages, mail folders, contacts, and calendar events through the Microsoft Graph subscriptions API.
layout: asyncapi
messages:
- description: Microsoft Graph delivers change notifications in batches. Each HTTP POST to your notification URL contains a JSON payload with a value array of changeNotification objects. Your endpoint must respond with HTTP 202 Accepted within 3 seconds.
  name: ChangeNotificationCollection
  summary: A collection of one or more change notifications delivered as a batch to the webhook endpoint via HTTP POST.
  title: Change Notification Collection
- description: Lifecycle notifications inform the application about events like missed notifications, subscription removal due to policy, or reauthorization requirements. Delivered to the lifecycleNotificationUrl configured on the subscription.
  name: LifecycleNotification
  summary: A lifecycle notification indicating a subscription state change.
  title: Lifecycle Notification
- description: When a subscription is created, Microsoft Graph sends a POST request to the notificationUrl with a validationToken query parameter. The endpoint must respond with HTTP 200 and the validationToken value as plain text in the response body within 10 seconds.
  name: SubscriptionValidation
  summary: Validation request sent by Microsoft Graph when creating a new subscription to verify the notification URL.
  title: Subscription Validation Request
name: Microsoft Outlook Change Notifications
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
servers:
- description: Microsoft Graph v1.0 endpoint for creating and managing webhook subscriptions. Applications POST subscription requests to this server to register for change notifications.
  name: graphApi
  protocol: https
  url: ''
- description: The application-provided HTTPS endpoint that receives change notification payloads from Microsoft Graph. Must be publicly accessible and respond to validation requests.
  name: webhookEndpoint
  protocol: https
  url: ''
slug: microsoft-outlook-change-notifications-asyncapi
spec_file: asyncapi/microsoft-outlook-change-notifications-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/microsoft-outlook/refs/heads/main/asyncapi/microsoft-outlook-change-notifications-asyncapi.yml
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
