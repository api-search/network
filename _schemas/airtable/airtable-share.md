---
description: A share link that provides external access to an Airtable base, view, or form. Share links can be enabled or disabled and optionally protected with a password.
layout: schema
name: Airtable Share
properties_list:
- description: The unique identifier for the share link (starts with 'shr').
  name: shareId
  type: string
- description: The type of resource being shared.
  name: type
  type: string
- description: The current state of the share link.
  name: state
  type: string
- description: The ID of the user who created the share link.
  name: createdByUserId
  type: string
- description: The time when the share link was created.
  name: createdTime
  type: string
- description: The ID of the base this share link provides access to.
  name: baseId
  type: string
- description: The ID of the specific view this share link provides access to. Null for base-level shares.
  name: viewId
  type:
  - string
  - 'null'
- description: Whether the share link requires a password to access.
  name: isPasswordEnabled
  type: boolean
- description: The effective permission level granted to anyone accessing through this share link.
  name: effectivePermissionLevel
  type: string
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-share-schema.json
slug: airtable-share
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Share
---
