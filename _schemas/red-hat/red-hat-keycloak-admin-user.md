---
description: A user account within a Keycloak realm.
layout: schema
name: User
properties_list:
- description: The unique identifier of the user.
  name: id
  type: string
- description: The username.
  name: username
  type: string
- description: The user's first name.
  name: firstName
  type: string
- description: The user's last name.
  name: lastName
  type: string
- description: The user's email address.
  name: email
  type: string
- description: Whether the email has been verified.
  name: emailVerified
  type: boolean
- description: Whether the user account is enabled.
  name: enabled
  type: boolean
- description: The creation timestamp in milliseconds.
  name: createdTimestamp
  type: integer
- description: Custom user attributes.
  name: attributes
  type: object
- description: User credentials configuration.
  name: credentials
  type: array
- description: Actions required on next login.
  name: requiredActions
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-keycloak-admin-user-schema.json
slug: red-hat-keycloak-admin-user
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: User
---
