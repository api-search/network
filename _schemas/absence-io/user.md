---
description: An employee user record.
layout: schema
name: User
properties_list:
- description: Unique identifier of the user.
  name: _id
  type: string
- description: Full name of the user.
  name: name
  type: string
- description: Email address of the user.
  name: email
  type: string
- description: ID of the department the user belongs to.
  name: departmentId
  type: string
- description: ID of the location the user is assigned to.
  name: locationId
  type: string
- description: ID of the team the user belongs to.
  name: teamId
  type: string
- description: 'User status: 1=active, 0=inactive.'
  name: status
  type: integer
- description: User's preferred language code.
  name: language
  type: string
provider_name: Absence.io
provider_slug: absence-io
schema_file: json-schema/user-schema.json
slug: user
tags:
- Absences
- Employees
- Leave Management
- HR
title: User
---
