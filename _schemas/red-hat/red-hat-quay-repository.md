---
description: A container image repository in the Quay registry.
layout: schema
name: Repository
properties_list:
- description: The namespace the repository belongs to.
  name: namespace
  type: string
- description: The name of the repository.
  name: name
  type: string
- description: A description of the repository.
  name: description
  type: string
- description: Whether the repository is publicly accessible.
  name: is_public
  type: boolean
- description: The type of repository.
  name: kind
  type: string
- description: The number of tags in the repository.
  name: tag_count
  type: integer
- description: The status token for repository notifications.
  name: status_token
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-quay-repository-schema.json
slug: red-hat-quay-repository
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Repository
---
