---
channels:
- description: The endpoint that receives all GitHub webhook event deliveries. The specific event type is identified by the X-GitHub-Event header.
  name: /webhook
  operation: publish
  operation_id: receiveWebhookEvent
  summary: Receive a GitHub webhook event
description: GitHub Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur on GitHub, such as pushes, pull requests, issues, releases, and more. Webhooks can be configured at the repository, organization, or GitHub App level. Each delivery includes headers for event identification, delivery tracking, and HMAC signature verification.
layout: asyncapi
messages:
- description: Triggered when one or more commits are pushed to a repository branch or tag. This is one of the most common webhook events and includes details about all commits in the push.
  name: push
  summary: Commits pushed to a repository branch or tag.
  title: Push Event
- description: Triggered when a pull request is assigned, auto-merge enabled/disabled, closed, converted to draft, demilestoned, dequeued, edited, enqueued, labeled, locked, milestoned, opened, ready for review, reopened, review requested, review request removed, synchronized, unassigned, unlabeled, or unlocked.
  name: pull_request
  summary: Pull request opened, closed, merged, or updated.
  title: Pull Request Event
- description: Triggered when an issue is opened, edited, deleted, pinned, unpinned, closed, reopened, assigned, unassigned, labeled, unlabeled, locked, unlocked, transferred, milestoned, or demilestoned.
  name: issues
  summary: Issue opened, edited, closed, or updated.
  title: Issues Event
- description: ''
  name: issue_comment
  summary: Comment on issue or pull request created, edited, or deleted.
  title: Issue Comment Event
- description: Triggered when a Git branch or tag is created. This event does not include an action property.
  name: create
  summary: Branch or tag created.
  title: Create Event
- description: Triggered when a Git branch or tag is deleted. This event does not include an action property.
  name: delete
  summary: Branch or tag deleted.
  title: Delete Event
- description: ''
  name: release
  summary: Release created, published, edited, or deleted.
  title: Release Event
- description: Triggered when a user forks a repository. This event does not include an action property.
  name: fork
  summary: Repository forked.
  title: Fork Event
- description: Triggered when someone stars a repository. This is a legacy event name that fires on star activity. The star event was added later as the correctly named equivalent.
  name: watch
  summary: User starred a repository (legacy naming).
  title: Watch Event
- description: ''
  name: star
  summary: Repository starred or unstarred.
  title: Star Event
- description: ''
  name: check_run
  summary: Check run created, completed, or rerequested.
  title: Check Run Event
- description: ''
  name: check_suite
  summary: Check suite completed, requested, or rerequested.
  title: Check Suite Event
- description: ''
  name: commit_comment
  summary: Commit comment created.
  title: Commit Comment Event
- description: ''
  name: deployment
  summary: Deployment created.
  title: Deployment Event
- description: ''
  name: deployment_status
  summary: Deployment status updated.
  title: Deployment Status Event
- description: ''
  name: discussion
  summary: Discussion created, edited, answered, or updated.
  title: Discussion Event
- description: ''
  name: discussion_comment
  summary: Discussion comment created, edited, or deleted.
  title: Discussion Comment Event
- description: ''
  name: workflow_run
  summary: Workflow run requested, completed, or in progress.
  title: Workflow Run Event
- description: ''
  name: workflow_job
  summary: Workflow job queued, in progress, completed, or waiting.
  title: Workflow Job Event
- description: ''
  name: workflow_dispatch
  summary: Workflow manually triggered.
  title: Workflow Dispatch Event
- description: ''
  name: repository
  summary: Repository created, deleted, archived, or updated.
  title: Repository Event
- description: Triggered by a POST to the repository dispatch endpoint, allowing external systems to trigger GitHub Actions workflows with custom event payloads.
  name: repository_dispatch
  summary: Custom event triggered via the API.
  title: Repository Dispatch Event
- description: ''
  name: pull_request_review
  summary: Pull request review submitted, edited, or dismissed.
  title: Pull Request Review Event
- description: ''
  name: pull_request_review_comment
  summary: Pull request review comment created, edited, or deleted.
  title: Pull Request Review Comment Event
- description: ''
  name: pull_request_review_thread
  summary: Pull request review thread resolved or unresolved.
  title: Pull Request Review Thread Event
- description: ''
  name: code_scanning_alert
  summary: Code scanning alert created, fixed, or appeared in branch.
  title: Code Scanning Alert Event
- description: ''
  name: dependabot_alert
  summary: Dependabot alert activity.
  title: Dependabot Alert Event
- description: ''
  name: secret_scanning_alert
  summary: Secret scanning alert created, resolved, or reopened.
  title: Secret Scanning Alert Event
- description: ''
  name: security_advisory
  summary: Security advisory published, updated, or withdrawn.
  title: Security Advisory Event
- description: ''
  name: branch_protection_rule
  summary: Branch protection rule created, edited, or deleted.
  title: Branch Protection Rule Event
- description: ''
  name: branch_protection_configuration
  summary: Branch protection configuration enabled or disabled.
  title: Branch Protection Configuration Event
- description: ''
  name: member
  summary: Collaborator added, removed, or permissions edited.
  title: Member Event
- description: ''
  name: membership
  summary: Team membership added or removed.
  title: Membership Event
- description: ''
  name: organization
  summary: Organization membership changes.
  title: Organization Event
- description: ''
  name: team
  summary: Team created, deleted, edited, or child team changes.
  title: Team Event
- description: ''
  name: team_add
  summary: Repository added to a team.
  title: Team Add Event
- description: ''
  name: label
  summary: Label created, edited, or deleted.
  title: Label Event
- description: ''
  name: milestone
  summary: Milestone created, closed, opened, edited, or deleted.
  title: Milestone Event
- description: ''
  name: project_card
  summary: Project (classic) card activity.
  title: Project Card Event
- description: ''
  name: project
  summary: Project (classic) created, edited, closed, or updated.
  title: Project Event
- description: ''
  name: project_column
  summary: Project (classic) column activity.
  title: Project Column Event
- description: ''
  name: projects_v2
  summary: Projects v2 created, edited, closed, or updated.
  title: Projects V2 Event
- description: ''
  name: projects_v2_item
  summary: Projects v2 item activity.
  title: Projects V2 Item Event
- description: ''
  name: page_build
  summary: GitHub Pages build attempted.
  title: Page Build Event
- description: ''
  name: package
  summary: GitHub Package published or updated.
  title: Package Event
- description: ''
  name: public
  summary: Private repository made public.
  title: Public Event
- description: Triggered when a wiki page is created or updated. The event name gollum is a long-standing GitHub tradition derived from the Lord of the Rings character.
  name: gollum
  summary: Wiki page created or updated.
  title: Wiki Event
- description: ''
  name: installation
  summary: GitHub App installed, uninstalled, or permissions changed.
  title: Installation Event
- description: ''
  name: installation_repositories
  summary: Repositories added or removed from GitHub App installation.
  title: Installation Repositories Event
- description: ''
  name: github_app_authorization
  summary: GitHub App authorization revoked.
  title: GitHub App Authorization Event
- description: ''
  name: marketplace_purchase
  summary: GitHub Marketplace purchase activity.
  title: Marketplace Purchase Event
- description: ''
  name: merge_group
  summary: Merge group checks requested or destroyed.
  title: Merge Group Event
- description: Triggered when the webhook configuration that is receiving this event is deleted. This allows the receiver to clean up any state associated with the webhook.
  name: meta
  summary: The webhook itself is deleted.
  title: Meta Event
- description: ''
  name: org_block
  summary: Organization blocked or unblocked a user.
  title: Organization Block Event
- description: Sent when a new webhook is created to verify the endpoint is reachable. This is a connectivity test and is not subscribable as a regular event.
  name: ping
  summary: Test event sent when a webhook is first created.
  title: Ping Event
- description: ''
  name: deploy_key
  summary: Deploy key created or deleted.
  title: Deploy Key Event
- description: ''
  name: deployment_protection_rule
  summary: Deployment protection rule requested.
  title: Deployment Protection Rule Event
- description: ''
  name: deployment_review
  summary: Deployment review approved, rejected, or requested.
  title: Deployment Review Event
- description: ''
  name: status
  summary: Commit status updated.
  title: Status Event
- description: ''
  name: sponsorship
  summary: Sponsorship created, edited, tier changed, or cancelled.
  title: Sponsorship Event
- description: ''
  name: repository_advisory
  summary: Repository security advisory published or reported.
  title: Repository Advisory Event
- description: ''
  name: repository_ruleset
  summary: Repository ruleset created, edited, or deleted.
  title: Repository Ruleset Event
- description: ''
  name: repository_vulnerability_alert
  summary: Vulnerability alert created, dismissed, or resolved.
  title: Repository Vulnerability Alert Event
- description: ''
  name: personal_access_token_request
  summary: Fine-grained PAT request created, approved, or denied.
  title: Personal Access Token Request Event
- description: ''
  name: custom_property
  summary: Custom property created, updated, or deleted.
  title: Custom Property Event
- description: ''
  name: custom_property_values
  summary: Custom property values changed for a repository.
  title: Custom Property Values Event
- description: ''
  name: security_and_analysis
  summary: Code security or analysis features enabled or disabled.
  title: Security and Analysis Event
- description: ''
  name: secret_scanning_alert_location
  summary: Secret scanning alert location detected.
  title: Secret Scanning Alert Location Event
- description: ''
  name: sub_issues
  summary: Sub-issue added or removed.
  title: Sub Issues Event
- description: ''
  name: repository_import
  summary: Repository import activity.
  title: Repository Import Event
- description: ''
  name: registry_package
  summary: Registry package published or updated.
  title: Registry Package Event
- description: ''
  name: installation_target
  summary: Installation target renamed.
  title: Installation Target Event
- description: ''
  name: projects_v2_status_update
  summary: Projects v2 status update activity.
  title: Projects V2 Status Update Event
- description: ''
  name: issue_dependencies
  summary: Issue dependency added or removed.
  title: Issue Dependencies Event
- description: ''
  name: secret_scanning_scan
  summary: Secret scanning scan completed.
  title: Secret Scanning Scan Event
name: GitHub Webhooks
provider_name: GitHub
provider_slug: github
servers:
- description: Your webhook receiver endpoint. GitHub sends POST requests to this URL when subscribed events occur.
  name: webhook-receiver
  protocol: https
  url: '{webhookUrl}'
slug: github-webhooks-asyncapi
spec_file: asyncapi/github-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/asyncapi/github-webhooks-asyncapi.yml
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
- AsyncAPI
- Webhooks
- Events
version: '2022-11-28'
---
