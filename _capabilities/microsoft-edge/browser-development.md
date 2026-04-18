---
consumed_apis:
- devtools-api
- addons-api
description: Unified workflow for Microsoft Edge browser development combining DevTools Protocol debugging with Add-ons extension lifecycle management. Used by extension developers, web developers, and QA engineers.
layout: capability
name: Microsoft Edge Browser Development
operations:
- description: List all debuggable targets
  method: GET
  name: list-targets
  path: /v1/targets
- description: Open a new browser tab
  method: PUT
  name: create-target
  path: /v1/targets/new
- description: Get browser version info
  method: GET
  name: get-browser-version
  path: /v1/version
- description: List extension products
  method: GET
  name: list-products
  path: /v1/extensions
- description: Get extension details
  method: GET
  name: get-product
  path: /v1/extensions/{productId}
personas: []
provider_name: Microsoft Edge
provider_slug: microsoft-edge
search_terms:
- microsoft
- edge
- open a new browser tab
- browser debugging and inspection
- list extension products
- create submission
- developer tools
- browser development
- progressive web apps
- extension product detail
- get extension details
- web development
- list all debuggable browser targets in microsoft edge
- get protocol schema
- create target
- get browser version
- develops and publishes browser extensions for microsoft edge
- get the full devtools protocol schema definition
- bring a browser tab to the foreground
- get submission status
- upload package
- list all extension products in the edge add-ons store
- close a browser tab
- chromium
- list products
- browser version
- get upload status
- get browser version info
- Extension Developer
- Web Developer
- tests web applications and extensions using devtools automation
- extensions
- browser
- get microsoft edge browser version information
- list all debuggable targets
- get details of an extension product
- QA Engineer
- debugging
- create new browser target
- list extensions
- submit an extension for review and publishing
- upload a new extension package
- webview
- debuggable browser targets
- list targets
- check the status of an extension submission
- extension products
- close target
- open a new browser tab in microsoft edge
- unified browser development workflow combining debugging and extension management
- activate target
- get extension
- check the status of a package upload
- automation
- get product
- develops web applications and uses devtools for debugging
- microsoft edge
- extension lifecycle from development to publication
slug: browser-development
tags:
- Microsoft Edge
- Browser Development
- Extensions
- Debugging
- Automation
tools:
- description: List all debuggable browser targets in Microsoft Edge
  hints:
    openWorld: true
    readOnly: true
  name: list-targets
- description: Open a new browser tab in Microsoft Edge
  hints:
    readOnly: false
  name: create-target
- description: Bring a browser tab to the foreground
  hints:
    readOnly: false
  name: activate-target
- description: Close a browser tab
  hints:
    destructive: true
    readOnly: false
  name: close-target
- description: Get Microsoft Edge browser version information
  hints:
    openWorld: true
    readOnly: true
  name: get-browser-version
- description: Get the full DevTools Protocol schema definition
  hints:
    openWorld: true
    readOnly: true
  name: get-protocol-schema
- description: List all extension products in the Edge Add-ons store
  hints:
    openWorld: true
    readOnly: true
  name: list-extensions
- description: Get details of an extension product
  hints:
    openWorld: true
    readOnly: true
  name: get-extension
- description: Submit an extension for review and publishing
  hints:
    readOnly: false
  name: create-submission
- description: Check the status of an extension submission
  hints:
    openWorld: true
    readOnly: true
  name: get-submission-status
- description: Upload a new extension package
  hints:
    readOnly: false
  name: upload-package
- description: Check the status of a package upload
  hints:
    openWorld: true
    readOnly: true
  name: get-upload-status
---
