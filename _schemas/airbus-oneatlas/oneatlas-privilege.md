---
description: ''
layout: schema
name: Privilege
properties_list:
- description: The creation time of the created Privilege. This is returned when the Privilege is properly created.
  name: createdAt
  type: string
- description: Filters the scope of the privilege (e.g. by workspace, id)
  name: filter
  type: object
- description: ''
  name: id
  type: object
- description: The priority of the privilege
  name: priority
  type: integer
- description: List of rights granted to a user. For now, only "browse" is supported. Therefore, it will give all the rights for now.
  name: rights
  type: object
- description: ''
  name: subscriptionId
  type: object
- description: ''
  name: userId
  type: object
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-privilege-schema.json
slug: oneatlas-privilege
tags:
- Imagery
- Satellites
title: Privilege
---
