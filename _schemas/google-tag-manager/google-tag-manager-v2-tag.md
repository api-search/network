---
description: Represents a Google Tag Manager Tag. A tag is a snippet of code that executes on a page when certain conditions (triggers) are met.
layout: schema
name: Tag
properties_list:
- description: GTM Tag's API relative path.
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
- description: The Tag ID uniquely identifies the GTM Tag.
  name: tagId
  type: string
- description: Tag display name.
  name: name
  type: string
- description: 'GTM Tag Type. Common types include ua (Universal Analytics), gaawc (Google Analytics GA4 Configuration), gaawe (Google Analytics GA4 Event), awct (Google Ads Conversion Tracking), sp (Custom Script), '
  name: type
  type: string
- description: If set to true, this tag will only fire in the live environment (not in preview or debug mode).
  name: liveOnly
  type: boolean
- description: User notes on how to apply this tag in the container.
  name: notes
  type: string
- description: The start timestamp in milliseconds to schedule a tag. The tag will only fire after this time.
  name: scheduleStartMs
  type: string
- description: The end timestamp in milliseconds to schedule a tag. The tag will stop firing after this time.
  name: scheduleEndMs
  type: string
- description: The tag's parameters, which configure its behavior.
  name: parameter
  type: array
- description: The fingerprint of the GTM Tag as computed at storage time. This value is recomputed whenever the tag is modified.
  name: fingerprint
  type: string
- description: Firing trigger IDs. A tag will fire when any of the listed triggers are true and all of its blockingTriggerIds (if any specified) are false.
  name: firingTriggerId
  type: array
- description: Blocking trigger IDs. If any of the listed triggers evaluates to true, the tag will not fire.
  name: blockingTriggerId
  type: array
- description: The list of setup tags. Currently, only one setup tag is allowed per tag.
  name: setupTag
  type: array
- description: The list of teardown tags. Currently, only one teardown tag is allowed per tag.
  name: teardownTag
  type: array
- description: Parent folder ID.
  name: parentFolderId
  type: string
- description: Option to fire this tag.
  name: tagFiringOption
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
- description: Indicates whether the tag is paused, which prevents the tag from firing.
  name: paused
  type: boolean
- description: If non-empty, then the tag display name will be included in the monitoring metadata map using the key specified.
  name: monitoringMetadataTagNameKey
  type: string
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-tag-schema.json
slug: google-tag-manager-v2-tag
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Tag
---
