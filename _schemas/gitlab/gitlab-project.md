---
description: A GitLab project containing a Git repository, issues, merge requests, CI/CD pipelines, and other DevOps resources.
layout: schema
name: GitLab Project
properties_list:
- description: The unique identifier of the project.
  name: id
  type: integer
- description: The display name of the project.
  name: name
  type: string
- description: A short description of the project.
  name: description
  type:
  - string
  - 'null'
- description: The URL-friendly path component of the project name.
  name: path
  type: string
- description: The full path of the project including the namespace, such as group/project-name.
  name: path_with_namespace
  type: string
- description: The full name of the project including the namespace.
  name: name_with_namespace
  type: string
- description: The visibility level of the project.
  name: visibility
  type: string
- description: The URL to access the project in a browser.
  name: web_url
  type: string
- description: The HTTP URL for cloning the repository.
  name: http_url_to_repo
  type: string
- description: The SSH URL for cloning the repository.
  name: ssh_url_to_repo
  type: string
- description: The URL to the README file of the default branch.
  name: readme_url
  type:
  - string
  - 'null'
- description: The default branch of the repository.
  name: default_branch
  type:
  - string
  - 'null'
- description: List of topic tags associated with the project.
  name: topics
  type: array
- description: Whether the project is archived and read-only.
  name: archived
  type: boolean
- description: Whether the repository has been initialized with commits.
  name: empty_repo
  type: boolean
- description: ''
  name: namespace
  type: object
- description: ''
  name: owner
  type: object
- description: The ID of the user who created the project.
  name: creator_id
  type: integer
- description: The number of stars the project has received.
  name: star_count
  type: integer
- description: The number of forks of the project.
  name: forks_count
  type: integer
- description: The number of open issues in the project.
  name: open_issues_count
  type: integer
- description: The path to the CI/CD configuration file relative to the repository root.
  name: ci_config_path
  type:
  - string
  - 'null'
- description: The access level for the issues feature.
  name: issues_access_level
  type: string
- description: The access level for the merge requests feature.
  name: merge_requests_access_level
  type: string
- description: The access level for CI/CD pipelines and builds.
  name: builds_access_level
  type: string
- description: The access level for the project wiki.
  name: wiki_access_level
  type: string
- description: The access level for the container registry.
  name: container_registry_access_level
  type: string
- description: The access level for GitLab Pages.
  name: pages_access_level
  type: string
- description: ''
  name: permissions
  type: object
- description: ''
  name: statistics
  type: object
- description: The date and time the project was created.
  name: created_at
  type: string
- description: The date and time the project was last updated.
  name: updated_at
  type: string
- description: The date and time of the last activity in the project.
  name: last_activity_at
  type: string
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-project-schema.json
slug: gitlab-project
tags:
- Code
- Platform
- Software Development
- Source Control
title: GitLab Project
---
