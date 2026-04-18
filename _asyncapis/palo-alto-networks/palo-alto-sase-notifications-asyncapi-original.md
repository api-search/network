---
channels:
- description: Channel for security incident notifications. Triggered when SASE detects a security incident such as a policy breach, threat detection, or anomalous activity within a tenant's network perimeter. Incident notifications include severity classification, affected tenant context, and descriptive details for triage and response.
  name: /notification/incident
  operation: subscribe
  operation_id: onIncidentNotification
  summary: Security incident notification
- description: Channel for platform announcement notifications. Delivered when Palo Alto Networks publishes service announcements including scheduled maintenance windows, feature releases, deprecation notices, and service status updates that affect SASE tenants.
  name: /notification/announcement
  operation: subscribe
  operation_id: onAnnouncementNotification
  summary: Platform announcement notification
- description: Channel for dataplane upgrade notifications. Triggered when a SASE dataplane upgrade is scheduled, in progress, or completed for a specific region. Notifications include the current and target software versions, scheduled maintenance window, and upgrade status transitions.
  name: /notification/dataplane-upgrade
  operation: subscribe
  operation_id: onDataplaneUpgradeNotification
  summary: Dataplane upgrade notification
- description: Channel for certificate expiration warning notifications. Triggered when TLS/SSL certificates used by SASE service connections, GlobalProtect portals, or custom domains are approaching their expiration date. Warnings are sent at configurable intervals (e.g., 90, 60, 30, 14, 7 days before expiry) to allow administrators to renew certificates before service disruption.
  name: /notification/certificate-expiry
  operation: subscribe
  operation_id: onCertificateExpiryNotification
  summary: Certificate expiration warning notification
description: Palo Alto Networks SASE (Secure Access Service Edge) delivers real-time notifications for security incidents, platform announcements, dataplane upgrades, and certificate expiration warnings across multitenant deployments. Notifications are sent as HTTP POST requests to registered webhook endpoints configured at the tenant or tenant service group (TSG) level. Each notification includes a tenant context identifier (tsg_id) for routing in multitenant environments. Notification subscriptions are managed through the SASE Multitenant Notification Service API, allowing administrators to select notification types, severity thresholds, and delivery endpoints for each tenant.
layout: asyncapi
messages:
- description: ''
  name: IncidentNotification
  summary: Webhook payload sent when a security incident is detected within a SASE tenant. Contains the incident classification, severity, affected tenant context, and descriptive information for triage.
  title: SASE Security Incident Notification
- description: ''
  name: AnnouncementNotification
  summary: Webhook payload sent for platform announcements including maintenance windows, feature releases, deprecation notices, and service status updates.
  title: SASE Platform Announcement Notification
- description: ''
  name: DataplaneUpgradeNotification
  summary: Webhook payload sent when a SASE dataplane upgrade is scheduled, in progress, or completed for a region.
  title: SASE Dataplane Upgrade Notification
- description: ''
  name: CertificateExpiryNotification
  summary: Webhook payload sent when a TLS/SSL certificate used by SASE services is approaching its expiration date.
  title: Certificate Expiration Warning Notification
name: SASE Multitenant Notifications
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
servers:
- description: Your notification endpoint URL registered with the SASE Multitenant Notification Service. Configure notification subscriptions via the SASE API to specify which notification types are delivered to this endpoint. The endpoint must accept POST requests with JSON payloads and return a 2xx response within 30 seconds.
  name: webhook
  protocol: https
  url: '{notificationEndpoint}'
slug: palo-alto-sase-notifications-asyncapi-original
spec_file: asyncapi/palo-alto-sase-notifications-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-sase-notifications-asyncapi-original.yml
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
