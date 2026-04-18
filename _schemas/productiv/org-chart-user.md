---
description: Represents a user entry in the organizational chart published to the Productiv platform.
layout: schema
name: OrgChartUser
properties_list:
- description: The email address of the user.
  name: email
  type: string
- description: First name of the user.
  name: firstName
  type: string
- description: Last name of the user.
  name: lastName
  type: string
- description: The email address of the user's manager.
  name: managerEmail
  type: string
- description: The department of the user.
  name: department
  type: string
- description: The job title of the user.
  name: title
  type: string
provider_name: Productiv
provider_slug: productiv
schema_file: json-schema/org-chart-user.json
slug: org-chart-user
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
title: OrgChartUser
---
