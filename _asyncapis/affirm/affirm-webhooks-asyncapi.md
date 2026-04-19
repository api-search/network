---
channels:
- description: Channel for Affirm checkout lifecycle events. Affirm sends POST requests with content-type application/x-www-form-urlencoded to the merchant's configured webhook endpoint as customers progress through the checkout flow.
  name: /webhooks/checkout
  operation: publish
  operation_id: receiveCheckoutEvent
  summary: Receive a checkout event
- description: Channel for Affirm prequalification events. Affirm sends POST requests with content-type application/json to the merchant's configured webhook endpoint as customers complete or expire from the prequalification flow.
  name: /webhooks/prequal
  operation: publish
  operation_id: receivePrequalEvent
  summary: Receive a prequalification event
description: 'Affirm uses webhooks to notify merchant endpoints in real time when events occur during the customer checkout and prequalification flows. Webhooks are available to Key and Enterprise merchants. Affirm sends two types of webhooks: checkout events delivered as application/x-www-form-urlencoded and prequalification events delivered as application/json. Checkout events fire as customers move through the Affirm financing flow, including opened, approved, not_approved, and confirmed status transitions. Prequalification events fire during the Affirm prequal flow, indicating approval decisions and expiry. Each webhook request includes an X-Affirm-Signature header containing a Base64-encoded HMAC signature that merchants can use to verify the request originated from Affirm. Merchant webhook endpoints must support TLS 1.2 and respond with a 2xx status code to acknowledge receipt. Affirm does not retry failed webhook deliveries.'
layout: asyncapi
messages:
- description: Affirm fires this event when a customer initiates the Affirm checkout flow and is presented with the login screen. This is the first event in the checkout webhook lifecycle.
  name: CheckoutOpenedEvent
  summary: Fired when a customer opens the Affirm checkout flow.
  title: Checkout Opened
- description: Affirm fires this event when the customer's credit application is approved and financing terms are offered. The payload includes the approved loan amount, APR, payment terms, and customer information as configured in the Data Sharing Agreement.
  name: CheckoutApprovedEvent
  summary: Fired when a customer receives a positive credit decision from Affirm.
  title: Checkout Approved
- description: Affirm fires this event when the customer's credit application is not approved and financing cannot be offered for the requested amount. The merchant can use this event to present alternative payment options to the customer.
  name: CheckoutNotApprovedEvent
  summary: Fired when a customer receives a negative credit decision from Affirm.
  title: Checkout Not Approved
- description: Affirm fires this event when the customer clicks confirm at the end of the Affirm checkout flow and is redirected back to the merchant's user_confirmation_url. This is the final checkout event and indicates the customer has accepted the loan terms. The checkout token can now be exchanged server-side
  name: CheckoutConfirmedEvent
  summary: Fired when a customer confirms their financing and is redirected back to the merchant.
  title: Checkout Confirmed
- description: Affirm fires this event when a customer completes the prequalification flow and receives a financing decision. The payload includes approved amount, APR, remaining credit, and customer information as configured in the merchant's Data Sharing Agreement.
  name: PrequalDecisionEvent
  summary: Fired when a customer receives an approval decision during prequalification.
  title: Prequalification Decision
- description: Affirm fires this event when a prequalification offer expires. This can occur within the prequalification session or up to 7 days after the prequalification was completed. Merchants can use this event to prompt customers to re-qualify.
  name: PrequalExpiryEvent
  summary: Fired when a customer's prequalification expires.
  title: Prequalification Expiry
name: Affirm Webhooks
provider_name: affirm
provider_slug: affirm
servers:
- description: The merchant-configured HTTPS endpoint that receives webhook event notifications from Affirm. Must support TLS 1.2 and respond with a 2xx HTTP status to acknowledge receipt.
  name: merchantWebhookEndpoint
  protocol: https
  url: '{webhookUrl}'
slug: affirm-webhooks-asyncapi
spec_file: asyncapi/affirm-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/asyncapi/affirm-webhooks-asyncapi.yml
tags:
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
