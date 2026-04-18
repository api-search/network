---
description: Represents the flag state override for a specific portal (account)
layout: schema
name: PortalFlagState
properties_list:
- description: The unique identifier for the HubSpot application
  name: appId
  type: integer
- description: The name of the feature flag
  name: flagName
  type: string
- description: The unique identifier for the HubSpot portal (account)
  name: portalId
  type: integer
- description: The state of a feature flag
  name: flagState
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-feature-flags-api-portal-flag-state-schema.json
slug: crm-feature-flags-api-portal-flag-state
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: PortalFlagState
---
