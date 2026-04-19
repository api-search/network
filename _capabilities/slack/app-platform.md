---
consumed_apis:
- slack-apps
- slack-views
- slack-dialog
- slack-bots
- slack-functions
- slack-workflows
- slack-calls
- slack-rtm
- slack-assistant
- slack-tests
description: Unified workflow for building Slack apps including app management, interactive views, dialogs, bots, workflow functions, calls, and real-time messaging. Used by platform developers building Slack integrations.
layout: capability
name: Slack App Platform
operations:
- description: List apps.
  method: GET
  name: list-apps
  path: /v1/apps
- description: Open a view.
  method: POST
  name: open-view
  path: /v1/views
- description: List workflows.
  method: GET
  name: list-workflows
  path: /v1/workflows
personas: []
provider_name: Slack
provider_slug: slack
search_terms:
- test api connectivity.
- app management.
- workflow management.
- manage calls
- bots
- api test
- chat
- list workflows
- open a view.
- team communication
- complete function
- view management.
- rtm connect
- collaboration
- open a dialog.
- platform
- get bot information.
- connect to real-time messaging.
- open view
- list apps.
- open a modal view.
- manage voice/video calls.
- app development
- manage assistant
- list installed apps.
- slack
- get bot info
- open dialog
- messaging
- automation
- manage workflows
- t1
- productivity
- manage ai assistant threads.
- list workflows.
- manage workflows.
- complete a workflow function.
- list apps
slug: app-platform
tags:
- Slack
- App Development
- Platform
- Automation
tools:
- description: List installed apps.
  hints:
    readOnly: true
  name: list-apps
- description: Open a modal view.
  hints:
    readOnly: false
  name: open-view
- description: Open a dialog.
  hints:
    readOnly: false
  name: open-dialog
- description: Get bot information.
  hints:
    readOnly: true
  name: get-bot-info
- description: Complete a workflow function.
  hints:
    readOnly: false
  name: complete-function
- description: Manage workflows.
  hints:
    readOnly: false
  name: manage-workflows
- description: Manage voice/video calls.
  hints:
    readOnly: false
  name: manage-calls
- description: Connect to Real-Time Messaging.
  hints:
    readOnly: true
  name: rtm-connect
- description: Manage AI assistant threads.
  hints:
    readOnly: false
  name: manage-assistant
- description: Test API connectivity.
  hints:
    readOnly: true
  name: api-test
---
