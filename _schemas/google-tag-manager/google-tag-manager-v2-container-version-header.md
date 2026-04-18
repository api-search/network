---
description: Represents a summary of a container version, without the full tag, trigger, and variable details.
layout: schema
name: ContainerVersionHeader
properties_list:
- description: GTM Container Version's API relative path.
  name: path
  type: string
- description: ''
  name: accountId
  type: string
- description: ''
  name: containerId
  type: string
- description: ''
  name: containerVersionId
  type: string
- description: Container version display name.
  name: name
  type: string
- description: Number of tags in the container version.
  name: numTags
  type: string
- description: Number of triggers in the container version.
  name: numTriggers
  type: string
- description: Number of variables in the container version.
  name: numVariables
  type: string
- description: ''
  name: deleted
  type: boolean
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-container-version-header-schema.json
slug: google-tag-manager-v2-container-version-header
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: ContainerVersionHeader
---
