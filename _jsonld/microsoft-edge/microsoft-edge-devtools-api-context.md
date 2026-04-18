---
class_count: 3
classes:
- Target
- BrowserVersion
- ProtocolSchema
context_file: json-ld/microsoft-edge-devtools-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/json-ld/microsoft-edge-devtools-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Microsoft Edge Devtools Api from Microsoft Edge.
layout: jsonld
name: Microsoft Edge Devtools Api Context
namespaces:
- prefix: edge
  uri: https://developer.microsoft.com/microsoft-edge/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: url
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: devtoolsFrontendUrl
  type: string
- container: ''
  name: faviconUrl
  type: reference
- container: ''
  name: webSocketDebuggerUrl
  type: string
- container: ''
  name: browser
  type: string
- container: ''
  name: protocolVersion
  type: string
- container: ''
  name: userAgent
  type: string
- container: ''
  name: v8Version
  type: string
- container: ''
  name: webKitVersion
  type: string
- container: set
  name: domains
  type: ''
- container: set
  name: commands
  type: ''
- container: set
  name: events
  type: ''
property_count: 16
provider_name: Microsoft Edge
provider_slug: microsoft-edge
slug: microsoft-edge-devtools-api-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
