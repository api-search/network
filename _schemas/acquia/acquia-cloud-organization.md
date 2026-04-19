---
description: Organization information.
layout: schema
name: Organization
properties_list:
- description: The internal ID of the organization.
  name: id
  type: string
- description: The UUID of the organization.
  name: uuid
  type: string
- description: The name of the organization.
  name: name
  type: string
- description: The number of subscriptions this organization has.
  name: subscriptions_total
  type: integer
- description: The number of administrators this organization has.
  name: admins_total
  type: integer
- description: The number of users this organization has.
  name: users_total
  type: integer
- description: The number of teams this organization has.
  name: teams_total
  type: integer
- description: The number of roles this organization has.
  name: roles_total
  type: integer
- description: ''
  name: owner
  type: object
- description: An array of various flags that indicate functionality for the organization.
  name: flags
  type: object
- description: ''
  name: _links
  type: object
- description: Entities related to the organization.
  name: _embedded
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-organization-schema.json
slug: acquia-cloud-organization
tags:
- Content
- Experience
title: Organization
---
