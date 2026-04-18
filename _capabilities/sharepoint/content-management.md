---
consumed_apis:
- sp-sites-lists
- sp-files-search
description: Unified workflow for managing SharePoint content including sites, lists, items, files, and search. Used by content managers, site admins, and collaboration teams.
layout: capability
name: SharePoint Content Management
operations:
- description: ''
  method: GET
  name: get-web
  path: /v1/sites
- description: ''
  method: GET
  name: get-lists
  path: /v1/lists
- description: ''
  method: POST
  name: create-list
  path: /v1/lists
- description: ''
  method: GET
  name: get-list-items
  path: /v1/lists/{title}/items
- description: ''
  method: POST
  name: create-list-item
  path: /v1/lists/{title}/items
- description: ''
  method: GET
  name: get-files
  path: /v1/files
- description: ''
  method: GET
  name: search
  path: /v1/search
personas: []
provider_name: Microsoft SharePoint
provider_slug: sharepoint
search_terms:
- enterprise content management
- microsoft
- create a new sharepoint list
- get files
- list files in a sharepoint folder
- download file
- get list items
- get files in folder
- intranet
- upload a file to sharepoint
- update list item
- get current user's sharepoint profile
- delete a sharepoint list item
- get my user profile
- collaboration
- content management
- document management
- delete list item
- add an item to a sharepoint list
- upload file
- update a sharepoint list item
- search
- get web
- get lists
- search across all sharepoint content
- create list item
- get sharepoint site properties
- download a file from sharepoint
- list all sharepoint lists
- get items from a sharepoint list
- search query
- sharepoint
- create list
slug: content-management
tags:
- SharePoint
- Content Management
- Collaboration
- Document Management
tools:
- description: Get SharePoint site properties
  hints:
    idempotent: true
    readOnly: true
  name: get-web
- description: List all SharePoint lists
  hints:
    idempotent: true
    readOnly: true
  name: get-lists
- description: Create a new SharePoint list
  hints:
    idempotent: false
    readOnly: false
  name: create-list
- description: Get items from a SharePoint list
  hints:
    idempotent: true
    readOnly: true
  name: get-list-items
- description: Add an item to a SharePoint list
  hints:
    idempotent: false
    readOnly: false
  name: create-list-item
- description: Update a SharePoint list item
  hints:
    idempotent: true
    readOnly: false
  name: update-list-item
- description: Delete a SharePoint list item
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-list-item
- description: List files in a SharePoint folder
  hints:
    idempotent: true
    readOnly: true
  name: get-files-in-folder
- description: Upload a file to SharePoint
  hints:
    idempotent: false
    readOnly: false
  name: upload-file
- description: Download a file from SharePoint
  hints:
    idempotent: true
    readOnly: true
  name: download-file
- description: Search across all SharePoint content
  hints:
    idempotent: true
    readOnly: true
  name: search-query
- description: Get current user's SharePoint profile
  hints:
    idempotent: true
    readOnly: true
  name: get-my-user-profile
---
