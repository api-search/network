---
description: A role that can be assigned to users or groups for authorization.
layout: schema
name: Role
properties_list:
- description: The unique identifier of the role.
  name: id
  type: string
- description: The name of the role.
  name: name
  type: string
- description: A description of the role.
  name: description
  type: string
- description: Whether this is a composite role containing other roles.
  name: composite
  type: boolean
- description: Whether this is a client-level role.
  name: clientRole
  type: boolean
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-keycloak-admin-role-schema.json
slug: red-hat-keycloak-admin-role
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Role
---
