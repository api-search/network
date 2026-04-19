---
description: ide schema from Acquia Cloud API
layout: schema
name: Ide
properties_list:
- description: The unique identifier of the Cloud IDE.
  name: uuid
  type: string
- description: The human-friendly label of the Cloud IDE.
  name: label
  type: string
- description: The current provisioning status of the Cloud IDE.
  name: status
  type: string
- description: ''
  name: _links
  type: object
- description: ''
  name: _embedded
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-ide-schema.json
slug: acquia-cloud-ide
tags:
- Content
- Experience
title: Ide
---
