---
description: ''
layout: schema
name: Site
properties_list:
- description: The unique identifier for the site.
  name: id
  type: string
- description: The name of the site.
  name: name
  type: string
- description: The URL namespace for the site.
  name: contentUrl
  type: string
- description: The administrator mode for the site.
  name: adminMode
  type: string
- description: The current state of the site.
  name: state
  type: string
- description: The storage quota for the site in megabytes.
  name: storageQuota
  type: integer
- description: The maximum number of users for the site. A value of -1 indicates no limit.
  name: userQuota
  type: integer
- description: The number of Creator-licensed users on the site.
  name: numCreators
  type: integer
- description: The number of Explorer-licensed users on the site.
  name: numExplorers
  type: integer
- description: The number of Viewer-licensed users on the site.
  name: numViewers
  type: integer
- description: Whether subscriptions are disabled on the site.
  name: disableSubscriptions
  type: boolean
- description: The revision number of the site.
  name: revision
  type: string
- description: ''
  name: usage
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-site-schema.json
slug: tableau-rest-site
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Site
---
