---
description: Represents a Google Tag Manager Workspace. A workspace is an isolated editing environment within a container where changes to tags, triggers, and variables can be made and tested before being published.
layout: schema
name: Workspace
properties_list:
- description: GTM Workspace's API relative path.
  name: path
  type: string
- description: GTM Account ID.
  name: accountId
  type: string
- description: GTM Container ID.
  name: containerId
  type: string
- description: The Workspace ID uniquely identifies the GTM Workspace.
  name: workspaceId
  type: string
- description: Workspace display name.
  name: name
  type: string
- description: Workspace description.
  name: description
  type: string
- description: The fingerprint of the GTM Workspace as computed at storage time. This value is recomputed whenever the workspace is modified.
  name: fingerprint
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-workspace-schema.json
slug: google-tag-manager-v2-workspace
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Workspace
---
