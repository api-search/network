---
description: defines the payment in transfer reservation. For "CREDIT_CARD" - creditCard is mandatory, for "TRAVEL_ACCOUNT" - paymentReference is optional, for "PAYMENT_SERVICE_PROVIDER" - paymentServiceProvider and paymentReference are mandatory.
layout: schema
name: Payment
properties_list:
- description: Method of payment required when PaymentType equal BT (applicable only for reservation action).
  name: methodOfPayment
  type: string
- description: payment refence that will be passed to provider in case "TRAVEL_ACCOUNT" method of payment
  name: paymentReference
  type: string
- description: payment service provider details will be passed to provider in case "PAYMENT_SERVICE_PROVIDER" method of payment.
  name: paymentServiceProvider
  type: string
- description: ''
  name: creditCard
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-payment-schema.json
slug: transfer-booking-payment
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Payment
---
