---
description: Schema for a machine learning model hosted on the Hugging Face Hub, including metadata, configuration, and repository information.
layout: schema
name: Hugging Face Model
properties_list:
- description: Internal unique identifier for the model
  name: _id
  type: string
- description: Model repository ID in the format author/model-name or model-name
  name: id
  type: string
- description: Alias for the model repository ID
  name: modelId
  type: string
- description: Author or organization that owns the model
  name: author
  type: string
- description: Latest Git commit SHA of the model repository
  name: sha
  type: string
- description: Timestamp of the last modification to the repository
  name: lastModified
  type: string
- description: Timestamp when the model repository was created
  name: createdAt
  type: string
- description: Whether the model repository is private
  name: private
  type: boolean
- description: Whether the model has been disabled
  name: disabled
  type: boolean
- description: Access gating configuration. False means no gating, 'auto' or 'manual' indicates gated access.
  name: gated
  type: object
- description: The primary task/pipeline this model is designed for
  name: pipeline_tag
  type: string
- description: Tags associated with the model including library, language, license, and custom tags
  name: tags
  type: array
- description: Primary ML library used by the model
  name: library_name
  type: string
- description: Total number of downloads in the last 30 days
  name: downloads
  type: integer
- description: Total number of all-time downloads
  name: downloadsAllTime
  type: integer
- description: Total number of likes/favorites
  name: likes
  type: integer
- description: List of files in the model repository
  name: siblings
  type: array
- description: List of Space IDs that use this model
  name: spaces
  type: array
- description: Safetensors metadata including parameter counts
  name: safetensors
  type: object
- description: Model configuration from config.json
  name: config
  type: object
- description: Parsed metadata from the model card (README.md YAML front matter)
  name: cardData
  type: object
- description: Transformers library-specific information
  name: transformersInfo
  type: object
- description: Widget example data for the model card inference widget
  name: widgetData
  type: array
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-model-schema.json
slug: hugging-face-model
tags: []
title: Hugging Face Model
---
