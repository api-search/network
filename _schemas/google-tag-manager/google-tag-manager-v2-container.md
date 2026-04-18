---
description: Represents a Google Tag Manager Container, which is a collection of tags, triggers, and variables used on a website or mobile app.
layout: schema
name: Container
properties_list:
- description: GTM Container's API relative path.
  name: path
  type: string
- description: GTM Account ID.
  name: accountId
  type: string
- description: The Container ID uniquely identifies the GTM Container.
  name: containerId
  type: string
- description: Container display name.
  name: name
  type: string
- description: List of domain names associated with the Container. This is used for auto-event tracking and link decoration.
  name: domainName
  type: array
- description: Container Public ID (e.g., GTM-XXXX).
  name: publicId
  type: string
- description: All Tag IDs that refer to this Container.
  name: tagIds
  type: array
- description: Container Notes.
  name: notes
  type: string
- description: List of Usage Contexts for the Container. Valid values include web, android, ios, and server.
  name: usageContext
  type: array
- description: The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the container is modified.
  name: fingerprint
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
- description: List of server-side container URLs for the Container.
  name: taggingServerUrls
  type: array
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-container-schema.json
slug: google-tag-manager-v2-container
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Container
---
