---
description: Application from Adobe Illustrator API
layout: schema
name: Application
properties_list:
- description: The application name.
  name: name
  type: string
- description: The version string.
  name: version
  type: string
- description: The build number.
  name: buildNumber
  type: string
- description: The current locale.
  name: locale
  type: string
- description: The scripting API version.
  name: scriptingVersion
  type: string
- description: Available memory in bytes.
  name: freeMemory
  type: integer
- description: Name of the currently active document.
  name: activeDocument
  type: string
- description: List of open document names.
  name: documents
  type: array
- description: The level of user interaction allowed.
  name: userInteractionLevel
  type: string
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-application-schema.json
slug: adobe-illustrator-scripting-application
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: Application
---
