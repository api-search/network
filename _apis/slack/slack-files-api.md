---
aid: slack:slack-files-api
name: Slack Files API
tags:
  - Files
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-files-openapi.yml
    type: OpenAPI
description: >-
  Slack's Files API lets apps programmatically upload, share, and manage files
  in Slack. Apps can upload binaries (images, docs, code snippets) or register
  links to external files, then attach them to channels, DMs, or threads with
  optional captions. The API supports retrieving file metadata and content,
  listing and filtering files, generating or revoking public share links, and
  deleting files, with access controlled by app scopes and channel membership.
  For large uploads, a two-step flow provides an upload URL before finalizing
  the file, and related Events API notifications (for example, file_created and
  file_shared) let apps react to changes. Common uses include import/export
  pipelines, compliance and archiving tools, and integrations with cloud
  storage.

---