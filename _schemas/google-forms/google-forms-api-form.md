---
description: A Google Form with items, settings, and metadata.
layout: schema
name: Form
properties_list:
- description: Output only. The form ID.
  name: formId
  type: string
- description: General information about the form.
  name: info
  type: object
- description: Form-level settings including quiz configuration.
  name: settings
  type: object
- description: A list of the form's items including section headers, questions, and media.
  name: items
  type: array
- description: Output only. The revision ID of the form.
  name: revisionId
  type: string
- description: Output only. The form URI to share with responders.
  name: responderUri
  type: string
- description: Output only. The ID of the linked Google Sheet.
  name: linkedSheetId
  type: string
- description: ''
  name: publishSettings
  type: object
provider_name: Google Forms
provider_slug: google-forms
schema_file: json-schema/google-forms-api-form-schema.json
slug: google-forms-api-form
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
title: Form
---
