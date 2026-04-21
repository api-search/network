---
consumed_apis:
- forms-api
description: Workflow capability for managing Google Forms - creating forms, collecting responses, and monitoring changes via watches. Used by form administrators and data analysts.
layout: capability
name: Google Forms Form Management
operations:
- description: Create a new form
  method: POST
  name: create-form
  path: /v1/forms
- description: Get form details
  method: GET
  name: get-form
  path: /v1/forms
- description: List form responses
  method: GET
  name: list-responses
  path: /v1/responses
- description: Get a single response
  method: GET
  name: get-response
  path: /v1/responses
- description: Create a notification watch
  method: POST
  name: create-watch
  path: /v1/watches
- description: List watches
  method: GET
  name: list-watches
  path: /v1/watches
- description: Delete a watch
  method: DELETE
  name: delete-watch
  path: /v1/watches
personas: []
provider_name: Google Forms
provider_slug: google-forms
search_terms:
- set up a pub/sub watch for form changes or new responses
- analyzes form responses and collects data
- delete watch
- Form Administrator
- batch update form
- get form details
- questionnaires
- get a single form response by id
- set publish settings
- notifications
- get response
- extend a watch's expiration by seven days
- forms
- form crud operations
- create a new google form with a title
- form response operations
- list responses
- creates and manages forms, monitors responses
- get form
- list form responses
- managing surveys, questions, and notification watches
- get a single response
- update form publish settings
- create watch
- create a notification watch
- delete a watch
- list watches
- Data Analyst
- google
- renew watch
- google forms
- creating and managing forms for data collection
- google workspace
- data collection
- create form
- list all active watches for a form
- create forms, collect responses, monitor changes
- apply batch updates to a form (add/remove/modify items)
- surveys
- watch notification operations
- delete a watch to stop notifications
- create a new form
- list all responses for a form
- get a google form's structure and settings
- responses
slug: form-management
tags:
- Google Forms
- Surveys
- Data Collection
- Notifications
tools:
- description: Create a new Google Form with a title
  hints:
    openWorld: true
    readOnly: false
  name: create-form
- description: Get a Google Form's structure and settings
  hints:
    openWorld: true
    readOnly: true
  name: get-form
- description: Apply batch updates to a form (add/remove/modify items)
  hints:
    readOnly: false
  name: batch-update-form
- description: Update form publish settings
  hints:
    readOnly: false
  name: set-publish-settings
- description: List all responses for a form
  hints:
    openWorld: true
    readOnly: true
  name: list-responses
- description: Get a single form response by ID
  hints:
    readOnly: true
  name: get-response
- description: Set up a Pub/Sub watch for form changes or new responses
  hints:
    readOnly: false
  name: create-watch
- description: List all active watches for a form
  hints:
    readOnly: true
  name: list-watches
- description: Delete a watch to stop notifications
  hints:
    destructive: true
  name: delete-watch
- description: Extend a watch's expiration by seven days
  hints:
    readOnly: false
  name: renew-watch
---
