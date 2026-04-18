---
description: Schema for a dataset hosted on the Hugging Face Hub, including metadata, structure, splits, and repository information.
layout: schema
name: Hugging Face Dataset
properties_list:
- description: Internal unique identifier for the dataset
  name: _id
  type: string
- description: Dataset repository ID in the format author/dataset-name or dataset-name
  name: id
  type: string
- description: Author or organization that owns the dataset
  name: author
  type: string
- description: Latest Git commit SHA of the dataset repository
  name: sha
  type: string
- description: Timestamp of the last modification
  name: lastModified
  type: string
- description: Timestamp when the dataset was created
  name: createdAt
  type: string
- description: Whether the dataset is private
  name: private
  type: boolean
- description: Whether the dataset has been disabled
  name: disabled
  type: boolean
- description: Access gating configuration
  name: gated
  type: object
- description: Tags associated with the dataset
  name: tags
  type: array
- description: Number of downloads in the last 30 days
  name: downloads
  type: integer
- description: Number of likes/favorites
  name: likes
  type: integer
- description: Short description of the dataset
  name: description
  type: string
- description: Citation text for the dataset (BibTeX format)
  name: citation
  type: string
- description: Files in the dataset repository
  name: siblings
  type: array
- description: Parsed metadata from the dataset card YAML front matter
  name: cardData
  type: object
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-dataset-schema.json
slug: hugging-face-dataset
tags: []
title: Hugging Face Dataset
---
