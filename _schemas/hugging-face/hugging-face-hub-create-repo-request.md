---
description: ''
layout: schema
name: CreateRepoRequest
properties_list:
- description: Repository name
  name: name
  type: string
- description: Repository type
  name: type
  type: string
- description: Organization to create the repo under
  name: organization
  type: string
- description: Whether the repo should be private
  name: private
  type: boolean
- description: SDK for Spaces (required when type is space)
  name: sdk
  type: string
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-hub-create-repo-request-schema.json
slug: hugging-face-hub-create-repo-request
tags: []
title: CreateRepoRequest
---
