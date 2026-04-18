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
- google forms
- get form
- create forms, collect responses, monitor changes
- create form
- get a single response
- Form Administrator
- update form publish settings
- delete watch
- surveys
- get form details
- set publish settings
- Data Analyst
- apply batch updates to a form (add/remove/modify items)
- questionnaires
- create a notification watch
- create watch
- form crud operations
- get response
- form response operations
- responses
- create a new google form with a title
- get a single form response by id
- managing surveys, questions, and notification watches
- watch notification operations
- data collection
- delete a watch
- extend a watch's expiration by seven days
- create a new form
- notifications
- delete a watch to stop notifications
- google workspace
- creates and manages forms, monitors responses
- renew watch
- list responses
- get a google form's structure and settings
- google
- list watches
- batch update form
- creating and managing forms for data collection
- set up a pub/sub watch for form changes or new responses
- analyzes form responses and collects data
- forms
- list all responses for a form
- list all active watches for a form
- list form responses
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
