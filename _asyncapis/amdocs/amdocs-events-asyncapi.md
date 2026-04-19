---
channels:
- description: Published when a new customer account is created in the BSS system.
  name: customer/created
  operation: subscribe
  operation_id: onCustomerCreated
  summary: Customer account created
- description: Published when a customer account is modified.
  name: customer/updated
  operation: subscribe
  operation_id: onCustomerUpdated
  summary: Customer account updated
- description: Published when a service subscription becomes active.
  name: subscription/activated
  operation: subscribe
  operation_id: onSubscriptionActivated
  summary: Subscription activated
- description: Published when a service subscription is suspended.
  name: subscription/suspended
  operation: subscribe
  operation_id: onSubscriptionSuspended
  summary: Subscription suspended
- description: Published when a service subscription is cancelled.
  name: subscription/cancelled
  operation: subscribe
  operation_id: onSubscriptionCancelled
  summary: Subscription cancelled
- description: Published when a new invoice is generated for a customer.
  name: billing/invoice/created
  operation: subscribe
  operation_id: onInvoiceCreated
  summary: Invoice created
- description: Published when a payment is received against an invoice.
  name: billing/payment/received
  operation: subscribe
  operation_id: onPaymentReceived
  summary: Payment received
description: The Amdocs connectX BSS Event API delivers real-time event notifications for telecom BSS operations including customer lifecycle events, subscription changes, billing events, and provisioning status updates via webhooks and message queues.
layout: asyncapi
messages:
- description: ''
  name: CustomerCreatedEvent
  summary: Notification that a new customer account was created
  title: Customer Created
- description: ''
  name: CustomerUpdatedEvent
  summary: Notification that a customer account was modified
  title: Customer Updated
- description: ''
  name: SubscriptionEvent
  summary: Notification that a subscription status changed
  title: Subscription Status Changed
- description: ''
  name: InvoiceEvent
  summary: Notification that an invoice was generated
  title: Invoice Created
- description: ''
  name: PaymentEvent
  summary: Notification that a payment was recorded
  title: Payment Received
name: Amdocs connectX BSS Event API
provider_name: Amdocs
provider_slug: amdocs
servers:
- description: Amdocs BSS Production WebSocket event stream
  name: production
  protocol: wss
  url: wss://events.amdocs-dbs.com
slug: amdocs-events-asyncapi
spec_file: asyncapi/amdocs-events-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/asyncapi/amdocs-events-asyncapi.yml
tags:
- Telecom
- BSS
- OSS
- Billing
- Customer Management
- MVNO
- 5G
- SaaS
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
