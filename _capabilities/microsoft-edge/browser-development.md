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
- browser development
- get microsoft edge browser version information
- check the status of a package upload
- get upload status
- developer tools
- list targets
- microsoft
- develops and publishes browser extensions for microsoft edge
- extensions
- open a new browser tab in microsoft edge
- debuggable browser targets
- close target
- activate target
- get submission status
- list all debuggable browser targets in microsoft edge
- list products
- get protocol schema
- open a new browser tab
- tests web applications and extensions using devtools automation
- get extension
- chromium
- get product
- debugging
- check the status of an extension submission
- get details of an extension product
- create target
- list all extension products in the edge add-ons store
- create submission
- QA Engineer
- browser version
- list all debuggable targets
- close a browser tab
- edge
- webview
- Web Developer
- extension lifecycle from development to publication
- unified browser development workflow combining debugging and extension management
- microsoft edge
- browser debugging and inspection
- web development
- develops web applications and uses devtools for debugging
- progressive web apps
- upload package
- automation
- bring a browser tab to the foreground
- upload a new extension package
- browser
- Extension Developer
- get browser version
- extension products
- get the full devtools protocol schema definition
- submit an extension for review and publishing
- get extension details
- list extension products
- get browser version info
- list extensions
- create new browser target
- extension product detail
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
