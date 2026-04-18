---
description: Represents a Google Tag Manager Trigger. A trigger defines conditions under which tags should fire, such as page views, clicks, form submissions, or custom events.
layout: schema
name: Trigger
properties_list:
- description: GTM Trigger's API relative path.
  name: path
  type: string
- description: GTM Account ID.
  name: accountId
  type: string
- description: GTM Container ID.
  name: containerId
  type: string
- description: GTM Workspace ID.
  name: workspaceId
  type: string
- description: The Trigger ID uniquely identifies the GTM Trigger.
  name: triggerId
  type: string
- description: Trigger display name.
  name: name
  type: string
- description: Defines the data layer event that causes this trigger.
  name: type
  type: string
- description: Used in the case of custom event, which is fired if and only if all Conditions are true.
  name: customEventFilter
  type: array
- description: The trigger will only fire if and only if all Conditions are true.
  name: filter
  type: array
- description: Used in the case of auto event tracking for filtering events.
  name: autoEventFilter
  type: array
- description: The fingerprint of the GTM Trigger as computed at storage time. This value is recomputed whenever the trigger is modified.
  name: fingerprint
  type: string
- description: Parent folder ID.
  name: parentFolderId
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
- description: User notes on how to apply this trigger in the container.
  name: notes
  type: string
- description: Additional parameters for the trigger.
  name: parameter
  type: array
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-trigger-schema.json
slug: google-tag-manager-v2-trigger
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Trigger
---
