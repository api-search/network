---
channels:
- description: The endpoint that receives all GitLab webhook event deliveries. The specific event type is identified by the X-Gitlab-Event header.
  name: /webhook
  operation: publish
  operation_id: receiveGitLabWebhookEvent
  summary: Receive a GitLab webhook event
description: GitLab Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in a GitLab project or group, such as pushes, merge requests, issues, pipeline status changes, and deployments. Webhooks are configured at the project or group level and include an X-Gitlab-Token header for payload signature verification.
layout: asyncapi
messages:
- description: Delivered when one or more commits are pushed to a branch in the repository. Contains information about the commits, the branch affected, and the user who performed the push.
  name: PushEvent
  summary: Triggered when code is pushed to a repository branch.
  title: Push Hook
- description: Delivered when a Git tag is pushed to or deleted from the repository. Contains the tag name, the commit it points to, and the user who performed the action.
  name: TagPushEvent
  summary: Triggered when a tag is created or deleted.
  title: Tag Push Hook
- description: Delivered when a merge request is opened, edited, closed, merged, approved, or has its reviewers changed. Contains detailed information about the merge request state, participants, and source/target branches.
  name: MergeRequestEvent
  summary: Triggered when a merge request is created, updated, or closed.
  title: Merge Request Hook
- description: Delivered when an issue is opened, edited, closed, or reopened. Contains details about the issue including title, description, labels, assignees, and milestone.
  name: IssueEvent
  summary: Triggered when an issue is created, updated, or closed.
  title: Issue Hook
- description: Delivered when a user adds a comment on a commit, merge request, issue, or code snippet. The noteable_type field identifies what the comment was made on.
  name: NoteEvent
  summary: Triggered when a comment is added on a commit, MR, issue, or snippet.
  title: Note Hook
- description: Delivered when a pipeline transitions between states such as pending, running, success, failed, or canceled. Contains information about the pipeline's stages, the triggering commit, and all jobs in the pipeline.
  name: PipelineEvent
  summary: Triggered when a CI/CD pipeline changes status.
  title: Pipeline Hook
- description: Delivered when an individual CI/CD job transitions between states. Contains information about the job, its runner, the associated pipeline, and any artifacts produced.
  name: JobEvent
  summary: Triggered when a CI/CD job changes status.
  title: Job Hook
- description: Delivered during deployment lifecycle transitions. Contains information about the environment, deployment ID, the ref being deployed, and the deployment status.
  name: DeploymentEvent
  summary: Triggered when a deployment starts, succeeds, fails, or is canceled.
  title: Deployment Hook
- description: Delivered when a release is created, updated, or deleted. Contains details about the release including its tag, name, description, and associated assets.
  name: ReleaseEvent
  summary: Triggered when a release is created, updated, or deleted.
  title: Release Hook
- description: Delivered when a user is added to or removed from a group, or when their access level is changed. Contains information about the member, their access level, and the group affected.
  name: MemberEvent
  summary: Triggered when a group member is added, removed, or changes access level.
  title: Member Hook
- description: Delivered when a wiki page is created, edited, or deleted in a project. Contains information about the wiki page including its slug, title, content, and the action performed.
  name: WikiPageEvent
  summary: Triggered when a wiki page is created, updated, or deleted.
  title: Wiki Page Hook
name: GitLab Webhooks
provider_name: GitLab
provider_slug: gitlab
servers:
- description: Your webhook receiver endpoint. GitLab sends POST requests to this URL when subscribed events occur in the configured project or group.
  name: webhook-receiver
  protocol: https
  url: '{webhookUrl}'
slug: gitlab-webhooks-asyncapi
spec_file: asyncapi/gitlab-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/asyncapi/gitlab-webhooks-asyncapi.yml
tags:
- Code
- Platform
- Software Development
- Source Control
- AsyncAPI
- Webhooks
- Events
version: '4'
---
