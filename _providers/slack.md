---
api_count: 39
apis:
- description: The Slack Admin API is a set of privileged endpointsprimarily under admin.* with related SCIM and Audit Logs APIsthat lets Enterprise Grid owners and admins automate organizationwide management and go
  name: Slack Admin API
  slug: slack-admin-api
- description: I'm not aware of an official Slack product literally called Tests API. Typically, when people say Slack Tests API, they mean using Slack's existing APIs and SDK tooling to automate tests for Slack app
  name: Slack Tests API
  slug: slack-tests-api
- description: The Slack Apps API is a set of platform APIs and tools that let developers build apps to extend Slack and automate work. With it, you can read and write data via the Web API (messages, channels, files
  name: Slack Apps API
  slug: slack-apps-api
- description: The Slack Assistant API provides the assistant.threads.* Web API methods that let apps building AI-powered assistants manage threaded conversations in Slack. It includes methods to set the status of a
  name: Slack Assistant API
  slug: slack-assistant-api
- description: Slack's Auth API covers the authentication and authorization pieces that let apps securely identify users and workspaces and manage access. It includes OAuth 2.0 endpoints used during app installation
  name: Slack Auth API
  slug: slack-auth-api
- description: The Slack Bookmarks API provides the ability to add, remove, edit, or list curated resources directly in public channels, private channels, direct messages, multi-person direct messages, and shared ch
  name: Slack Bookmarks API
  slug: slack-bookmarks-api
- description: 'Slack''s bot APIs let you build apps that live in Slack and automate work by listening for events and taking actions in conversations. Using the Web API, your bot can post and schedule messages, reply '
  name: Slack Bots API
  slug: slack-bots-api
- description: 'Slack''s Calls API lets apps represent thirdparty voice or video calls inside Slack by creating a call object with a join URL and metadata, so users see a rich call message with a Join button, status, '
  name: Slack Calls API
  slug: slack-calls-api
- description: The Slack Canvases API lets apps programmatically create, edit, delete, and manage access to Slack Canvases, which are rich document surfaces embedded within Slack. Key methods include canvases.create
  name: Slack Canvases API
  slug: slack-canvases-api
- description: 'The Slack Chat API is the set of chat.* methods in the Slack Web API that lets apps and bots create and manage messages in Slack workspaces. It enables posting messages to channels and DMs with Block '
  name: Slack Chat API
  slug: slack-chat-api
- description: The Slack Conversations API is the unified Web API for working with all types of Slack conversationspublic and private channels, direct messages, and multi-person DMs. It lets apps discover and inspec
  name: Slack Conversations API
  slug: slack-conversations-api
- description: Slack's Dialog API lets apps open form-like popups inside Slack to collect structured input from users. Apps trigger a dialog (often from a slash command, message action, or interactive message) by ca
  name: Slack Dialog API
  slug: slack-dialog-api
- description: 'Slack''s Do Not Disturb (DND) API lets apps read and manage users'' notification quiet time so they don''t get pinged when they''ve paused alerts. With the dnd:read and dnd:write scopes, an app can check '
  name: Slack DND API
  slug: slack-dnd-api
- description: Slack's Emoji API lets apps discover and manage a workspace's custom emoji. The core method, emoji.list (requires the emoji:read scope), returns a name-to-URL map of all custom emoji along with aliase
  name: Slack Emoji API
  slug: slack-emoji-api
- description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occu
  name: Slack Events API
  slug: slack-events-api
- description: Slack's Files API lets apps programmatically upload, share, and manage files in Slack. Apps can upload binaries (images, docs, code snippets) or register links to external files, then attach them to c
  name: Slack Files API
  slug: slack-files-api
- description: 'The Slack Functions API provides methods for managing custom functions that run as steps within Slack workflows. The key methods are functions.completeSuccess, which marks a custom function as having '
  name: Slack Functions API
  slug: slack-functions-api
- description: The Slack Lists API provides methods for programmatically creating and managing Lists, a structured data surface in Slack for tracking work items, tasks, and records. Methods include slackLists.create
  name: Slack Lists API
  slug: slack-lists-api
- description: Slack's Migration API is a Web API used during Enterprise Grid migrations to translate legacy, workspace-scoped identifiers into their new, canonical IDs so apps keep working after a workspace moves o
  name: Slack Migration API
  slug: slack-migration-api
- description: The Slack OAuth API implements the OAuth 2.0 flow that lets developers securely install Slack apps to workspaces and obtain access tokens with specific, granular scopes. An app redirects a user to Sla
  name: Slack OAuth API
  slug: slack-oauth-api
- description: The Slack OpenID Connect API implements the Sign in with Slack flow based on the OpenID Connect standard built on top of OAuth 2.0. It includes openid.connect.token for exchanging an authorization cod
  name: Slack OpenID Connect API
  slug: slack-openid-connect-api
- description: The Slack Pins API is a set of Web API methods that let your app manage pinned items in conversations so important content is easy to find. With pins.add, pins.list, and pins.remove, you can programma
  name: Slack Pins API
  slug: slack-pins-api
- description: Slack's Reactions API lets apps programmatically manage emoji reactions on messages and files, making it easy to capture lightweight feedback like approvals, acknowledgments, or votes. Through Web API
  name: Slack Reactions API
  slug: slack-reactions-api
- description: Slack's Reminders API lets apps create and manage personal reminders for Slack users, so teams can automate nudges, followups, and routine checkins without leaving Slack. Through Web API methods, an a
  name: Slack Reminders API
  slug: slack-reminders-api
- description: 'The Slack Real Time Messaging (RTM) API lets an app open a WebSocket connection to Slack and receive a live stream of JSON events from a workspacesuch as new messages, edits, reactions, user presence '
  name: Slack RTM API
  slug: slack-rtm-api
- description: The Slack SCIM API lets teams on Plus and Enterprise plans provision and manage user accounts and groups programmatically using the SCIM (System for Cross-domain Identity Management) protocol. It supp
  name: Slack SCIM API
  slug: slack-scim-api
- description: The Slack Audit Logs API is designed for building security information and event management (SIEM) tools for Slack Enterprise Grid organizations. It provides a read-only view of audit events happening
  name: Slack Audit Logs API
  slug: slack-audit-logs-api
- description: Slack's Search API lets apps programmatically find messages and files in a workspace using the same query syntax users have in Slack (e.g., in:, from:, has:, before:/after:, is:thread). Through endpoi
  name: Slack Search API
  slug: slack-search-api
- description: The Slack Stars API is a set of Web API methods that let apps manage a user's starred itemsSlack's legacy personal bookmarking feature. It allows adding or removing a star on items such as messages (v
  name: Slack Stars API
  slug: slack-stars-api
- description: Slack's Team API is the part of the Slack Web API that lets apps read workspace-level (team) information and, for admins, certain audit and billing data. With it, apps can fetch basic workspace identi
  name: Slack Team API
  slug: slack-team-api
- description: Slack's User Groups API lets apps programmatically create and manage user groups (mentionable aliases like @eng or @oncall) in a workspace. It supports creating, renaming, and updating groups and thei
  name: Slack User Groups API
  slug: slack-user-groups-api
- description: 'Slack''s Users API is a set of Web API methods that let your app discover and work with people in a Slack workspace. It can list members, fetch details for a specific user, look up users by email, and '
  name: Slack Users API
  slug: slack-users-api
- description: The Slack Views API lets your app build and control Block Kit interfaces inside Slackprimarily modals and the App Home tab. With methods like views.open, views.update, and views.push, your app can lau
  name: Slack Views API
  slug: slack-views-api
- description: Slack's Workflows API lets you automate work inside Slack by defining workflowsordered steps or functionsthat run in response to triggers like shortcuts, messages, schedules, link clicks, or webhooks.
  name: Slack Workflows API
  slug: slack-workflows-api
- description: 'The Slack Web API is an HTTP-based interface that provides access to all of Slack''s platform features. It consists of over 200 methods organized by functional area (chat, conversations, users, files, '
  name: Slack Web API
  slug: slack-web-api
- description: Slack Incoming Webhooks provide a simple way to post messages from external sources into Slack. Creating an incoming webhook gives you a unique URL to which you send a JSON payload with the message te
  name: Slack Incoming Webhooks API
  slug: slack-incoming-webhooks-api
- description: Slack Slash Commands allow users to invoke app functionality directly from the message composer box by typing a forward slash followed by a command name and optional parameters. When a user triggers a
  name: Slack Slash Commands API
  slug: slack-slash-commands-api
- description: The Slack App Manifest API provides methods to programmatically create, configure, update, export, validate, and delete Slack apps using JSON or YAML manifest files. Key methods include apps.manifest.
  name: Slack App Manifest API
  slug: slack-app-manifest-api
- description: The Slack Interactivity API encompasses the mechanisms by which Slack apps handle user interactions with interactive components such as buttons, menus, date pickers, modals, shortcuts, and other Block
  name: Slack Interactivity API
  slug: slack-interactivity-api
asyncapis:
- description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occu
  name: Slack Events API
  slug: slack-events-asyncapi
capabilities:
- description: Unified workflow for building Slack apps including app management, interactive views, dialogs, bots, workflow functions, calls, and real-time messaging. Used by platform developers building Slack inte
  name: Slack App Platform
  slug: app-platform
- description: Unified workflow for messaging and communication including posting messages, managing conversations, sharing files, reacting, searching, and organizing with pins and stars. Used by app developers buil
  name: Slack Messaging and Communication
  slug: messaging-communication
- description: Unified workflow for workspace administration including admin controls, team settings, user management, user groups, authentication, and enterprise migration. Used by workspace administrators and IT t
  name: Slack Workspace Administration
  slug: workspace-administration
common:
- title: ''
  type: StatusPage
  url: https://slack-status.com/
- title: ''
  type: Portal
  url: https://api.slack.com/
- title: ''
  type: GettingStarted
  url: https://api.slack.com/automation/quickstart
- title: ''
  type: CodeExamples
  url: https://api.slack.com/samples
- title: ''
  type: Sandbox
  url: https://api.slack.com/docs/developer-sandbox
- title: ''
  type: Authentication
  url: https://api.slack.com/authentication
- title: ''
  type: Tutorials
  url: https://api.slack.com/tutorials
- title: ''
  type: TermsOfService
  url: https://api.slack.com/developer-policy
- title: ''
  type: TermsOfService
  url: https://slack.com/intl/en-gb/terms-of-service/api-updated?_gl=1*1yvqubm*_gcl_au*ODQ0OTgxOTg3LjE3MzU5NDg2ODY.*_ga*MTk4NzA1NTA3Ny4xNzM1OTQ4Njg3*_ga_QTJQME5M5D*MTczNTk0ODY4NS4xLjEuMTczNTk0ODk4My41LjAuMA..
- title: ''
  type: Blog
  url: https://slack.com/intl/en-gb/blog
- title: ''
  type: Plans
  url: https://slack.com/pricing
- title: ''
  type: OAuth
  url: https://api.slack.com/authentication/oauth-v2
- title: ''
  type: Marketplace
  url: https://slack.com/apps
- title: ''
  type: Community
  url: https://api.slack.com/community
- title: ''
  type: Support
  url: https://api.slack.com/support
- title: ''
  type: PrivacyPolicy
  url: https://slack.com/privacy-policy
- title: ''
  type: ChangeLog
  url: https://api.slack.com/changelog
- title: ''
  type: SDK
  url: https://api.slack.com/tools
- title: ''
  type: RateLimits
  url: https://docs.slack.dev/apis/web-api/rate-limits
- title: ''
  type: Security
  url: https://docs.slack.dev/security
- title: ''
  type: Scopes
  url: https://docs.slack.dev/reference/scopes
- title: ''
  type: BlockKit
  url: https://docs.slack.dev/block-kit
- title: ''
  type: Webhooks
  url: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks
- title: ''
  type: EventsAPI
  url: https://docs.slack.dev/apis/events-api
- title: ''
  type: SocketMode
  url: https://docs.slack.dev/apis/events-api/using-socket-mode
- title: ''
  type: SlackConnect
  url: https://docs.slack.dev/apis/slack-connect
- title: ''
  type: OpenAPISpecs
  url: https://github.com/slackapi/slack-api-specs
- title: ''
  type: GitHubOrganization
  url: https://github.com/slackapi
- title: Python SDK
  type: SDK
  url: https://github.com/slackapi/python-slack-sdk
- title: Node.js SDK
  type: SDK
  url: https://github.com/slackapi/node-slack-sdk
- title: Java SDK
  type: SDK
  url: https://github.com/slackapi/java-slack-sdk
- title: Bolt for Python
  type: SDK
  url: https://github.com/slackapi/bolt-python
- title: Bolt for JavaScript
  type: SDK
  url: https://github.com/slackapi/bolt-js
- title: Deno SDK
  type: SDK
  url: https://github.com/slackapi/deno-slack-sdk
- title: MCP Plugin
  type: Resources
  url: https://github.com/slackapi/slack-mcp-plugin
- title: GitHub Action
  type: Resources
  url: https://github.com/slackapi/slack-github-action
- title: Manifest Schema
  type: Resources
  url: https://github.com/slackapi/manifest-schema
- title: ''
  type: DeveloperProgram
  url: https://api.slack.com/developer-program
- title: ''
  type: ApplicationManagement
  url: https://api.slack.com/apps
- title: ''
  type: Marketplace
  url: https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace
- title: ''
  type: SecurityBestPractices
  url: https://docs.slack.dev/authentication/best-practices-for-security
- title: ''
  type: APIReference
  url: https://docs.slack.dev/reference/methods
- title: ''
  type: GettingStarted
  url: https://docs.slack.dev/quickstart
- title: ''
  type: CLI
  url: https://docs.slack.dev/tools/slack-cli
- title: ''
  type: DenoSDK
  url: https://docs.slack.dev/tools/deno-slack-sdk
- title: ''
  type: BoltJavaSDK
  url: https://docs.slack.dev/tools/java-slack-sdk
- title: ''
  type: AppManifest
  url: https://docs.slack.dev/app-manifests
- title: ''
  type: Interactivity
  url: https://docs.slack.dev/interactivity
- title: ''
  type: FAQ
  url: https://docs.slack.dev/faq
- title: ''
  type: DeveloperSupport
  url: https://docs.slack.dev/developer-support
- title: ''
  type: SignUp
  url: https://api.slack.com/developer-program/join
- title: ''
  type: TermsOfService
  url: https://slack.com/terms-of-service/api
- title: ''
  type: DeveloperChangelog
  url: https://docs.slack.dev/changelog
- title: ''
  type: DeveloperBlog
  url: https://slack.dev
- title: ''
  type: SlashCommands
  url: https://docs.slack.dev/interactivity/slash-commands
- title: ''
  type: BlockKitReference
  url: https://docs.slack.dev/reference/block-kit
- title: ''
  type: AuditLogsAPIReference
  url: https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference
- title: ''
  type: SCIMAPIReference
  url: https://docs.slack.dev/reference/scim-api
- title: ''
  type: SpectralRules
  url: rules/slack-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/slack-vocabulary.yaml
- title: Messaging and Communication
  type: NaftikoCapability
  url: capabilities/messaging-communication.yaml
- title: Workspace Administration
  type: NaftikoCapability
  url: capabilities/workspace-administration.yaml
- title: App Platform
  type: NaftikoCapability
  url: capabilities/app-platform.yaml
created: '2024-04-04'
description: Slack is a cloud-based team collaboration platform that provides chat, file sharing, and integrations with other tools and services.
features:
- name: Real-time messaging with channels, threads, and direct messages
- name: Block Kit interactive UI framework for rich message formatting
- name: Workflow Builder for no-code and custom automation steps
- name: Events API and Socket Mode for real-time event-driven integrations
- name: Slash commands and interactive components for user-triggered actions
- name: Canvas and Lists surfaces for structured document collaboration
- name: Enterprise Grid with organization-wide admin controls and SCIM provisioning
- name: Audit Logs API for security monitoring and compliance
- name: AI assistant framework for building conversational agents in Slack
- name: Incoming and outgoing webhooks for simple integrations
image: https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png
integrations:
- name: Python Slack SDK for building bots and web API clients
- name: Node.js Bolt framework for rapid app development
- name: Java Slack SDK for enterprise Java applications
- name: Deno Slack SDK for serverless Slack functions
- name: Slack CLI for local development and app deployment
- name: Incoming Webhooks for simple message posting from external systems
- name: SCIM API for identity provider integration and user provisioning
jsonld:
- class_count: 0
  name: Slack Context
  property_count: 8
  slug: slack-context
- class_count: 0
  name: Slack Web Context
  property_count: 0
  slug: slack-web-context
layout: provider
modified: '2026-04-18'
name: Slack
rules:
- name: Slack API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: slack-spectral-rules
skills: []
slug: slack
solutions: []
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
url: https://raw.githubusercontent.com/api-search/messaging/main/_apis/slack/apis.md
use_cases:
- name: DevOps teams automating deployment notifications and incident response
- name: Customer support teams routing tickets and managing escalations
- name: HR teams onboarding employees with automated workflows and reminders
- name: Sales teams receiving CRM alerts and managing deal updates in channels
- name: Engineering teams integrating CI/CD pipelines and code review notifications
- name: IT admins provisioning users and managing workspace security at scale
- name: Product teams collecting feedback with interactive surveys and polls
---
