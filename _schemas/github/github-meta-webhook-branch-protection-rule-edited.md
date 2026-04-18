---
description: webhook-branch-protection-rule-edited from GitHub API
layout: schema
name: webhook-branch-protection-rule-edited
properties_list:
- description: ''
  name: action
  type: string
- description: If the action was `edited`, the changes to the rule.
  name: changes
  type: object
- description: ''
  name: enterprise
  type: object
- description: ''
  name: installation
  type: object
- description: ''
  name: organization
  type: object
- description: ''
  name: repository
  type: object
- description: The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/enterprise-server@3.9/github/administering-a-repository/defining-the-mergeability-of-pull
  name: rule
  type: object
- description: ''
  name: sender
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-meta-webhook-branch-protection-rule-edited-schema.json
slug: github-meta-webhook-branch-protection-rule-edited
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: webhook-branch-protection-rule-edited
---
