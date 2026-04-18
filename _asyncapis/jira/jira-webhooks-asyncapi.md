---
channels:
- description: The endpoint that receives all Jira Cloud webhook event deliveries. The event type is identified by the webhookEvent field in the JSON payload. Jira retries failed deliveries (non-200 responses) up to 8 times with exponential backoff.
  name: /webhook
  operation: publish
  operation_id: receiveJiraWebhookEvent
  summary: Receive a Jira webhook event
description: Jira Cloud webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in your Jira instance. Webhooks can be registered via the Jira REST API or through the Jira administration UI. Each webhook delivery includes a JSON payload with details about the event, the affected entities, and a timestamp. Jira supports both dynamic webhooks (registered via REST API with expiration) and static webhooks (configured in app descriptors for Connect apps). Forge apps use a separate event trigger mechanism.
layout: asyncapi
messages:
- description: Triggered when a user creates a new issue. The payload includes the full issue details, the user who created it, and the changelog.
  name: jira:issue_created
  summary: Fired when a new issue is created in Jira.
  title: Issue Created
- description: Triggered when a user updates an issue. This includes field changes, status transitions, comments added, and other modifications. The payload includes the changelog showing what changed.
  name: jira:issue_updated
  summary: Fired when an existing issue is updated in Jira.
  title: Issue Updated
- description: Triggered when a user deletes an issue. The payload includes the issue details as they were before deletion.
  name: jira:issue_deleted
  summary: Fired when an issue is deleted from Jira.
  title: Issue Deleted
- description: Triggered when a user adds a comment to an issue. The payload includes the full comment details and the associated issue.
  name: comment_created
  summary: Fired when a comment is added to an issue.
  title: Comment Created
- description: Triggered when a user edits a comment on an issue. The payload includes the updated comment details and the associated issue.
  name: comment_updated
  summary: Fired when an existing comment on an issue is edited.
  title: Comment Updated
- description: Triggered when a user deletes a comment from an issue. The payload includes the deleted comment details and the associated issue.
  name: comment_deleted
  summary: Fired when a comment is removed from an issue.
  title: Comment Deleted
- description: ''
  name: issuelink_created
  summary: Fired when a link between issues is created.
  title: Issue Link Created
- description: ''
  name: issuelink_deleted
  summary: Fired when a link between issues is removed.
  title: Issue Link Deleted
- description: ''
  name: attachment_created
  summary: Fired when an attachment is added to an issue.
  title: Attachment Created
- description: ''
  name: attachment_deleted
  summary: Fired when an attachment is removed from an issue.
  title: Attachment Deleted
- description: ''
  name: worklog_created
  summary: Fired when a worklog entry is added to an issue.
  title: Worklog Created
- description: ''
  name: worklog_updated
  summary: Fired when a worklog entry is edited on an issue.
  title: Worklog Updated
- description: ''
  name: worklog_deleted
  summary: Fired when a worklog entry is removed from an issue.
  title: Worklog Deleted
- description: ''
  name: project_created
  summary: Fired when a new project is created.
  title: Project Created
- description: ''
  name: project_updated
  summary: Fired when a project is updated.
  title: Project Updated
- description: ''
  name: project_deleted
  summary: Fired when a project is permanently deleted.
  title: Project Deleted
- description: ''
  name: project_soft_deleted
  summary: Fired when a project is moved to the trash.
  title: Project Soft Deleted
- description: ''
  name: project_restored_deleted
  summary: Fired when a project is restored from the trash.
  title: Project Restored from Trash
- description: ''
  name: sprint_created
  summary: Fired when a sprint is created.
  title: Sprint Created
- description: ''
  name: sprint_updated
  summary: Fired when a sprint is updated.
  title: Sprint Updated
- description: ''
  name: sprint_deleted
  summary: Fired when a sprint is deleted.
  title: Sprint Deleted
- description: ''
  name: sprint_started
  summary: Fired when a sprint is started.
  title: Sprint Started
- description: ''
  name: sprint_closed
  summary: Fired when a sprint is closed (completed).
  title: Sprint Closed
- description: ''
  name: board_created
  summary: Fired when a board is created.
  title: Board Created
- description: ''
  name: board_updated
  summary: Fired when a board is updated.
  title: Board Updated
- description: ''
  name: board_deleted
  summary: Fired when a board is deleted.
  title: Board Deleted
- description: ''
  name: user_created
  summary: Fired when a new user is created.
  title: User Created
- description: ''
  name: user_updated
  summary: Fired when a user account is updated.
  title: User Updated
- description: ''
  name: user_deleted
  summary: Fired when a user account is deleted.
  title: User Deleted
- description: ''
  name: option_voting_changed
  summary: Fired when the voting option is enabled or disabled.
  title: Voting Option Changed
- description: ''
  name: option_watching_changed
  summary: Fired when the watching option is enabled or disabled.
  title: Watching Option Changed
- description: ''
  name: option_unassigned_issues_changed
  summary: Fired when the unassigned issues option is changed.
  title: Unassigned Issues Option Changed
- description: ''
  name: option_subtasks_changed
  summary: Fired when the sub-tasks option is enabled or disabled.
  title: Sub-tasks Option Changed
- description: ''
  name: option_attachments_changed
  summary: Fired when the attachments option is enabled or disabled.
  title: Attachments Option Changed
- description: ''
  name: option_issuelinks_changed
  summary: Fired when the issue links option is enabled or disabled.
  title: Issue Links Option Changed
- description: ''
  name: option_timetracking_changed
  summary: Fired when the time tracking option is enabled or disabled.
  title: Time Tracking Option Changed
name: Jira Cloud Webhooks
provider_name: Jira
provider_slug: jira
servers:
- description: Your webhook receiver endpoint. Jira sends POST requests to this URL when subscribed events occur. The URL must be publicly accessible and respond with a 200-level status code within 10 seconds.
  name: webhook-receiver
  protocol: https
  url: '{webhookUrl}'
slug: jira-webhooks-asyncapi
spec_file: asyncapi/jira-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/asyncapi/jira-webhooks-asyncapi.yml
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
- AsyncAPI
- Webhooks
- Events
version: '3'
---
