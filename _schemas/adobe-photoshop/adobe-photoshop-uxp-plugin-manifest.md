---
description: Schema for the manifest.json file required by UXP plugins for Adobe Photoshop. The manifest defines plugin metadata, entry points, permissions, and host application requirements.
layout: schema
name: Adobe Photoshop UXP Plugin Manifest
properties_list:
- description: Unique plugin identifier. Use reverse domain notation (e.g., com.example.myplugin).
  name: id
  type: string
- description: Display name of the plugin shown in the Photoshop UI.
  name: name
  type: string
- description: Plugin version in semver format (major.minor.patch).
  name: version
  type: string
- description: UXP manifest schema version. Version 5 or 6 recommended for current Photoshop.
  name: manifestVersion
  type: integer
- description: Path to the main JavaScript entry point file relative to the plugin root.
  name: main
  type: string
- description: Host application requirements.
  name: host
  type: object
- description: Plugin entry points defining panels, commands, and other UI elements.
  name: entrypoints
  type: array
- description: Plugin icons at various sizes for different display contexts.
  name: icons
  type: array
- description: Permissions the plugin requires to function.
  name: requiredPermissions
  type: object
- description: Configuration for hybrid plugin native C++ addon.
  name: addon
  type: object
- description: Short description of the plugin's purpose.
  name: description
  type: string
- description: Plugin author or company name.
  name: author
  type: string
- description: Keywords for plugin discovery in the Adobe Marketplace.
  name: keywords
  type: array
provider_name: Adobe Photoshop
provider_slug: adobe-photoshop
schema_file: json-schema/adobe-photoshop-uxp-plugin-manifest-schema.json
slug: adobe-photoshop-uxp-plugin-manifest
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
title: Adobe Photoshop UXP Plugin Manifest
---
