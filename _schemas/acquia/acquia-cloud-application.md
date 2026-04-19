---
description: application schema from Acquia Cloud API
layout: schema
name: Application
properties_list:
- description: The unique internal ID of the application.
  name: id
  type: integer
- description: The UUID of the application.
  name: uuid
  type: string
- description: The name of the application.
  name: name
  type: string
- description: Hosting details for this application.
  name: hosting
  type: object
- description: ''
  name: subscription
  type: object
- description: ''
  name: organization
  type: object
- description: ''
  name: flags
  type: object
- description: The type of application supported.
  name: type
  type: string
- description: The current application status.
  name: status
  type: string
- description: ''
  name: _links
  type: object
- description: Entities related to the application.
  name: _embedded
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-application-schema.json
slug: acquia-cloud-application
tags:
- Content
- Experience
title: Application
---
