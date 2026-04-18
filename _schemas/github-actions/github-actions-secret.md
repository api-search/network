---
description: Represents an encrypted secret for GitHub Actions. The encrypted value is never returned by the API.
layout: schema
name: GitHub Actions Secret
properties_list:
- description: The name of the secret.
  name: name
  type: string
- description: The date and time the secret was created.
  name: created_at
  type: string
- description: The date and time the secret was last updated.
  name: updated_at
  type: string
- description: The visibility scope of the secret (organization secrets only).
  name: visibility
  type: string
- description: The API URL to manage selected repositories for this secret (organization secrets with selected visibility only).
  name: selected_repositories_url
  type: string
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-secret-schema.json
slug: github-actions-secret
tags: []
title: GitHub Actions Secret
---
