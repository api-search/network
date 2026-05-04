---
image: /assets/images/blog/network-update.png
layout: post
title: Finding Event-Driven APIs, Webhooks, and Streams in the Index
tags:
  - AsyncAPI
  - Event-Driven
  - Webhooks
  - Search
  - Discovery
date: 2026-05-03
---

Most of what gets profiled in the catalog is request/response — REST APIs documented with OpenAPI. But a growing slice of the network is the other half of the integration story: events, webhooks, message queues, and streams. Those don't surface well through OpenAPI alone, so we describe them with [AsyncAPI](https://www.asyncapi.com/) and index them as a first-class collection at [asyncapi.apis.io](https://asyncapi.apis.io).

The current index has **196 AsyncAPI specifications across 165 providers**, covering the channels, events, and message schemas an integrator needs to subscribe to a webhook, consume from a queue, or process a stream — alongside the OpenAPI descriptions that handle the management side of those same providers.

### The shape of event-driven coverage

The AsyncAPI side of the catalog clusters into a few distinct categories of providers, each describing events in their own way:

**Message brokers and event buses** — the platforms that move events between systems. [Apache Kafka](https://asyncapi.apis.io/asyncapis/apache-kafka/), [Apache Pulsar](https://asyncapi.apis.io/asyncapis/apache-pulsar/), [RabbitMQ](https://asyncapi.apis.io/asyncapis/rabbitmq/), [NATS](https://asyncapi.apis.io/asyncapis/nats/), [Amazon EventBridge](https://asyncapi.apis.io/asyncapis/amazon-eventbridge/), [SNS](https://asyncapi.apis.io/asyncapis/amazon-sns/), [SQS](https://asyncapi.apis.io/asyncapis/amazon-sqs/), [Kinesis](https://asyncapi.apis.io/asyncapis/amazon-kinesis/), [Azure Service Bus](https://asyncapi.apis.io/asyncapis/azure-service-bus/), [Event Hubs](https://asyncapi.apis.io/asyncapis/microsoft-azure-event-hubs/), [Google Pub/Sub](https://asyncapi.apis.io/asyncapis/google-pub-sub/), [IBM MQ](https://asyncapi.apis.io/asyncapis/ibm-mq/), and [AMQP](https://asyncapi.apis.io/asyncapis/amqp/) all sit in the index with their channels and topics described.

**SaaS webhooks** — the long tail of "tell me when something happened" subscriptions. [Stripe](https://asyncapi.apis.io/asyncapis/stripe/), [GitHub](https://asyncapi.apis.io/asyncapis/github/), [GitLab](https://asyncapi.apis.io/asyncapis/gitlab/), [Slack](https://asyncapi.apis.io/asyncapis/slack/), [Discord](https://asyncapi.apis.io/asyncapis/discord/), [Zendesk](https://asyncapi.apis.io/asyncapis/zendesk/), [HubSpot](https://asyncapi.apis.io/asyncapis/hubspot/), [Salesforce](https://asyncapi.apis.io/asyncapis/salesforce/), [Calendly](https://asyncapi.apis.io/asyncapis/calendly/), [DocuSign](https://asyncapi.apis.io/asyncapis/docusign/), [Intuit](https://asyncapi.apis.io/asyncapis/intuit/), and dozens more describe the events you can subscribe to and the payload shapes you'll receive.

**Cloud-native eventing** — the building blocks of event-driven architecture. [CloudEvents](https://asyncapi.apis.io/asyncapis/cloudevents/), [Dapr](https://asyncapi.apis.io/asyncapis/dapr/), [Knative](https://asyncapi.apis.io/asyncapis/knative/), [KEDA](https://asyncapi.apis.io/asyncapis/keda/), [Argo](https://asyncapi.apis.io/asyncapis/argo/), [Conductor](https://asyncapi.apis.io/asyncapis/conductor/), and the [Kubernetes operator](https://asyncapi.apis.io/asyncapis/kubernetes-operators/) and [services](https://asyncapi.apis.io/asyncapis/kubernetes-services/) surfaces that everything else builds on.

**Payments and financial events** — where webhooks are the integration. [Stripe](https://asyncapi.apis.io/asyncapis/stripe/), [Braintree](https://asyncapi.apis.io/asyncapis/braintree/), [Coinbase](https://asyncapi.apis.io/asyncapis/coinbase/), [Binance](https://asyncapi.apis.io/asyncapis/binance/), [Affirm](https://asyncapi.apis.io/asyncapis/affirm/), [Marqeta](https://asyncapi.apis.io/asyncapis/marqeta/), [Moov](https://asyncapi.apis.io/asyncapis/moov/), and [Fiserv](https://asyncapi.apis.io/asyncapis/fiserv/) describe the lifecycle events that drive most fintech integrations.

**Observability and operations** — the streams that tell you something is wrong. [OpenTelemetry](https://asyncapi.apis.io/asyncapis/opentelemetry/), [Prometheus](https://asyncapi.apis.io/asyncapis/prometheus/), [Sentry](https://asyncapi.apis.io/asyncapis/sentry/), [Bugsnag](https://asyncapi.apis.io/asyncapis/bugsnag/), [Rollbar](https://asyncapi.apis.io/asyncapis/rollbar/), [Dynatrace](https://asyncapi.apis.io/asyncapis/dynatrace/), [LogRocket](https://asyncapi.apis.io/asyncapis/logrocket/), [Fullstory](https://asyncapi.apis.io/asyncapis/fullstory/), and [Opsgenie](https://asyncapi.apis.io/asyncapis/opsgenie/).

**Communications and realtime** — voice, SMS, chat. [Sinch](https://asyncapi.apis.io/asyncapis/sinch/), [Bandwidth](https://asyncapi.apis.io/asyncapis/bandwidth/), [SendGrid](https://asyncapi.apis.io/asyncapis/sendgrid/), [Brevo](https://asyncapi.apis.io/asyncapis/brevo/), [MessageBird](https://asyncapi.apis.io/asyncapis/messagebird/), [WhatsApp](https://asyncapi.apis.io/asyncapis/whatsapp/), [Twitch](https://asyncapi.apis.io/asyncapis/twitch/), and [Zoom](https://asyncapi.apis.io/asyncapis/zoom/) all expose their delivery, status, and lifecycle events here.

### Why a separate index

REST and event-driven describe two different shapes of integration. A profile that only covers OpenAPI tells you how to *call* a provider; the AsyncAPI side tells you what the provider will *send back at you* — the webhook events that fire when an order ships, the topic you can subscribe to for state changes, the message schema your consumer needs to parse.

For each provider with both shapes, the network keeps them side by side. [Stripe's profile](https://providers.apis.io/providers/stripe/) lists OpenAPI for the management surface and an AsyncAPI for the webhook events. [GitHub](https://providers.apis.io/providers/github/) does the same. The index treats them as complementary descriptions of the same provider, so you can find one through the other.

### Searching for events

The [asyncapi.apis.io](https://asyncapi.apis.io) homepage is filterable across all 196 specs — type "webhook," "events," "kafka," or a vertical like "payments" and the list narrows. Each spec page lists the channels, operations, and message schemas, and links back to the provider's full profile, OpenAPI specs, and any [JSON-LD context](https://json-ld.apis.io) describing the same entities.

For agents working through the catalog, the practical effect is that "find me a payment provider with webhooks" or "find me an event bus" or "find me a CI/CD platform that publishes pipeline events" is a single filter query rather than a research project.

The OpenAPI side of the index covers the request/response surface across **11,989 APIs**. The AsyncAPI side fills in the event surface — the part of integration that has historically been the hardest to discover from the outside. The point is to have both indexed in the same structure, so an integrator (or an agent) can search across either shape and surface the right description for the job.
