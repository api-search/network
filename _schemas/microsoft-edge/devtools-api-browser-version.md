---
description: Browser version and protocol information from the Microsoft Edge DevTools Protocol
layout: schema
name: BrowserVersion
properties_list:
- description: Browser name and version
  name: Browser
  type: string
- description: DevTools Protocol version
  name: Protocol-Version
  type: string
- description: Full user agent string
  name: User-Agent
  type: string
- description: V8 JavaScript engine version
  name: V8-Version
  type: string
- description: WebKit rendering engine version
  name: WebKit-Version
  type: string
- description: WebSocket URL for browser-level debugging
  name: webSocketDebuggerUrl
  type: string
provider_name: Microsoft Edge
provider_slug: microsoft-edge
schema_file: json-schema/devtools-api-browser-version-schema.json
slug: devtools-api-browser-version
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
title: BrowserVersion
---
