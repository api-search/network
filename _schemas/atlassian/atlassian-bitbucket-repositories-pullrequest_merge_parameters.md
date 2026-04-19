---
description: The metadata that describes a pull request merge.
layout: schema
name: pullrequest_merge_parameters
properties_list:
- description: ''
  name: type
  type: string
- description: The commit message that will be used on the resulting commit.
  name: message
  type: string
- description: Whether the source branch should be deleted. If this is not provided, we fallback to the value used when the pull request was created, which defaults to False
  name: close_source_branch
  type: boolean
- description: The merge strategy that will be used to merge the pull request.
  name: merge_strategy
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-repositories-pullrequest_merge_parameters-schema.json
slug: atlassian-bitbucket-repositories-pullrequest_merge_parameters
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: pullrequest_merge_parameters
---
