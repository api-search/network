---
description: A Google Tag Manager Container represents a collection of tags, triggers, and variables deployed to a website, mobile app, or server-side environment. Containers organize measurement codes and related code fragments that are collectively managed through Google Tag Manager.
layout: schema
name: Google Tag Manager Container
properties_list:
- description: 'GTM Container''s API relative path. Example: accounts/123456/containers/789012.'
  name: path
  type: string
- description: GTM Account ID that this container belongs to.
  name: accountId
  type: string
- description: The Container ID uniquely identifies the GTM Container within the account.
  name: containerId
  type: string
- description: Container display name. This is the human-readable name shown in the Tag Manager interface.
  name: name
  type: string
- description: List of domain names associated with the Container. Used for auto-event tracking and link decoration across domains.
  name: domainName
  type: array
- description: Container Public ID. This is the identifier used in the GTM snippet installed on websites (e.g., GTM-XXXX).
  name: publicId
  type: string
- description: All Tag IDs that refer to this Container. These are the Google Tag IDs associated with this container.
  name: tagIds
  type: array
- description: Container notes. Free-text field for describing the purpose, ownership, or other metadata about the container.
  name: notes
  type: string
- description: List of Usage Contexts for the Container. Defines the platform or environment where this container will be deployed.
  name: usageContext
  type: array
- description: The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the container is modified and is used for optimistic locking to prevent concurrent modification conf
  name: fingerprint
  type: string
- description: Auto-generated link to the tag manager UI for this container.
  name: tagManagerUrl
  type: string
- description: List of server-side container URLs. Only applicable for server-side containers. These are the URLs where the server-side tagging server is deployed.
  name: taggingServerUrls
  type: array
- description: Read-only Container feature set indicating which capabilities are available for this container type.
  name: features
  type: object
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-container-schema.json
slug: google-tag-manager-container
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Google Tag Manager Container
---
