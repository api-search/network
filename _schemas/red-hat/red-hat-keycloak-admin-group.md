---
description: A group that enables bulk role and attribute assignment to users.
layout: schema
name: Group
properties_list:
- description: The unique identifier of the group.
  name: id
  type: string
- description: The name of the group.
  name: name
  type: string
- description: The full path of the group in the hierarchy.
  name: path
  type: string
- description: Child groups.
  name: subGroups
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-keycloak-admin-group-schema.json
slug: red-hat-keycloak-admin-group
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Group
---
