---
channels:
- description: Triggered when Prisma Cloud generates a new alert due to a policy violation detected during a cloud resource scan. The alert payload contains full context about the violated policy, the affected cloud resource, and its account.
  name: alert/created
  operation: subscribe
  operation_id: onAlertCreated
  summary: New policy-violation alert created
- description: Triggered when an existing Prisma Cloud alert is updated, typically when the underlying resource configuration changes after the initial policy violation was detected, causing a re-evaluation.
  name: alert/updated
  operation: subscribe
  operation_id: onAlertUpdated
  summary: Existing alert updated
- description: Triggered when a Prisma Cloud alert is automatically resolved because the underlying cloud resource configuration has been brought back into compliance with the policy.
  name: alert/resolved
  operation: subscribe
  operation_id: onAlertResolved
  summary: Alert automatically resolved
- description: Triggered when a Prisma Cloud alert is manually dismissed by a user or suppressed by a configured snooze or suppression rule.
  name: alert/dismissed
  operation: subscribe
  operation_id: onAlertDismissed
  summary: Alert manually dismissed or snoozed
description: Prisma Cloud Cloud Security Posture Management (CSPM) Webhooks deliver real-time event notifications for policy violations and security alerts across multi-cloud environments including AWS, Azure, GCP, OCI, and Alibaba Cloud. Webhooks are configured as notification channels in Prisma Cloud Settings > Integrations and dispatch HTTP POST requests with JSON payloads to registered HTTPS endpoints whenever alert lifecycle events occur. Supported events include alert creation, update, resolution, and dismissal. Webhooks enable integration with SIEM platforms, SOAR systems, ticketing tools, and custom security automation workflows.
layout: asyncapi
messages:
- description: ''
  name: AlertCreated
  summary: A new Prisma Cloud policy-violation alert has been created
  title: Alert Created
- description: ''
  name: AlertUpdated
  summary: An existing Prisma Cloud policy-violation alert has been updated
  title: Alert Updated
- description: ''
  name: AlertResolved
  summary: A Prisma Cloud policy-violation alert has been automatically resolved
  title: Alert Resolved
- description: ''
  name: AlertDismissed
  summary: A Prisma Cloud policy-violation alert has been dismissed
  title: Alert Dismissed
name: Prisma Cloud CSPM Webhooks
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
servers:
- description: Customer-configured HTTPS endpoint to receive Prisma Cloud webhook notifications. The endpoint must be publicly accessible, accept HTTP POST requests with a JSON body, and return a 2xx HTTP status code. Configure the endpoint URL in Prisma Cloud Settings > Integrations > Add Integration > Webhook.
  name: customer-webhook
  protocol: https
  url: '{webhookUrl}'
slug: palo-alto-prisma-cloud-webhooks-asyncapi-original
spec_file: asyncapi/palo-alto-prisma-cloud-webhooks-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-prisma-cloud-webhooks-asyncapi-original.yml
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
version: 1.0.0
---
