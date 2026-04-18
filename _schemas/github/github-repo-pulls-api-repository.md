---
description: repository on GitHub.
layout: schema
name: repository
properties_list:
- description: Unique identifier of the repository
  name: id
  type: integer
- description: ''
  name: node_id
  type: string
- description: The name of the repository.
  name: name
  type: string
- description: ''
  name: full_name
  type: string
- description: ''
  name: license
  type: object
- description: ''
  name: forks
  type: integer
- description: ''
  name: permissions
  type: object
- description: ''
  name: owner
  type: object
- description: Whether the repository is private or public.
  name: private
  type: boolean
- description: ''
  name: html_url
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: fork
  type: boolean
- description: ''
  name: url
  type: string
- description: ''
  name: archive_url
  type: string
- description: ''
  name: assignees_url
  type: string
- description: ''
  name: blobs_url
  type: string
- description: ''
  name: branches_url
  type: string
- description: ''
  name: collaborators_url
  type: string
- description: ''
  name: comments_url
  type: string
- description: ''
  name: commits_url
  type: string
- description: ''
  name: compare_url
  type: string
- description: ''
  name: contents_url
  type: string
- description: ''
  name: contributors_url
  type: string
- description: ''
  name: deployments_url
  type: string
- description: ''
  name: downloads_url
  type: string
- description: ''
  name: events_url
  type: string
- description: ''
  name: forks_url
  type: string
- description: ''
  name: git_commits_url
  type: string
- description: ''
  name: git_refs_url
  type: string
- description: ''
  name: git_tags_url
  type: string
- description: ''
  name: git_url
  type: string
- description: ''
  name: issue_comment_url
  type: string
- description: ''
  name: issue_events_url
  type: string
- description: ''
  name: issues_url
  type: string
- description: ''
  name: keys_url
  type: string
- description: ''
  name: labels_url
  type: string
- description: ''
  name: languages_url
  type: string
- description: ''
  name: merges_url
  type: string
- description: ''
  name: milestones_url
  type: string
- description: ''
  name: notifications_url
  type: string
- description: ''
  name: pulls_url
  type: string
- description: ''
  name: releases_url
  type: string
- description: ''
  name: ssh_url
  type: string
- description: ''
  name: stargazers_url
  type: string
- description: ''
  name: statuses_url
  type: string
- description: ''
  name: subscribers_url
  type: string
- description: ''
  name: subscription_url
  type: string
- description: ''
  name: tags_url
  type: string
- description: ''
  name: teams_url
  type: string
- description: ''
  name: trees_url
  type: string
- description: ''
  name: clone_url
  type: string
- description: ''
  name: mirror_url
  type: string
- description: ''
  name: hooks_url
  type: string
- description: ''
  name: svn_url
  type: string
- description: ''
  name: homepage
  type: string
- description: ''
  name: language
  type: string
- description: ''
  name: forks_count
  type: integer
- description: ''
  name: stargazers_count
  type: integer
- description: ''
  name: watchers_count
  type: integer
- description: The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
  name: size
  type: integer
- description: The default branch of the repository.
  name: default_branch
  type: string
- description: ''
  name: open_issues_count
  type: integer
- description: Whether this repository acts as a template that can be used to generate new repositories.
  name: is_template
  type: boolean
- description: ''
  name: topics
  type: array
- description: Whether issues are enabled.
  name: has_issues
  type: boolean
- description: Whether projects are enabled.
  name: has_projects
  type: boolean
- description: Whether the wiki is enabled.
  name: has_wiki
  type: boolean
- description: ''
  name: has_pages
  type: boolean
- description: Whether downloads are enabled.
  name: has_downloads
  type: boolean
- description: Whether discussions are enabled.
  name: has_discussions
  type: boolean
- description: Whether the repository is archived.
  name: archived
  type: boolean
- description: Returns whether or not this repository disabled.
  name: disabled
  type: boolean
- description: 'The repository visibility: public, private, or internal.'
  name: visibility
  type: string
- description: ''
  name: pushed_at
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: Whether to allow rebase merges for pull requests.
  name: allow_rebase_merge
  type: boolean
- description: ''
  name: temp_clone_token
  type: string
- description: Whether to allow squash merges for pull requests.
  name: allow_squash_merge
  type: boolean
- description: Whether to allow Auto-merge to be used on pull requests.
  name: allow_auto_merge
  type: boolean
- description: Whether to delete head branches when pull requests are merged
  name: delete_branch_on_merge
  type: boolean
- description: Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.
  name: allow_update_branch
  type: boolean
- description: Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead.
  name: use_squash_pr_title_as_default
  type: boolean
- description: 'The default value for a squash merge commit title: - `PR_TITLE` - default to the pull request''s title. - `COMMIT_OR_PR_TITLE` - default to the commit''s title (if only one commit) or the pull request''s'
  name: squash_merge_commit_title
  type: string
- description: 'The default value for a squash merge commit message: - `PR_BODY` - default to the pull request''s body. - `COMMIT_MESSAGES` - default to the branch''s commit messages. - `BLANK` - default to a blank com'
  name: squash_merge_commit_message
  type: string
- description: 'The default value for a merge commit title. - `PR_TITLE` - default to the pull request''s title. - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from'
  name: merge_commit_title
  type: string
- description: The default value for a merge commit message. - `PR_TITLE` - default to the pull request's title. - `PR_BODY` - default to the pull request's body. - `BLANK` - default to a blank commit message.
  name: merge_commit_message
  type: string
- description: Whether to allow merge commits for pull requests.
  name: allow_merge_commit
  type: boolean
- description: Whether to allow forking this repo
  name: allow_forking
  type: boolean
- description: Whether to require contributors to sign off on web-based commits
  name: web_commit_signoff_required
  type: boolean
- description: ''
  name: open_issues
  type: integer
- description: ''
  name: watchers
  type: integer
- description: ''
  name: master_branch
  type: string
- description: ''
  name: starred_at
  type: string
- description: Whether anonymous git access is enabled for this repository
  name: anonymous_access_enabled
  type: boolean
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-pulls-api-repository-schema.json
slug: github-repo-pulls-api-repository
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: repository
---
