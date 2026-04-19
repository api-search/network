---
description: Groups objects to create an object group.
layout: schema
name: GroupObjectsRequest
properties_list:
- description: A user-supplied object ID for the group to be created.
  name: groupObjectId
  type: string
- description: The object IDs of the objects to group.
  name: childrenObjectIds
  type: array
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-group-objects-request-schema.json
slug: google-slides-group-objects-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: GroupObjectsRequest
---
