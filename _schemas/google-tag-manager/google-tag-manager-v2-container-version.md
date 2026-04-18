---
description: Represents a version of a Google Tag Manager Container. A container version is a snapshot of all tags, triggers, variables, and configuration at a point in time.
layout: schema
name: ContainerVersion
properties_list:
- description: GTM ContainerVersion's API relative path.
  name: path
  type: string
- description: GTM Account ID.
  name: accountId
  type: string
- description: GTM Container ID.
  name: containerId
  type: string
- description: The Container Version ID uniquely identifies the GTM Container Version.
  name: containerVersionId
  type: string
- description: Container version display name.
  name: name
  type: string
- description: Container version description.
  name: description
  type: string
- description: The tags in the container that this version was taken from.
  name: tag
  type: array
- description: The triggers in the container that this version was taken from.
  name: trigger
  type: array
- description: The variables in the container that this version was taken from.
  name: variable
  type: array
- description: The fingerprint of the GTM Container Version as computed at storage time.
  name: fingerprint
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
- description: A value of true indicates this version has been deleted.
  name: deleted
  type: boolean
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-container-version-schema.json
slug: google-tag-manager-v2-container-version
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: ContainerVersion
---
