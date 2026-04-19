---
class_count: 7
classes:
- name
- description
- identifier
- version
- platform
- publisher
- category
context_file: json-ld/google-chrome-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-chrome/refs/heads/main/json-ld/google-chrome-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Chrome from Google Chrome.
layout: jsonld
name: Google Chrome Context
namespaces:
- prefix: chrome
  uri: https://developer.chrome.com/docs/extensions/schema/
- prefix: chromeManagement
  uri: https://developers.google.com/chrome/management/schema/
- prefix: chromePolicy
  uri: https://developers.google.com/chrome/policy/schema/
- prefix: cws
  uri: https://developer.chrome.com/docs/webstore/schema/
- prefix: cdp
  uri: https://chromedevtools.github.io/devtools-protocol/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
properties:
- container: ''
  name: BrowserExtension
  type: ''
- container: ''
  name: ExtensionAction
  type: ''
- container: ''
  name: ServiceWorker
  type: ''
- container: ''
  name: ContentScript
  type: ''
- container: ''
  name: DeclarativeNetRequestRuleset
  type: ''
- container: ''
  name: ChromeWebStoreItem
  type: ''
- container: ''
  name: ManagedDevice
  type: ''
- container: ''
  name: TelemetryDevice
  type: ''
- container: ''
  name: TelemetryEvent
  type: ''
- container: ''
  name: TelemetryUser
  type: ''
- container: ''
  name: ChromePolicy
  type: ''
- container: ''
  name: PolicySchema
  type: ''
- container: ''
  name: DevToolsTarget
  type: ''
- container: ''
  name: CrUXRecord
  type: ''
- container: ''
  name: BuiltInAISession
  type: ''
- container: ''
  name: SafeBrowsingThreat
  type: ''
- container: ''
  name: url
  type: reference
- container: ''
  name: dateCreated
  type: dateTime
- container: ''
  name: dateModified
  type: dateTime
property_count: 19
provider_name: Google Chrome
provider_slug: google-chrome
slug: google-chrome-context
tags:
- Browser
- Chrome Extensions
- Developer Tools
- Web Platform
- JSON-LD
- Linked Data
- Semantic Web
---
