---
aid: slack:slack-dialog-api
name: Slack Dialog API
tags:
  - Dialog
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-dialog-openapi.yml
    type: OpenAPI
description: >-
  Slack's Dialog API lets apps open form-like popups inside Slack to collect
  structured input from users. Apps trigger a dialog (often from a slash
  command, message action, or interactive message) by calling dialog.open with a
  short-lived trigger_id, then present fields like text inputs, textareas, and
  select menus (including dynamic, server-powered options). When users submit or
  cancel, Slack sends a dialog_submission or dialog_cancellation payload to the
  app, which can validate inputs and send dialog_errors for inline feedback
  before completing the workflow. Dialogs are ephemeral to the user and
  well-suited for tasks like creating tickets, requesting PTO, or gathering
  parameters. Note: Slack now recommends using Block Kit modals via the Views
  API, which supersede legacy dialogs.

---