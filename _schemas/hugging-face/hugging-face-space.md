---
description: Schema for a Space (interactive ML application) hosted on the Hugging Face Hub, including runtime configuration, SDK, hardware, and repository metadata.
layout: schema
name: Hugging Face Space
properties_list:
- description: Internal unique identifier for the Space
  name: _id
  type: string
- description: Space repository ID in the format author/space-name
  name: id
  type: string
- description: Author or organization that owns the Space
  name: author
  type: string
- description: Latest Git commit SHA
  name: sha
  type: string
- description: Timestamp of the last modification
  name: lastModified
  type: string
- description: Timestamp when the Space was created
  name: createdAt
  type: string
- description: Whether the Space is private
  name: private
  type: boolean
- description: Whether the Space has been disabled
  name: disabled
  type: boolean
- description: Tags associated with the Space
  name: tags
  type: array
- description: Number of likes/favorites
  name: likes
  type: integer
- description: SDK framework used to build the Space
  name: sdk
  type: string
- description: Version of the SDK
  name: sdk_version
  type: string
- description: Python version used
  name: python_version
  type: string
- description: Main application file (e.g., app.py)
  name: app_file
  type: string
- description: Port the application listens on (for Docker Spaces)
  name: app_port
  type: integer
- description: Emoji displayed next to the Space name
  name: emoji
  type: string
- description: Gradient start color for the Space card
  name: colorFrom
  type: string
- description: Gradient end color for the Space card
  name: colorTo
  type: string
- description: Whether the Space is pinned on the author's profile
  name: pinned
  type: boolean
- description: License identifier
  name: license
  type: string
- description: Brief description shown on the Space card
  name: short_description
  type: string
- description: Model IDs used by this Space
  name: models
  type: array
- description: Dataset IDs used by this Space
  name: datasets
  type: array
- description: Runtime status and configuration
  name: runtime
  type: object
- description: Files in the Space repository
  name: siblings
  type: array
- description: Parsed metadata from the Space card YAML front matter
  name: cardData
  type: object
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-space-schema.json
slug: hugging-face-space
tags: []
title: Hugging Face Space
---
