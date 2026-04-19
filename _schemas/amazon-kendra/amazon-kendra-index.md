---
description: An Amazon Kendra search index.
layout: schema
name: Index
properties_list:
- description: The unique identifier of the index.
  name: Id
  type: string
- description: The name of the index.
  name: Name
  type: string
- description: The current status of the index.
  name: Status
  type: string
- description: The Amazon Kendra edition.
  name: Edition
  type: string
- description: The IAM role ARN for the index.
  name: RoleArn
  type: string
- description: When the index was created.
  name: CreatedAt
  type: string
- description: When the index was last updated.
  name: UpdatedAt
  type: string
provider_name: Amazon Kendra
provider_slug: amazon-kendra
schema_file: json-schema/amazon-kendra-index-schema.json
slug: amazon-kendra-index
tags:
- AI
- AWS
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
title: Index
---
