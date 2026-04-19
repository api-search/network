---
description: A file object, representing a file at a commit in a repository
layout: schema
name: commit_file
properties_list:
- description: ''
  name: type
  type: string
- description: The path in the repository
  name: path
  type: string
- description: ''
  name: attributes
  type: string
- description: The escaped version of the path as it appears in a diff. If the path does not require escaping this will be the same as path.
  name: escaped_path
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-workspaces-commit_file-schema.json
slug: atlassian-bitbucket-workspaces-commit_file
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: commit_file
---
