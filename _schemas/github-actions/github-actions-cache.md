---
description: Represents a cached dependency entry in GitHub Actions.
layout: schema
name: GitHub Actions Cache Entry
properties_list:
- description: Unique identifier of the cache entry.
  name: id
  type: integer
- description: The Git reference for the cache entry.
  name: ref
  type: string
- description: The cache key used to identify the cache entry.
  name: key
  type: string
- description: The version of the cache entry.
  name: version
  type: string
- description: The date and time the cache was last accessed.
  name: last_accessed_at
  type: string
- description: The date and time the cache was created.
  name: created_at
  type: string
- description: The size of the cache entry in bytes.
  name: size_in_bytes
  type: integer
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-cache-schema.json
slug: github-actions-cache
tags: []
title: GitHub Actions Cache Entry
---
