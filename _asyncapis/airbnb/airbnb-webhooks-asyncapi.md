---
channels:
- description: The webhook endpoint that receives all Airbnb event notifications. Events are delivered as HTTP POST requests with a JSON payload. Each event includes a type field to identify the event category and a signature header for verification.
  name: /webhook
  operation: publish
  operation_id: receiveWebhookEvent
  summary: Receive an Airbnb webhook event
description: The Airbnb Webhooks API enables connectivity partners to receive real-time notifications when events occur on the Airbnb platform. It supports webhook subscriptions for reservation changes, message creation, review submissions, listing calendar updates, and other key events. Partners can subscribe to events such as reservation confirmations, cancellations, guest messages, new reviews, and availability or pricing changes, allowing their systems to react immediately without needing to poll the API for updates.
layout: asyncapi
messages:
- description: ''
  name: ReservationCreated
  summary: Sent when a new reservation request is created by a guest.
  title: Reservation Created
- description: ''
  name: ReservationConfirmed
  summary: Sent when a reservation is confirmed by the host or automatically through instant booking.
  title: Reservation Confirmed
- description: ''
  name: ReservationCancelled
  summary: Sent when a reservation is cancelled by either the host or guest.
  title: Reservation Cancelled
- description: ''
  name: ReservationUpdated
  summary: Sent when a reservation is modified, such as date changes or guest count updates.
  title: Reservation Updated
- description: ''
  name: ReservationCheckedIn
  summary: Sent when a guest checks in to the property.
  title: Reservation Checked In
- description: ''
  name: ReservationCheckedOut
  summary: Sent when a guest checks out of the property.
  title: Reservation Checked Out
- description: ''
  name: MessageCreated
  summary: Sent when a new message is created in a reservation thread by either the host or guest.
  title: Message Created
- description: ''
  name: ReviewSubmitted
  summary: Sent when a new review is submitted by a guest for a completed reservation.
  title: Review Submitted
- description: ''
  name: CalendarUpdated
  summary: Sent when the availability calendar for a listing is updated, including blocked dates and availability changes.
  title: Calendar Updated
- description: ''
  name: ListingUpdated
  summary: Sent when a listing is updated, including changes to description, amenities, photos, or status.
  title: Listing Updated
- description: ''
  name: PricingUpdated
  summary: Sent when the pricing for a listing is changed, including nightly rates, cleaning fees, and discount rules.
  title: Pricing Updated
- description: ''
  name: BookingCreated
  summary: Sent when a new experience booking is created by a guest.
  title: Experience Booking Created
- description: ''
  name: BookingConfirmed
  summary: Sent when an experience booking is confirmed by the host.
  title: Experience Booking Confirmed
- description: ''
  name: BookingCancelled
  summary: Sent when an experience booking is cancelled.
  title: Experience Booking Cancelled
name: Airbnb Webhooks API
provider_name: airbnb
provider_slug: airbnb
servers:
- description: The partner-configured HTTPS endpoint that receives webhook notifications from Airbnb. Partners register their webhook URL through the Airbnb developer portal.
  name: partnerWebhookEndpoint
  protocol: https
  url: '{webhookUrl}'
slug: airbnb-webhooks-asyncapi
spec_file: asyncapi/airbnb-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/asyncapi/airbnb-webhooks-asyncapi.yml
tags:
- AsyncAPI
- Webhooks
- Events
version: 2025.03.31
---
