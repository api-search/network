---
description: The response for a user object.
layout: schema
name: User
properties_list:
- description: The internal database ID (uid) of the user.
  name: id
  type: integer
- description: The UUID for the user.
  name: uuid
  type: string
- description: The user name.
  name: name
  type: string
- description: The first name of the user.
  name: first_name
  type: string
- description: The last name of the user.
  name: last_name
  type: string
- description: The date/time of the last login for the user.
  name: last_login_at
  type: string
- description: The date/time when the user was created.
  name: created_at
  type: string
- description: The e-mail address of the user.
  name: mail
  type: string
- description: The telephone numbers for the user.
  name: phone
  type: object
- description: The job title of the user.
  name: job_title
  type: string
- description: The job function of the user.
  name: job_function
  type: string
- description: The company of the user.
  name: company
  type: string
- description: The country of the user.
  name: country
  type: string
- description: The state of the user, if in the United States.
  name: state
  type: string
- description: The timezone of the user.
  name: timezone
  type: string
- description: The user's picture url.
  name: picture_url
  type: string
- description: The various feature flags for the user.
  name: features
  type: array
- description: ''
  name: flags
  type: object
- description: Metadata related to the user.
  name: metadata
  type: object
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-user-schema.json
slug: acquia-cloud-user
tags:
- Content
- Experience
title: User
---
