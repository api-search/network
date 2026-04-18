---
description: The payload delivered to the webhook endpoint for every Prisma Cloud CSPM alert lifecycle event. Contains all contextual information about the event type, the alert, the violated policy, and the affected cloud resource.
layout: schema
name: AlertPayload
properties_list:
- description: The type of alert lifecycle event that triggered this webhook notification. Identifies whether this is a creation, update, resolution, or dismissal event.
  name: notification_type
  type: string
- description: The unique identifier for the Prisma Cloud alert. Alert IDs are prefixed with 'P-' followed by a numeric sequence, used to reference the alert in Prisma Cloud API operations and the management console
  name: alert_id
  type: string
- description: The current lifecycle status of the alert at the time this webhook notification was dispatched.
  name: alert_status
  type: string
- description: The unique UUID identifier of the Prisma Cloud security policy that was violated and triggered this alert. Can be used to retrieve full policy details via the Prisma Cloud API.
  name: policy_id
  type: string
- description: The human-readable display name of the Prisma Cloud security policy that was violated. Provides immediate context about the nature of the misconfiguration or compliance gap detected.
  name: policy_name
  type: string
- description: The cloud service provider where the violating resource resides. Identifies which cloud environment requires investigation and remediation.
  name: cloud_type
  type: string
- description: The cloud provider account ID, subscription ID, or project ID where the violating resource is deployed. Used to identify the specific cloud account requiring remediation.
  name: account_id
  type: string
- description: The unique identifier of the cloud resource that violated the policy. For AWS resources this is typically an ARN. For Azure resources this is the resource ID path. For GCP resources this is the full r
  name: resource_id
  type: string
- description: The cloud provider service or resource type of the violating resource (e.g., s3, ec2, azure_storage_account, google_storage_bucket). Used to identify the type of infrastructure requiring remediation.
  name: resource_type
  type: string
- description: The severity level of the policy violation as defined by the Prisma Cloud security policy. Drives alert prioritization and notification routing in downstream systems.
  name: severity
  type: string
- description: The ISO 8601 date-time string indicating when this alert event occurred. For created events this is the alert creation time. For resolved or dismissed events this is the time of the status change.
  name: timestamp
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-webhooks-alert-payload-schema.json
slug: prisma-cloud-webhooks-alert-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AlertPayload
---
