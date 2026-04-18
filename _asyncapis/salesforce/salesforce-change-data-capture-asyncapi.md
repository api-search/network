---
channels:
- description: CometD channel for subscribing to change events for a specific Salesforce standard or custom object. Delivers events when records of that type are created, updated, deleted, or undeleted.
  name: /data/{objectApiName}ChangeEvent
  operation: subscribe
  operation_id: receiveChangeEvent
  summary: Receive a record change event for a specific object
- description: Omnibus channel that delivers change events for all objects configured for Change Data Capture in your org's settings. Use this channel to receive all CDC events in a single subscription.
  name: /data/ChangeEvents
  operation: subscribe
  operation_id: receiveAllChangeEvents
  summary: Receive change events for all CDC-enabled objects
description: Salesforce Change Data Capture (CDC) delivers change events that represent changes to Salesforce records including creates, updates, deletes, and undeletes. Subscribers receive rich change events with header metadata, changed fields, and entity metadata. Change events are durable and retained for 72 hours. CDC enables near-real-time data replication and synchronization of Salesforce data to external systems.
layout: asyncapi
messages:
- description: ''
  name: ChangeEventMessage
  summary: A record change notification for a Salesforce object
  title: Salesforce Change Data Capture Event
name: Salesforce Change Data Capture API
provider_name: Salesforce
provider_slug: salesforce
servers:
- description: CometD endpoint for subscribing to Change Data Capture events
  name: salesforce-cometd
  protocol: https
  url: https://{instanceName}.salesforce.com/cometd/{apiVersion}
slug: salesforce-change-data-capture-asyncapi
spec_file: asyncapi/salesforce-change-data-capture-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/asyncapi/salesforce-change-data-capture-asyncapi.yml
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
- AsyncAPI
- Webhooks
- Events
version: '59.0'
---
