---
description: ''
layout: schema
name: Group
properties_list:
- description: The unique identifier for the group.
  name: id
  type: string
- description: The name of the group.
  name: name
  type: string
- description: The domain name for Active Directory groups. For local groups, this is "local".
  name: domainName
  type: string
- description: The minimum site role for members of the group when they are imported from Active Directory.
  name: minimumSiteRole
  type: string
- description: The number of users in the group.
  name: userCount
  type: integer
- description: ''
  name: import
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-group-schema.json
slug: tableau-rest-group
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Group
---
