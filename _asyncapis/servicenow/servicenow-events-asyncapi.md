---
channels:
- description: Receives notifications when incident records are created, updated, or resolved in ServiceNow. Triggered by business rules configured on the incident table.
  name: /webhook/incident
  operation: publish
  operation_id: receiveIncidentEvent
  summary: Receive an incident event notification
- description: Receives notifications when change request records are created, approved, implemented, or closed. Triggered by business rules or workflow activities on the change_request table.
  name: /webhook/change
  operation: publish
  operation_id: receiveChangeEvent
  summary: Receive a change request event notification
- description: Receives event management alerts from ServiceNow IT Operations Management. Events are published to external monitoring systems when alerts are triggered, acknowledged, or resolved.
  name: /webhook/event-management
  operation: publish
  operation_id: receiveEventManagementAlert
  summary: Receive an event management alert
description: ServiceNow supports outbound event-driven integrations through business rules, event management, and outbound REST messages. When records are created, updated, or deleted in ServiceNow tables, business rules can trigger outbound HTTP POST notifications to external webhook receivers. This specification documents the event payloads and notification patterns used by ServiceNow's outbound integration capabilities for incident, change, and problem management workflows.
layout: asyncapi
messages:
- description: ''
  name: IncidentCreated
  summary: Notification sent when a new incident is created.
  title: Incident Created
- description: ''
  name: IncidentUpdated
  summary: Notification sent when an incident is updated.
  title: Incident Updated
- description: ''
  name: IncidentResolved
  summary: Notification sent when an incident is resolved or closed.
  title: Incident Resolved
- description: ''
  name: ChangeCreated
  summary: Notification sent when a change request is created.
  title: Change Request Created
- description: ''
  name: ChangeUpdated
  summary: Notification sent when a change request is approved, implemented, or closed.
  title: Change Request Updated
- description: ''
  name: EventManagementAlert
  summary: Alert notification from ServiceNow Event Management.
  title: Event Management Alert
name: ServiceNow Events and Notifications
provider_name: ServiceNow
provider_slug: servicenow
servers:
- description: Your webhook receiver endpoint. ServiceNow sends POST requests to this URL when configured business rules or event actions are triggered.
  name: webhookReceiver
  protocol: https
  url: '{webhookUrl}'
slug: servicenow-events-asyncapi
spec_file: asyncapi/servicenow-events-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/servicenow/refs/heads/main/asyncapi/servicenow-events-asyncapi.yml
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
- AsyncAPI
- Webhooks
- Events
version: Yokohama
---
