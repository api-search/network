---
description: ''
layout: schema
name: Revision
properties_list:
- description: The revision number.
  name: revisionNumber
  type: integer
- description: The date and time the revision was published.
  name: publishedAt
  type: string
- description: Whether this revision has been deleted.
  name: deleted
  type: boolean
- description: Whether this is the current revision.
  name: current
  type: boolean
- description: The size of the revision in bytes.
  name: sizeInBytes
  type: integer
- description: ''
  name: publisher
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-revision-schema.json
slug: tableau-rest-revision
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Revision
---
