---
description: Represents a feature flag configuration for an application
layout: schema
name: FeatureFlag
properties_list:
- description: The unique identifier for the HubSpot application
  name: appId
  type: integer
- description: The name of the feature flag
  name: flagName
  type: string
- description: The state of a feature flag
  name: defaultState
  type: string
- description: The state of a feature flag
  name: overrideState
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-feature-flags-api-feature-flag-schema.json
slug: crm-feature-flags-api-feature-flag
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
title: FeatureFlag
---
