---
description: ''
layout: schema
name: Version
properties_list:
- description: ''
  name: when
  type: string
- description: ''
  name: friendlyWhen
  type: string
- description: ''
  name: message
  type: string
- description: Set this to the current version number incremented by one
  name: number
  type: integer
- description: If `minorEdit` is set to 'true', no notification email or activity stream will be generated for the change.
  name: minorEdit
  type: boolean
- description: ''
  name: _expandable
  type: object
- description: True if content type is modifed in this version (e.g. page to blog)
  name: contentTypeModified
  type: boolean
- description: The revision id provided by confluence to be used as a revision in Synchrony
  name: confRev
  type: string
- description: The revision id provided by Synchrony
  name: syncRev
  type: string
- description: Source of the synchrony revision
  name: syncRevSource
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-version-schema.json
slug: atlassian-confluence-content-version
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: Version
---
