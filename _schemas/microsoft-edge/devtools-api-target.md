---
description: A debuggable browser target from the Microsoft Edge DevTools Protocol HTTP API
layout: schema
name: Target
properties_list:
- description: Target description
  name: description
  type: string
- description: URL to the DevTools frontend for this target
  name: devtoolsFrontendUrl
  type: string
- description: URL to the target's favicon
  name: faviconUrl
  type: string
- description: Unique target identifier
  name: id
  type: string
- description: Page title
  name: title
  type: string
- description: Target type
  name: type
  type: string
- description: Current URL of the target
  name: url
  type: string
- description: WebSocket URL for debugging this target
  name: webSocketDebuggerUrl
  type: string
provider_name: Microsoft Edge
provider_slug: microsoft-edge
schema_file: json-schema/devtools-api-target-schema.json
slug: devtools-api-target
tags:
- Browser
- Chromium
- Developer Tools
- Edge
- Extensions
- Microsoft
- Progressive Web Apps
- Web Development
- WebView
title: Target
---
