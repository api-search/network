---
description: An autolink reference.
layout: schema
name: autolink
properties_list:
- description: ''
  name: id
  type: integer
- description: The prefix of a key that is linkified.
  name: key_prefix
  type: string
- description: template for the target URL that is generated if a key was found.
  name: url_template
  type: string
- description: Whether this autolink reference matches alphanumeric characters. If false, this autolink reference only matches numeric characters.
  name: is_alphanumeric
  type: boolean
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-autolinks-api-autolink-schema.json
slug: github-repo-autolinks-api-autolink
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: autolink
---
