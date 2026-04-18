---
description: ''
layout: schema
name: ExtensionPackageAttributes
properties_list:
- description: The unique name of the extension package.
  name: name
  type: string
- description: The human-readable display name.
  name: display_name
  type: string
- description: A description of the extension package capabilities.
  name: description
  type: string
- description: The current version using semantic versioning.
  name: version
  type: string
- description: The platform the extension supports.
  name: platform
  type: string
- description: Information about the extension package author.
  name: author
  type: object
- description: The availability level of the extension package.
  name: availability
  type: string
- description: Whether the extension package has been discontinued.
  name: discontinued
  type: boolean
- description: The current processing status.
  name: status
  type: string
- description: The URL on Adobe Exchange for public extensions.
  name: exchange_url
  type: string
- description: Path to the extension icon within the package.
  name: icon_path
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/extension-extension-package-attributes-schema.json
slug: extension-extension-package-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: ExtensionPackageAttributes
---
