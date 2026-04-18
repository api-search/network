---
description: A Quay user account.
layout: schema
name: User
properties_list:
- description: The username.
  name: username
  type: string
- description: The user's email address.
  name: email
  type: string
- description: Whether the user's email has been verified.
  name: verified
  type: boolean
- description: Organizations the user belongs to.
  name: organizations
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-quay-user-schema.json
slug: red-hat-quay-user
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
