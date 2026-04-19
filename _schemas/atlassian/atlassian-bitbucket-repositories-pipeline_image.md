---
description: The definition of a Docker image that can be used for a Bitbucket Pipelines step execution context.
layout: schema
name: pipeline_image
properties_list:
- description: The name of the image. If the image is hosted on DockerHub the short name can be used, otherwise the fully qualified name is required here.
  name: name
  type: string
- description: The username needed to authenticate with the Docker registry. Only required when using a private Docker image.
  name: username
  type: string
- description: The password needed to authenticate with the Docker registry. Only required when using a private Docker image.
  name: password
  type: string
- description: The email needed to authenticate with the Docker registry. Only required when using a private Docker image.
  name: email
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-repositories-pipeline_image-schema.json
slug: atlassian-bitbucket-repositories-pipeline_image
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: pipeline_image
---
