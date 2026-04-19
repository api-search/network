---
description: Represents a Monitron project.
layout: schema
name: Project
properties_list:
- description: The time at which the project was created.
  name: createdAt
  type: string
- description: The Amazon Resource Name (ARN) of the project.
  name: projectArn
  type: string
- description: The name of the project.
  name: projectName
  type: string
- description: The current status of the project.
  name: status
  type: string
- description: The time at which the project was last updated.
  name: updatedAt
  type: string
provider_name: Amazon Monitron
provider_slug: amazon-monitron
schema_file: json-schema/monitron-api-project-schema.json
slug: monitron-api-project
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Project
---
